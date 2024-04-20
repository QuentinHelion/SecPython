from scapy.all import *

def icmp(ip):
    icmp = IP(dst=ip)/ICMP()
    response = sr1(icmp, timeout=1, verbose=False)
    if response:
        return True  # If response received
    else:
        return False  # If no response received
