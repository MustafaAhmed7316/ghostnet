import argparse
import sys

parser = argparse.ArgumentParser(
prog="ghostnet",
description="ghostnet is an advance port scanning tool",
epilog="made by snitch")

def arguments():
    parser.add_argument('-p', '--ping', type=str, help='usage: python core.py -p ip/url')
    parser.add_argument('-tr', '--traceroute', type=str, help='usage: python core.py -tr ip/url')
    
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
        
    args = parser.parse_args()
    return args