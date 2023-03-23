## Mikrotik

### Active VPN Information 

#### Phase 1 Info
- `/ip ipsec active-peers print `

```commandline
returns active peers 
```

#### Phase 2 Info
- `/ ip ipsec installed-sa print `

```commandline
returns active SAs
```


### VPN Configuration 
- `/ip ipsec profile`

```commandline
returns Phase 1 Config 
Diffie Hellman Group  , dpd , encryption , integrity 
```

- `/ip ipsec peer export `

```commandline
returns peer configuration 
IKE Version , IP Addresses 
```

- `/ip ipsec identity export `

- `/ip ipsec policy`
```commandline
show the policy for the IPSEC tunnel with the peers and identities 
```

- `/ip ipsec proposal`
```commandline
Phase 2 config returns encryption , diffie hellman group 
```
### Network Troubleshooting Commands 
#### PING 
- `ping`
#### Traceroute 
- ` /tool traceroute `


### IPSEC Config
`/ip ipsec export `
`/ip ipsec active-peers `

### Firewall Config
`/ip firewall filter print where dst-port~"500"`
`/ip firewall filter print where dst-port~"4500"`
`/ip firewall address-list print where address~"GW_IP"`
`/ip firewall address-list print where address~"VPN_IP"`
`/ip firewall filter print where src-address~"GW_IP"`
`/ip firewall filter print where src-address~"VPN_IP"`
`/ip firewall filter print where dst-address~"GW_IP"`
`/ip firewall filter print where dst-address~"VPN_IP"`

` /ip ipsec policy print` 
`/ip ipsec proposal print` - IKE Proposals
`/ip ipsec profile print ` - IPSEC Profile

### System Information 
`/system resource print ` - RouterOS Version 
`/system license print ` - Licensing Info 
####
### Session Tracking 
`/ip firewall connection tracking print `
