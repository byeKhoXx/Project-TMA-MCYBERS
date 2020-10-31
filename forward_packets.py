import os
os.sys.path.append('/home/ismael/.local/lib/python3.8/site-packages')# Needed to be executed as root, change the path for the path where scapy is located in your machine 
from scapy.all import send, Raw, sniff, sendp, socket
from scapy.layers.inet import IP, TCP, in4_chksum
import sys
import json

iface = "eth1"
filter = "ip"
REMOTE_IP = "10.0.2.4" #IP of our VPS
LOCAL_IP = "10.0.2.5" #IP of our client
SENDER_IP = "10.0.2.6" #IP of the customer of our client

def handle_packet(packet):
    
    #*** NEW APPROACH ***
    if packet[IP].dst == LOCAL_IP and packet[IP].src == SENDER_IP:

        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        s_port = packet[TCP].sport
        d_port = packet[TCP].dport
        tcp_flags = str(packet[TCP].flags)
        js = {"ip_src": ip_src, "ip_dst": ip_dst, "s_port": s_port, "d_port": d_port, "tcp_flags" : tcp_flags}

        payload = json.dumps(js)
        print(payload)

        send(IP(dst="10.0.2.4")/TCP(dport=8000)/Raw(load=payload))
        

'''
        #*** OLD APPROACH *** 
        packet[IP].dst = REMOTE_IP
        packet[IP].src = LOCAL_IP
        old_chksum = packet[IP].chksum
        del(packet[IP].chksum)



        packet_raw = raw(packet)
        udp_raw = packet_raw[20:]
        packet[IP].chksum = in4_chksum(socket.IPPROTO_UDP, packet[IP], udp_raw)


        packet[IP].show2()
        new_chksum = packet[IP].chksum
        print("SRC -> " + packet[IP].src + " /DST -> " + packet[IP].dst)
        print("OLD -> " + str(old_chksum) + " /NEW -> " + str(new_chksum))
        send(packet)
        print("Packet redirected!")'''



sniff(prn=handle_packet, filter=filter, iface=iface, store=0)

