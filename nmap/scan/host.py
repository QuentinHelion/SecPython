from scapy.all import *
from .os_fing  import *
from .icmp import *
from .tcp import *

def host(ip):
    print(f"Scanning host: {ip}")
    ping_result = icmp(ip)
    print(f"ICMP Ping: {'Reachable' if ping_result else 'Unreachable'}")

    if ping_result:
        ports_to_scan = range(1, 1025)  # Scan common ports from 1 to 1024
        port_scan_result = tcp(ip, ports_to_scan)
        print("Port Scan Results:")
        for port, status in port_scan_result.items():
            print(f"\tPort {port}: {status}")

        os = os_fing(ip)
        print(f"Operating System: {os}")