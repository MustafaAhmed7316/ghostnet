import subprocess
import re

def banner(ip):
    result = subprocess.run(
        ['ping', '-c', '1', '-W', '1', ip],
        capture_output=True,
        text=True
    )
    match = re.search(r'ttl=(\d+)', result.stdout, re.IGNORECASE)
    if match:
        ttl = int(match.group(1))
        if ttl <= 64:
            print(f"{ip} is linux/unix")
        elif ttl <= 128:
            print(f"{ip} is windows")
        elif ttl <= 255:
            print(f"{ip} is networking gear")
    else:
        print(f"{ip} is unreachable")