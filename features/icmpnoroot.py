from icmplib import ping
import socket
import time

def tcp_check(host, port=80, timeout=2):
    try:
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        start = time.time()
        s.connect((host, port))
        rtt = (time.time() - start) * 1000 
        s.close()
        return True, round(rtt, 2)
    except (socket.timeout, socket.error):
        return False, 0.0

def icmp_ping_noroot(target, count=4):
    try:
        result = ping(target, count=count, interval=0.5, timeout=2, privileged=False)

        if result.is_alive:
            print(f"host:            {result.address}")
            print(f"packets sent:    {result.packets_sent}")
            print(f"packets recv:    {result.packets_received}")
            print(f"packet loss:     {result.packet_loss * 100:.1f}%")
            print(f"min rtt:         {result.min_rtt} ms")
            print(f"avg rtt:         {result.avg_rtt} ms")
            print(f"max rtt:         {result.max_rtt} ms")
            print(f"alive:           True")
        else:
            print(f"[!] ICMP failed, trying TCP fallback...\n")
            rtts = []
            sent = count
            received = 0

            for i in range(count):
                alive, rtt = tcp_check(target)
                if alive:
                    rtts.append(rtt)
                    received += 1
                    print(f"  [{i+1}] {target} rtt={rtt}ms")
                else:
                    print(f"  [{i+1}] {target} timeout")

            loss = ((sent - received) / sent) * 100
            avg_rtt = round(sum(rtts) / len(rtts), 2) if rtts else 0.0
            min_rtt = min(rtts) if rtts else 0.0
            max_rtt = max(rtts) if rtts else 0.0

            print(f"\nhost:            {target}")
            print(f"packets sent:    {sent}")
            print(f"packets recv:    {received}")
            print(f"packet loss:     {loss:.1f}%")
            print(f"min rtt:         {min_rtt} ms")
            print(f"avg rtt:         {avg_rtt} ms")
            print(f"max rtt:         {max_rtt} ms")
            print(f"alive:           {'True' if received > 0 else 'False'} (via TCP)")

    except KeyboardInterrupt:
        print("\n[!] ping interrupted by user")