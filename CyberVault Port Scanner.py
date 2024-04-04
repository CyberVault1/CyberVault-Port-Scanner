import socket
import threading
import pyfiglet

def get_local_ip():
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Connect to an external server
        s.connect(("8.8.8.8", 80))
        # Get the local IP address
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception as e:
        print("Error getting local IP address:", str(e))
        return None

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set timeout to 1 second
        result = sock.connect_ex((ip, port))
        if result == 0:
            try:
                service = socket.getservbyport(port)
                print(f"Port {port} ({service}) is open on {ip}")
            except socket.error:
                print(f"Port {port} (Unknown service) is open on {ip}")
        sock.close()
    except Exception as e:
        print(f"Error scanning port {port}: {str(e)}")

def scan_all_ports(ip):
    threads = []
    for port in range(65536):
        t = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

def main():
    while True:
        print(pyfiglet.figlet_format("CyberVault Port Scanner", font='big'))  # Print CyberVault in big letters
        print("Welcome to CyberVault's Port Scanner!")
        print("Select an option:")
        print("1. Start Port Scan")
        print("2. Exit")
        choice = input("Enter your choice (1 or 2):  ")
        
        if choice == '1':
            ip = get_local_ip()
            if ip:
                print(f"Scanning all ports on local network IP: {ip}")
                scan_all_ports(ip)
            else:
                print("Failed to get local IP address. Please check your network connection.")
        elif choice == '2':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
        
        print("\nSelect an option:")
        print("3. Run another scan")
        print("4. Exit")
        next_choice = input("Enter your choice (3 or 4): ")
        if next_choice == '4':
            print("Exiting...")
            break
        elif next_choice != '3':
            print("Invalid choice. Exiting...")
            break

if __name__ == "__main__":
    main()
