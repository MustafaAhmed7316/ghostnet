from utils.arguments import arguments
from features.icmproot import icmp_ping

args = arguments()
target = args.ping

if target:
    print(f"pinging {target}...\n")
    icmp_ping(target)
else:
    print("no target found")