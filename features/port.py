import asyncio
import threading
import sys

print_lock = threading.Lock()

TOP_50_PORTS = [
    21, 22, 23, 25, 53, 80, 110, 111, 135, 139,
    143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080,
    8443, 8888, 27017, 6379, 5432, 1433, 1521, 2049, 2181, 5000,
    5001, 5601, 6443, 7001, 7080, 7443, 8000, 8001, 8009, 8161,
    8181, 9000, 9090, 9200, 9300, 9418, 9999, 10000, 11211, 61616
]

def safe_print(msg):
    with print_lock:
        print(msg, flush=True)

async def scan_port(target, port, semaphore):
    async with semaphore:
        try:
            conn = asyncio.open_connection(target, port)
            reader, writer = await asyncio.wait_for(conn, timeout=2.0)
            safe_print(f"Port {port} is open")
            writer.close()
            await writer.wait_closed()
        except (asyncio.TimeoutError, ConnectionRefusedError, OSError):
            pass

async def scan_range(target, ports):
    semaphore = asyncio.Semaphore(100)
    tasks = [scan_port(target, p, semaphore) for p in ports]
    await asyncio.gather(*tasks)

def thread_worker(target, ports):
    asyncio.run(scan_range(target, ports))

def start_scan(target):
    print(f"Scanning target: {target}")
    
    threads = []
    for port in TOP_50_PORTS:
        t = threading.Thread(target=thread_worker, args=(target, [port]))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\nScan complete.")