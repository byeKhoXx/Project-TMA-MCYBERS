import requests
from time import sleep
from random import randrange

def switch_fqdn(name, IP):
    tries = 1
    print(f"Attempting DNS record change for {name} to {IP}...")
    response=requests.get(f'http://10.0.2.15/?myip={IP}', auth=(name, name))
    while(response.status_code != 200):
        tries += 1
        sleep(randrange(100, 1000)/1000)
        response=requests.get(f'http://10.0.2.15/?myip={IP}', auth=(name, name))
        if(tries == 15 and response.status_code != 200):
            return response.status_code

    print(f"DNS record successfully changed in {tries} tries!")
    return response.status_code

if __name__ == '__main__':
    print(switch_fqdn('acme', '10.0.2.6'))
