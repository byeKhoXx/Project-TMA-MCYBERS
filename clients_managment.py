from datetime import date,timedelta
from db_model.db_connection import db_connection
from db_model.client import Client
from db_model.packet import Packet

def add_new_client(name, ip):
    db = db_connection()
    client = Client.get_client_by_name(name, db)
    if client is None:
        client = Client(name, ip)
        Client.insert_db(client, db)
    db.close_connection()

def get_client_by_name(name):
    db = db_connection()
    result = Client.get_client_by_name(name, db)
    db.close_connection()
    return result
    
def add_new_packet(client,date,time_slot,packet_count):
    db = db_connection()
    package = Packet(date,time_slot,packet_count ,client.id)
    Packet.insert_db(package,db)
    db.close_connection()

def get_mean_for_last(client,time_slot,num_of_days = 10):
    db = db_connection()
    days_before = date.today() - timedelta(days=num_of_days)
    packets = Packet.get_packets_after(client,days_before,db)
    db.close_connection()
    packet_count_sum = sum(p.packet_count for p in packets)
    result = packet_count_sum / len(packets)
    return result

# Test code

# Insert client
client_name = "demo_name"
client_ip =   "demo_ip"
add_new_client(client_name, client_ip)

# Insert package
packet_date = date.today()
packet_time_slot = 5
packet_count = 10
client = get_client_by_name(client_name)
add_new_packet(client,packet_date,packet_time_slot,packet_count)


# Get mean for x number of days perios
mean_value = get_mean_for_last(client,packet_time_slot)






