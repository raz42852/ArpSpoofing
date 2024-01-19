import os

def check_ping(ip):
    # Send ping request to ip and return True if connected else False
    res = os.system("ping -n 1 " + ip)
    if res == 0:
        return True
    return False

def scan_network(network_prefix):
    # The func get network perfix and scan all of the network if connected and return list with active ips
    active_ips = []
    for num in range(1, 256):
        ip = "{}.{}".format(network_prefix, num)
        if check_ping(ip) == True:
            active_ips.append(ip)
    return active_ips