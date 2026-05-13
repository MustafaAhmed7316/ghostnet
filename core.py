import os
import asyncio
from utils.arguments import arguments
from features.icmproot import icmp_ping
from features.icmpnoroot import icmp_ping_noroot
from features.traceroute import traceroute
from features.resolve import resolve
from features.port import start_scan
from features.subnet import subnet_scan

args = arguments()
target = args.ping
trtarget = args.traceroute
rstarget = args.resolve
portscan = args.port
subnetscan = args.subnet

isRoot = os.geteuid() == 0

if not any([target, trtarget, rstarget, portscan, subnetscan]):
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

    if portscan:
        start_scan(portscan)

    if subnetscan:
        if len(subnetscan) == 2:
            subnet_scan(subnetscan[0], subnetscan[1])
        else:
            subnet_scan(subnetscan[0])
