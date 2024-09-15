import socket
import os

def run_server():
    port = 54321
    save_path = os.path.expanduser("~/Desktop")  # Save files to Desktop by default
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', port))
        s.listen()
        print(f"Listening on port {port}...")
        
        while True:
            conn, addr = s.accept()
            with conn:
                file_name = conn.recv(1024).decode()
                file_path = os.path.join(save_path, file_name)
                
                with open(file_path, 'wb') as f:
                    while True:
                        chunk = conn.recv(1024)
                        if not chunk:
                            break
                        f.write(chunk)
                print(f"File received and saved to {file_path}")

if __name__ == "__main__":
    run_server()
