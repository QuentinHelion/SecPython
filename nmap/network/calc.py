import ipaddress

def calc(ip, mask):
    ip_network = ipaddress.ip_network(f"{ip}/{mask}",strict=False)
    return [str(ip) for ip in ip_network] 
    