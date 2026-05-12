import socket

def resolve(rstarget):
    
    resolved = socket.gethostbyname(rstarget)
    
    print(resolved)