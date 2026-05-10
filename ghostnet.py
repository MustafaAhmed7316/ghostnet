import requests
import argparse
import socket

parser = argparse.ArgumentParser(description="ghostnet")
parser.add_argument("--link", type=str, help="enter the link that you want to scan")
parser.add_argument("--ip", type=int, help="enter the ipv4 that you want to scan")


args = parser.parse_args()

if args.link:
    ip = socket.gethostbyname(args.link)
    print(ip)

