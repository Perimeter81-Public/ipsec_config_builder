## Fortinet

### Active VPN Information 

#### Get IPSEC Phase 1 info
diagnose vpn tunnel list 

```commandline
get list of vpn tunnels 
```

```commandline
list all ipsec tunnel in vd 0
------------------------------------------------------
name=Perimeter81 ver=2 serial=1 172.31.29.79:0->131.226.32.161:0 dst_mtu=0
bound_if=3 lgwy=dyn/0 tun=intf/0 mode=auto/1 encap=none/512 options[0200]=frag-rfc  run_state=0 role=primary accept_traffic=1 overlay_id=0

proxyid_num=1 child_num=0 refcnt=12 ilast=42955482 olast=42955482 ad=/0
stat: rxp=0 txp=0 rxb=0 txb=0
dpd: mode=on-idle on=0 idle=30000ms retry=10 count=0 seqno=0
natt: mode=none draft=0 interval=0 remote_port=0
proxyid=Perimeter81 proto=0 sa=0 ref=2 serial=3 auto-negotiate
  src: 0:0.0.0.0/0.0.0.0:0
  dst: 0:0.0.0.0/0.0.0.0:0
run_tally=1
```

#### Phase 2 Info
- get vpn ipsec tunnel details

```commandline 
type: confirm route or policy based 
packets: traffic sent & recieved across the vpn 
mode: confirm ikev2
```

```commandline
gateway
  name: 'Perimeter81'
  type: route-based
  local-gateway: 172.31.29.79:0 (dynamic)
  remote-gateway: 131.226.32.161:0 (static)
  mode: ike-v2
  interface: 'port1' (3)
  rx  packets: 0  bytes: 0  errors: 0
  tx  packets: 0  bytes: 0  errors: 1
  dpd: on-idle/unnegotiated
  selectors
    name: 'Perimeter81'
    auto-negotiate: enable
    mode: tunnel
    src: 0:0.0.0.0/0.0.0.0:0
    dst: 0:0.0.0.0/0.0.0.0:0
```


### VPN Configuration 
``
- show vpn ipsec phase1-interface 

```commandline
show vpn interface config
```

```commandline
config vpn ipsec phase1-interface
    edit "Perimeter81"
        set interface "port1"
        set ike-version 2
        set peertype any
        set net-device disable
        set mode-cfg enable
        set proposal aes256-sha256
        set localid "172.31.29.79"
        set dpd on-idle
        set comments "Phase 1 Config for Perimeter81"
        set dhgrp 14
        set remote-gw 131.226.32.161
        set psksecret ENC +jWIcwBt68GpSHzaBd2g3sQXrvrUcHYwMGcgzT1poI8lR9lfi/DEyiR4DIpNbBTHgEuxo6mot43ZrgPPduA5xTEeRrN9+FTnwhOhU9Z4v30+4racbNTSf4CY82vn3wrudXv0eG1g6QvNBPbwQTX8NcW6u+FUEzWw1YRSN/fJbSc5kBLNJ0fxx+MitfaLC+a36nj4hA==
        set dpd-retrycount 10
        set dpd-retryinterval 30
    next
end
```

- show vpn ipsec phase2 

```commandline
config vpn ipsec phase2-interface
    edit "Perimeter81"
        set phase1name "Perimeter81"
        set proposal aes256-sha256
        set dhgrp 14
        set auto-negotiate enable
        set comments "Phase 2 Config for Perimeter81"
    next
end
```

### VPN Debugging  
**DANGER USING THESE COMMANDS CAN CAUSE PERFORMANCE ISSUES ONLY USE IF YOU KNOW WHAT YOU ARE DOING**

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


