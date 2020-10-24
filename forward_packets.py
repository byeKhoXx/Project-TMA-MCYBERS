import os
os.sys.path.append('/home/ismael/.local/lib/python3.8/site-packages')# Needed to be executed as root, change the path for the path where scapy is located in your machine 

from scapy.all import send, Raw, sniff, sendp
from scapy.layers.inet import IP, TCP
import sys
#send(IP(dst="10.0.2.5")/TCP(dport=80)/Raw(load="Hola Mundo"), count=5)



iface = "eth1"
filter = "ip"
REMOTE_IP = "10.0.2.4" #IP of our VPS
LOCAL_IP = "10.0.2.5" #IP of our client
SENDER_IP = "10.0.2.6" #IP of the customer of our client

def handle_packet(packet):
    

    #packet[IP].src = MY_IP
    if packet[IP].dst == LOCAL_IP and packet[IP].src == SENDER_IP:

        packet[IP].dst = REMOTE_IP
        del(packet[IP].chksum)
        packet.show2()
        print(packet[IP].src)
        print(packet[IP].dst)
        send(packet)
        print("Packet redirected!")



sniff(prn=handle_packet, filter=filter, iface=iface, store=0)

