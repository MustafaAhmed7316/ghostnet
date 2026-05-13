import argparse
import sys

parser = argparse.ArgumentParser(
prog="ghostnet",
description="ghostnet is an advance port scanning tool",
epilog="made by snitch")

def arguments():
    parser.add_argument('-p', '--ping', type=str, help='usage: python core.py -p ip/url')
    parser.add_argument('-tr', '--traceroute', type=str, help='usage: python core.py -tr ip/url')
    
    parser.add_argument('-rs', '--resolve', type=str, help='usage: python core.py -rs <domain>, do not add https://')
    
    parser.add_argument('-pt', '--port', type=str, help='usage: python core.py -p ')
    
    parser.add_argument('-sn', '--subnet', type=str, help='usage: python core.py -sn 192.168.1.0/24 80')
    
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
        
    args = parser.parse_args()
    return args
