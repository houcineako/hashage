import socket

def scan_ports(target_ip, ports=[21, 22, 23, 80, 443]):
    open_ports = []
    print(f"Scanning ports on {target_ip}...")

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout de 1 seconde

        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port} is open")
            open_ports.append(port)
        else:
            print(f"Port {port} is closed")
        sock.close()    
    return open_ports
# Exemple d'utilisation
target_ip = "192.168.1.1"
open_ports = scan_ports(target_ip)
print(f"Open ports: {open_ports}")