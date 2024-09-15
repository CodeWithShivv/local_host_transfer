import socket

def discover():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.bind(('', 12345))
    
    while True:
        message, address = sock.recvfrom(1024)
        if message == b"DISCOVER_SERVER":
            response = f"Server at {socket.gethostbyname(socket.gethostname())}:{54321}"
            sock.sendto(response.encode(), address)

if __name__ == "__main__":
    discover()
