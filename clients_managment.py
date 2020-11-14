# Client Management

"""
TODO: Create the following bds and methods
    BDs
        1.Clients:
            - ID or client name
            - IP client
        2.Packets
            - Day
            - Time slot (every 15min during 24hours of the day)
            - Number of packets
            - Client: Foreign key to Clients table


    Methods:
        1. new_client(name, ip):
            add a new entry to the clients table with the name and ip

        2. get_ip_client(client)
            return the ip of the client

        3. add_packets(client, day, time slot, number of packets):
            adds to the table packets the day, time slot and number of packets and the foreign key with the user.

        4. mean_last_10(client, time slot):
            queries to the packets table the last 10 days in the same time slot and client and returns the mean

"""



