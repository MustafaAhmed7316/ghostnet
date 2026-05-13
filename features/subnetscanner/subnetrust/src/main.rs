use tokio::net::TcpStream;
use std::net::SocketAddr;
use tokio::time::{timeout, Duration};
use ipnetwork::IpNetwork;
use std::sync::Arc;
use tokio::sync::Semaphore;
use std::time::Instant;

#[tokio::main]
async fn main() {
    let args: Vec<String> = std::env::args().collect();

    if args.len() < 2 {
        eprintln!("usage: subnetrust <subnet> [port]");
        eprintln!("example: subnetrust 192.168.1.0/24 80");
        std::process::exit(1);
    }

    let subnet: IpNetwork = args[1].parse().unwrap_or_else(|_| {
        eprintln!("invalid subnet: {}", args[1]);
        std::process::exit(1);
    });
    
    let port: u16 = if args.len() >= 3 {
        args[2].parse().unwrap_or_else(|_| {
            eprintln!("invalid port: {}", args[2]);
            std::process::exit(1);
        })
    } else {
        80
    };

    let sem = Arc::new(Semaphore::new(1000));
    let mut tasks = vec![];

    println!("scanning subnet: {} port: {}", subnet, port);
    let start = Instant::now();

    for ip in subnet.iter() {
        let sem = sem.clone();
        let ip = ip.to_string();
        tasks.push(tokio::spawn(async move {
            scan_port(&ip, port, sem).await;
        }));
    }

    for task in tasks {
        task.await.unwrap();
    }

    let elapsed = start.elapsed();
    println!("scan complete in {:.2}s", elapsed.as_secs_f64());
}

async fn scan_port(ip: &str, port: u16, sem: Arc<Semaphore>) {
    let _permit = sem.acquire().await.unwrap();
    let addr: SocketAddr = format!("{}:{}", ip, port).parse().unwrap();

    match timeout(Duration::from_millis(500), TcpStream::connect(addr)).await {
        Ok(Ok(_stream)) => println!("{}:{} is open", ip, port),
        Ok(Err(_)) => {}
        Err(_) => {}
    }
}