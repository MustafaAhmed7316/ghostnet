import subprocess
import os

def subnet_scan(target, port=None):
    binary = os.path.expanduser('subnetscanner/subnetrust/target/release/subnetrust')
    cmd = [binary, target]
    if port:
        cmd.append(str(port))
    subprocess.run(cmd)
