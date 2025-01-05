from modules.port_scanner import scan_ports
from modules.brute_forcer import brute_force_ssh
from modules.directory_scanner import scan_directories
from modules.network_sniffer import start_sniffing
from modules.vulnerability_scanner import scan_sql_injection
from modules.dos_flooder import flood
from utils.logger import logger

def main():
    print("Select a module:")
    print("1. Port Scanner")
    print("2. Brute Forcer")
    print("3. Directory Scanner")
    print("4. Network Sniffer")
    print("5. Vulnerability Scanner")
    print("6. DoS Flooder")
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        target = input("Enter the target IP: ")
        ports = list(map(int, input("Enter ports to scan (comma separated): ").split(',')))
        open_ports = scan_ports(target, ports)
        print(f"Open ports: {open_ports}")
    elif choice == "2":
        target = input("Enter the target IP: ")
        username = input("Enter username: ")
        password_list = input("Enter path to password list: ").split(',')
        brute_force_ssh(target, username, password_list)
    elif choice == "3":
        target = input("Enter the target URL: ")
        directories = input("Enter directories to scan (comma separated): ").split(',')
        scan_directories(target, directories)
    elif choice == "4":
        interface = input("Enter the network interface (e.g., eth0): ")
        start_sniffing(interface)
    elif choice == "5":
        target = input("Enter the target URL: ")
        param = input("Enter parameter to test (e.g., 'id'): ")
        scan_sql_injection(target, param)
    elif choice == "6":
        target = input("Enter the target URL: ")
        thread_count = int(input("Enter number of threads to use: "))
        flood(target, thread_count)
    else:
        print("Invalid choice. Exiting.")
        return

if __name__ == "__main__":
    main()
