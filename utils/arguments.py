import argparse

parser = argparse.ArgumentParser(
prog="ghostnet",
description="ghostnet is an advance port scanning tool",
epilog="made by snitch")

def arguments():
    parser.add_argument('-p', '--ping')
    args = parser.parse_args()
    return args