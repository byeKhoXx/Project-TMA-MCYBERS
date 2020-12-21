# TMA-MCYBERS

## Install
In order to get the system up and running, 3 VMs, a NatNetwork and an internalNetwork are needed:
  * **DNS**: has the ip 10.0.2.15 in the NatNetwork
  * **Webserver**: has the ip 10.0.2.4 in the NatNetwork and has the ip 10.0.5.4 in the internalNetwork
  * **Proxy**: has the ip 10.0.2.6 in the NatNetwork andhas the ip 10.0.5.6 in the internalNetwork
Also, all the machines need to have the 10.0.2.15 as the first option for DNS. These is changes by 
editing the file `/etc/resolv.conf`.

### Webserver
First of all, install apache2 as a demo webserver by running:
```
sudo apt install apache2
```

Then the needed components by running:

```
sudo pip3 install scapy schedule
```

The custom components run by the weserver are the killswitch and the packet forwarder. Both components can be found under the webserver folder.
In order to enable the client opertion, open two terminals. In the first one run:

```
sudo python3 forward_packets.py
```

And on the second one:

```
./killswitch.sh
```

The `forward_packets.py` module will send sampled traffic from an specific client to the webserver. In a production scenario, all the traffic should be forwarded
but for demosntration purposes we are only sending the traffic from a given client.

The `killswitch.sh` module will stop the public interface of the WebServer as soon as it receives a connection through the internal network. This ensures that,
even in the worst load possible, if the server is capable of just creating the connection, it will kill the public interface.

### DNS
The DynDNS has been developed by using the [MiniDynDNS](https://github.com/arkanis/minidyndns) by arkanis. In order
to create the service, fisrt make sure that the system has ruby installed. Then clone the project by running:
```
git clone https://github.com/arkanis/minidyndns.git
``` 

and place the `db.yml` and `config.yml` alonside the `dns.rb` file. These files will create the following fqdns:
	* acme.tmaco.local for the webserver
	* dns.tmaco.local for the DNS
	* proxy.tmaco.local for the proxy

In order to run the DNS, execute:
```
sudo ruby dns.rb
```

### Proxy
In order to create the proxy, first of all you will need a python3 virtual envirioment. In order to install
the tool to generate it, run:
```
sudo apt install python3-venv
```

and then create one by running:

```
python3 -m venv venv
```

In order to activate it, run:

```
source venv/bin/activate
```

Now, inside the virtual enviroment, install the `proxy.py` module by running:

```
pip install proxy.py
```

In order to install all the crafted plugins for this module, copy the file inside the directory `proxy/configs` named 
`web_server_route.py` inside the virtual enviroment directory `venv/lib/python3.7/site-packages/proxy/plugin` thus
replacing the original files.

In order to execute the proxy, the user needs to have priviledges to use port 80. One simple *but very insecure way*
to do it is to run it as root. In order to switch just run `sudo su`. Finally, reativate the venv and run the
`start.sh` script inside the proxy folder.

Now we need to activate the controller part of the system. In order to do so, install the following packages on the same 
machine that the proxy runs but not in the venv:

```
sudo pip3 install scapy schedule requests
```

The run:

```
sudo python3 receive_packets.py
```

And enter `webserver` as the client name. It has been previously set-up in the demo db with the correct IP for
the webserver.
 
# Configuration
All the before mentioned files include definition style variables that can include paths and tunnable parameteres,
please read the documentation in those files to find out more on how to configure the whole system.
 