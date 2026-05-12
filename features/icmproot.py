from icmplib import ping

def icmp_ping(target):
    try:
        result = ping(target, count=4, interval=0.5, timeout=2, privileged=True)
        print(f"host:            {result.address}")
        print(f"packets sent:    {result.packets_sent}")
        print(f"packets recv:    {result.packets_received}")
        print(f"packet loss:     {result.packet_loss * 100:.1f}%")
        print(f"avg rtt:         {result.avg_rtt} ms")
        print(f"alive:           {result.is_alive}")
    except KeyboardInterrupt:
        print("\n[!] ping interrupted by user")
    except PermissionError:
        print("[!] root required. try running with sudo")
