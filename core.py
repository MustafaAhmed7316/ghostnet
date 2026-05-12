import os
from utils.arguments import arguments
from features.icmproot import icmp_ping
from features.icmpnoroot import icmp_ping_noroot
from features.traceroute import traceroute
from features.resolve import resolve

args = arguments()
target = args.ping
trtarget = args.traceroute
rstarget = args.resolve

isRoot = os.geteuid() == 0

if not any([target, trtarget, rstarget]):
    print("no target found")
else:
    if target:
        print(f"pinging {target}...\n")
        if isRoot:
            icmp_ping(target)
        else:
            icmp_ping_noroot(target)
        
    if trtarget:
        traceroute(trtarget, privileged=isRoot)
        
    if rstarget:
        resolve(rstarget)
