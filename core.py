import os
from utils.arguments import arguments
from features.icmproot import icmp_ping
from features.icmpnoroot import icmp_ping_noroot
from features.traceroute import traceroute

args = arguments()
target = args.ping
trtarget = args.traceroute

isRoot = os.geteuid() == 0


if target:
    print(f"pinging {target}...\n")
    
    if isRoot:
        icmp_ping(target)
    else:
         icmp_ping_noroot(target)
    
if trtarget:
    traceroute(trtarget, privileged=isRoot)
else:
    print("no target found")