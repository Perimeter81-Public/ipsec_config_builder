## Fortinet

### Get all VPN Information
diagnose vpn tunnel list 

### Get IPSEC Phase 1 info
get vpn ike gateway
get vpn ipsec tunnel details

### Get IPSEC Phase 2 info
diagnose vpn ipsec status 

### Network Troubleshooting Commands 
#### Ping  
execute ping <ip>
#### Traceroute
execute traceroute <ip>
#### Packet Sniffer 
diagnose sniffer packet any
diagnose sniffer packet any "not host <ip>"
diagnose sniffer packet port1 'udp port <port_number>'

### Get Device Configuration 
show full-configuration
