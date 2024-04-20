from scapy.all import *

def tcp(ip, ports):
    results = {}
    for port in ports:
        src_port = RandShort()
        response = sr1(IP(dst=ip)/TCP(sport=src_port, dport=port, flags="S"), timeout=1, verbose=0)
        if response:
            if response.haslayer(TCP):
                if response[TCP].flags == 18:  # Check if SYN-ACK received
                    results[port] = "Open"
                elif response[TCP].flags == 20:  # Check if RST-ACK received
                    results[port] = "Closed"
            elif response.haslayer(ICMP):
                if int(response[ICMP].type) == 3 and int(response[ICMP].code) in [1, 2, 3, 9, 10, 13]:
                    results[port] = "Filtered"
        else:
            results[port] = "Unfiltered or Filtered"
    return results