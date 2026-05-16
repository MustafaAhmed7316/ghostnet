import os
from utils.arguments import arguments
from features.icmproot import icmp_ping
from features.icmpnoroot import icmp_ping_noroot
from features.traceroute import traceroute
from features.resolve import resolve
from features.port import start_scan
from features.subnet import subnet_scan
from features.banner import banner

args = arguments()
target = args.ping
trtarget = args.traceroute
rstarget = args.resolve
portscan = args.port
subnetscan = args.subnet
subnetport = args.sport
bannergrab = args.banner

isRoot = os.geteuid() == 0

if not any([target, trtarget, rstarget, portscan, subnetscan, bannergrab]):
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
        subnet_scan(subnetscan, subnetport)

    if bannergrab:
        banner(bannergrab)