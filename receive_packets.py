from scapy.all import *
from scapy.layers.http import HTTP, HTTPRequest, TCP_client
from clients_managment import *
import json


LOCAL_IP = "10.0.2.4"
client = input("Client:")
REMOTE_IP = get_ip_client(client)

# TODO: Define dictionary 1 [ip_src, number of packets]
# TODO: Define dictionary 2 [ip_src, number of packets]
global packets # Number of packets recived las 15min

# cron ->sched.scheduler  https://docs.python.org/3/library/sched.html

# DoS detection
""" 
TODO: 
cron every 1 min:
    r = number of minute % 2
    if r == 0
        if dictionary 1 have one entry that have a big number of packets ==> Attack in using the ip ot that entry
        clean dictionary 1
    else 
        if dictionary 2 have one entry that have a big number of packets ==> Attack in using the ip ot that entry
        clean dictionary 2
"""

# DDoS detection
"""
TODO:
cron every 15 min
    add_packets(client, day, time slot, number of packets)
    mean10 = mean_last_10(client, time slot)
    if(packets > mean10 *2) ==> atac
    packets=0
"""


def handle_packet(packet):
    if packet[IP].dst == LOCAL_IP and packet[IP].src == REMOTE_IP:
        packet_raw = raw(packet)
        # TODO: add to dictionary 1 and 2 the ip recived (if not exist an entry add with 1, and if exist add 1)
        global packets
        # TODO: packets++
        print("NEW PACKET!")
        print(packet_raw)

sniff(iface='eth1', prn=handle_packet, filter="ip")