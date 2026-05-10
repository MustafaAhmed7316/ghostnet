import argparse
import socket
import threading
from scapy.all import IP, TCP, sr1

parser = argparse.ArgumentParser(description="ghostnet")
parser.add_argument("--link", type=str, help="enter the link that you want to scan")
parser.add_argument("--ip", type=str, help="enter the ipv4 that you want to scan")
args = parser.parse_args()

if args.link:
    ip = socket.gethostbyname(args.link)
elif args.ip:
    ip = args.ip
else:
    print("Error: provide --link or --ip")
    exit(1)

open_ports = []
lock = threading.Lock()  

def scan_port(ip, port):
    packet = IP(dst=ip) / TCP(dport=port, flags="S")
    response = sr1(packet, timeout=0.5, verbose=0)

    if response and response.haslayer(TCP):
        if response[TCP].flags == "SA":
            with lock:
                open_ports.append(port)
                print(f"Port {port} is open")

print(f"Scanning {ip}...\n")

threads = []

for port in range(1, 1025):
    t = threading.Thread(target=scan_port, args=(ip, port))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"\nDone. Open ports: {open_ports}")
