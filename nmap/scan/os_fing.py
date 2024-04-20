from scapy.all import *

def os_fing(ip):
    ans, _ = sr(IP(dst=ip)/TCP(dport=80, flags="S"), timeout=2, verbose=False)
    if ans:
        ttl = ans[0][1].ttl
        if ttl <= 64:
            return "Linux/Unix"
        elif ttl <= 128:
            return "Windows"
        else:
            return "Unknown"
    else:
        return "Unknown"