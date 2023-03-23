## Cisco IOS-XE

### Active VPN Information 
#### Phase 1 Info 

- show crypto ikev2 session 
- show crypto ikev2 sa 

```
Tunnel ID - Local & Remote 
Port - 4500
Encyrption 
Authentication
Lifetime - 
Child SA - should routes 
```

```sample output 
Tunnel-id Local                 Remote                fvrf/ivrf            Status 
2         172.31.92.132/4500    131.226.32.161/4500   none/none            READY  
      Encr: AES-CBC, keysize: 256, PRF: SHA384, Hash: SHA384, DH Grp:14, Auth sign: PSK, Auth verify: PSK
      Life/Active Time: 86400/836 sec
Child sa: local selector  0.0.0.0/0 - 255.255.255.255/65535
          remote selector 0.0.0.0/0 - 255.255.255.255/65535
          ESP spi in/out: 0x84766B73/0xCBF0C989 
```

#### Phase 2 Info 
show crypto ipsec sa
show crypto ipsec sa | i peer|Status|conn id|caps|transform

```
Run command with the "|" will filter for imporant info 
Peer: Perimeter81 Public IP 
Status: Active 
Port - 500 /4500 NAT-T 
conn id - There needs to be two 
encaps -- traffic to P81 
decaps -- traffic from P81 
 
```

```commandline
ios-xe#show crypto ipsec sa | i peer|Status|conn id|caps|transform  
   current_peer 131.226.32.161 port 4500
    #pkts encaps: 0, #pkts encrypt: 0, #pkts digest: 0
    #pkts decaps: 0, #pkts decrypt: 0, #pkts verify: 0
        transform: esp-aes esp-sha-hmac ,
        in use settings ={Tunnel UDP-Encaps, }
        conn id: 2003, flow_id: CSR:3, sibling_flags FFFFFFFF80000048, crypto map: Tunnel101-head-0
        Status: ACTIVE(ACTIVE)
        transform: esp-aes esp-sha-hmac ,
        in use settings ={Tunnel UDP-Encaps, }
        conn id: 2004, flow_id: CSR:4, sibling_flags FFFFFFFF80000048, crypto map: Tunnel101-head-0
        Status: ACTIVE(ACTIVE)
```

- show crypto ipsec profile 


### VPN Configuration 
- show run | s ikev2

```commandline
Returns all configuration relative to ikev2 
```

- show run | s ipsec
```commandline
Returns all configuration relative to ipsec
```

### VPN Debugging  
**DANGER USING THESE COMMANDS CAN CAUSE PERFORMANCE ISSUES ONLY USE IF YOU KNOW WHAT YOU ARE DOING**
- debug crypto ikev2 

- debug crypto ipsec

### Network Troubleshooting Commands
#### Ping
ping 10.130.0.1
#### Traceroute
traceroute 10.130.0.1
```commandline

```
