from icmplib import traceroute as icmp_traceroute

def traceroute(target, privileged=False):
    try:
        hops = icmp_traceroute(target, count=2, interval=0.05, timeout=2)
       
        if not hops:
            print("[!] no hops found")
            return
            
        print(f"{'hop':<5} {'ip':<20} {'avg rtt':<15} {'alive'}")
        print("-" * 50)
        
        for hop in hops:
            print(f"{hop.distance:<5} {hop.address:<20} {hop.avg_rtt:<15} {hop.is_alive}")
            
    except KeyboardInterrupt:
        print("[!] traceroute interrupted by user")
