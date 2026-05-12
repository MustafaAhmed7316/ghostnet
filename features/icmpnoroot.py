from icmplib import ping
result = ping("1.1.1.1", privileged=False)

print({result.packets_received})