### System Information 
`/system resource print ` - RouterOS Version 
`/system license print ` - Licensing Info 
####
### Session Tracking 
`/ip firewall connection tracking print `

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
