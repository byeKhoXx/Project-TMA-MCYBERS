from scapy.all import *
from scapy.layers.http import HTTP, HTTPRequest, TCP_client


LOCAL_IP = "10.0.2.4"
REMOTE_IP = "10.0.2.5"

def handle_packet(packet):
    if packet[IP].dst == LOCAL_IP and packet[IP].src == REMOTE_IP:
        packet_raw = raw(packet)
        print("NEW PACKET!")
        print(packet_raw)

sniff(iface='eth1', prn=handle_packet, filter="ip")