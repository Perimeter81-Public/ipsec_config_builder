sysctl -w net.ipv4.ip_forward=1
sysctl -w net.ipv6.conf.all.forwarding=1
sysctl -w net.ipv4.conf.all.accept_redirects=0
sysctl -w net.ipv4.conf.all.send_redirects=0


sudo apt update
sudo apt install strongswan

# Path: vendor_templates/strongswan/ss_ipsec.conf

# Update Firewall
iptables -A INPUT -p udp -m multiport --dports 500,4500 -j ACCEPT
iptables-save > /etc/iptables/rules.v4
