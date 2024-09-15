import tkinter as tk
from tkinter import filedialog, messagebox
import socket
import threading
import os

def discover_server():
    discovery_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    discovery_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    discovery_socket.settimeout(5)  # Set timeout for blocking operations
    discovery_socket.bind(('', 12345))

    discovery_socket.sendto(b"DISCOVER_SERVER", ('<broadcast>', 12345))
    print("Discovery message sent")

    try:
        while True:
            message, server_address = discovery_socket.recvfrom(1024)
            if message:
                server_info = message.decode()
                server_ip = server_info.split()[2]
                if server_ip not in discovered_servers:
                    discovered_servers.append(server_ip)
                    update_server_list()
    except socket.timeout:
        print("Discovery timeout")
    finally:
        discovery_socket.close()

def update_server_list():
    server_listbox.delete(0, tk.END)
    for server in discovered_servers:
        server_listbox.insert(tk.END, server)

def send_file(file_path, server_ip):
    port = 54321
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((server_ip, port))
            file_name = os.path.basename(file_path)
            s.sendall(file_name.encode())
            with open(file_path, 'rb') as f:
                while chunk := f.read(1024):
                    s.sendall(chunk)
        messagebox.showinfo("Success", "File sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send file:\n{e}")

def select_file():
    file_path = filedialog.askopenfilename(title="Select a file to send")
    if file_path:
        selected_server = server_listbox.get(tk.ACTIVE)
        if selected_server:
            send_file(file_path, selected_server)
        else:
            messagebox.showerror("Error", "No server selected.")
    else:
        messagebox.showinfo("Info", "No file selected.")

def create_gui():
    global server_listbox
    global discovered_servers

    discovered_servers = []

    root = tk.Tk()
    root.title("File Transfer")
    root.geometry("400x300")

    tk.Label(root, text="Discovered Servers:", pady=10).pack()

    server_listbox = tk.Listbox(root, width=50, height=10)
    server_listbox.pack(pady=10)

    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    refresh_button = tk.Button(button_frame, text="Refresh Servers", command=lambda: discovered_servers.clear() or discover_server())
    refresh_button.pack(side=tk.LEFT, padx=5)

    select_button = tk.Button(button_frame, text="Select File", command=select_file)
    select_button.pack(side=tk.LEFT, padx=5)

    threading.Thread(target=discover_server, daemon=True).start()

    root.mainloop()

if __name__ == "__main__":
    create_gui()
