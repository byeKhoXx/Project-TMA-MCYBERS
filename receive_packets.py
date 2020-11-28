from scapy.all import *
from scapy.layers.http import HTTP, HTTPRequest, TCP_client
from clients_managment import *
import json
import schedule
import threading
import time


LOCAL_IP = "10.0.2.4"
client = input("Client:")
REMOTE_IP = get_ip_client(client)

global d1 = dict() # Define dictionary 1 [ip_src, number of packets]
global d2 = dict() # Define dictionary 2 [ip_src, number of packets]
global packets # Number of packets recived las 15min

# cron ->sched.scheduler  https://docs.python.org/3/library/sched.html

# DoS detection

def clean_dic():
    seconds = time.time()
    r = (seconds/60) % 2
    global d1
    global d2
    if r == 0:
        for key in d1:
            if d1[key] > 100:
                # Attack using ip = key
        d1 = dict()
    else 
        for key in d2:
            if d2[key] > 100:
                # Attack using ip = key
        d2 = dict()

# DDoS detection

def add_to_ddbb():
"""
    TODO ->
    clients_managements.add_packets(client, day, time slot, packets)
    mean10 = mean_last_10(client, time slot)
"""
    if packets > mean10 *2:
        # DDoS attack
    global packets
    packets=0

def scheduler(): #Scheduler for tasks every X minutes
    schedule.every().minute.do(clean_dic) # Executing "clean_dic()" every minute
    schedule.every(15).minutes.do(add_to_ddbb) # Executing "add_to_ddbb()" eevry 15 minutes
    while 1:
        schedule.run_pending()

def handle_packet(packet):
    if packet[IP].dst == LOCAL_IP and packet[IP].src == REMOTE_IP:
        packet_raw = raw(packet)
        # Add to dictionary 1 and 2 the ip recived
        global d1
        global d2
        if(packet_raw.ip_src in d1):
            d1[packet_raw.ip_src] = d1[packet_raw.ip_src] + 1
        else:
            d1[packet_raw.ip_src] = 1
        if(packet_raw.ip_src in d2):
            d2[packet_raw.ip_src] = d1[packet_raw.ip_src] + 1
        else:
            d2[packet_raw.ip_src] = 1
        global packets
        packets = packets + 1
        print("NEW PACKET!")
        print(packet_raw)

sniff(iface='eth1', prn=handle_packet, filter="ip")

t=threading.Thread(target=scheduler) #Threading the scheduler
#t.daemon = True  # set thread to daemon ('ALGO' won't be printed in this case)
t.start()
