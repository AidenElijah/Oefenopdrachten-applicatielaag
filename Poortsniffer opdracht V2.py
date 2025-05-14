import socket

def scan_port(ip, port):
    """Probeert een poort te openen op een opgegeven IP-adres."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)  
        result = s.connect_ex((ip, port)) 
        return result == 0

def scan_ports(ip, port_range=(1, 1024)):
    """Scant een reeks poorten op een opgegeven IP-adres."""
    open_ports = []
    print(f"Scannen van {ip} op poorten {port_range[0]}-{port_range[1]}...")
    
    for port in range(port_range[0], port_range[1] + 1):
        if scan_port(ip, port):
            open_ports.append(port)
            print(f"[OPEN] Poort {port} is open")
    
    if not open_ports:
        print("Geen open poorten gevonden.")
    return open_ports

if __name__ == "__main__":
    target_ip = input("Voer het IP-adres in om te scannen: ")
    start_port = int(input("Voer het startpoortnummer in: "))
    end_port = int(input("Voer het eindpoortnummer in: "))
    
    open_ports = scan_ports(target_ip, (start_port, end_port))
    print("\nScan voltooid. Open poorten:", open_ports)