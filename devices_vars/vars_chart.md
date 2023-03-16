## Variables Chart 

### Palo 
| Variable | Description                           | Type      | Options                                                   |
|----------| ------------------------------------- | --------- |-----------------------------------------------------------|
| phase1   | IKE Profile                           | String    | AlphaNumeric Characters                                   |
| phase2   | IPSEC Profile                         | String    | AlphaNumeric Characters                                                          |
| p81_gw   | IKE Gateway Peer                      | String    | Name , IKEv2 , Intfs , IPs , PSK , NAT-T                  |
| psk      | Prershare Key                         | String    | Shared Secret Between the IPSEC peers                     |
| p81_net  | Subnet assigned to P81 VPN            | IP Subnet | Policy Based example 10.255.0.0/16 / Route based 0.0.0.0/0 |
| prem_net | Subnet the client has on their equipment | IP Subnet | Policy Based example 10.0.0.0/16 / Route based 0.0.0.0/0  |
| ike_ver  | Which protocol version                | INT       | 1 or 2                                                    |
| encry    | The cipher suite to use               | List      | 3des , aes , aes256 , blowfish                            |
| integ    | Authentication Hash                   | List      | aes256 , sha1                                             |
| dhg      |                                       | List      | 2,5,14,19,20,21                                           |
| ph1_life |                                       |           |                                                           |
| ph2_life |                                       |           |                                                           |
| dpd      |                                       |           |                                                           |

### Mikrotik 
| Variable | Description                           | Type      | Options                                                   |
|----------| ------------------------------------- | --------- |-----------------------------------------------------------|
| phase1   | IKE Profile                           | String    | AlphaNumeric Characters                                   |
| phase2   | IPSEC Profile                         | String    | AlphaNumeric Characters                                                          |
| p81_gw   | IKE Gateway Peer                      | String    | Name , IKEv2 , Intfs , IPs , PSK , NAT-T                  |
| psk      | Prershare Key                         | String    | Shared Secret Between the IPSEC peers                     |
| p81_net  | Subnet assigned to P81 VPN            | IP Subnet | Policy Based example 10.255.0.0/16 / Route based 0.0.0.0/0 |
| prem_net | Subnet the client has on their equipment | IP Subnet | Policy Based example 10.0.0.0/16 / Route based 0.0.0.0/0  |
| ike_ver  | Which protocol version                | INT       | 1 or 2                                                    |
| encry    | The cipher suite to use               | List      | 3des , aes , aes256 , blowfish                            |
| integ    | Authentication Hash                   | List      | aes256 , sha1                                             |
| dhg      |                                       | List      | 2,5,14,19,20,21                                           |
| ph1_life |                                       |           |                                                           |
| ph2_life |                                       |           |                                                           |
| dpd      |                                       |           |                                                           |

### Fortinet 
| Variable | Description                             | Type               | Options                                                 |
|----------|-----------------------------------------|--------------------|---------------------------------------------------------|
| phase1   | IKE Profile                             | String             | AlphaNumeric Characters                                 |
| phase2   | IPSEC Profile                           | String             | AlphaNumeric Characters                                 |
| p81_gw   | IKE Gateway Peer                        | IPv4 Address       | ex: 192.168.1.1                                         |
| psk      | Prershare Key                           | String             | alphanumeric characters 0 - 64 and can not start with 0 |
| p81_net  | Subnet assigned to P81 VPN              | IPv4 Subnet + Mask | ex: 10.130.0.0 255.255.0.0                              |
| prem_net | Subnet the client has on their equipment | IP Subnet + Mask   | ex: 172.17.100.0 255.255.255.0                          |
| ike_ver  | Which protocol version                  | INT                | 1 or 2                                                  |
| encry    | The cipher suite to use                 | List               | 3des aes128,192,256 aria128,192,256  chacha20poly1305   |
| integ    | Authentication Hash                     | List               | md5 , sha1,256,384,512 , prfsha1,256,384,512            |
| dhg      | Diffie Hellman Group                    | List               | 1,2,5,14,15,16,17,18,19,20,21,27,28,29,30,21,32         |
| ph1_life |                                         | Integer            | Time in Hours                                           |
| ph2_life |                                         | Integer            | Time in Hours                                           |
| dpd      |                                         | Integer            | Number 1-60                                             |

### Cisco
| Variable | Description                           | Type      | Options                                                   |
|----------| ------------------------------------- | --------- |-----------------------------------------------------------|
| phase1   | IKE Profile                           | String    | AlphaNumeric Characters                                   |
| phase2   | IPSEC Profile                         | String    | AlphaNumeric Characters                                                          |
| p81_gw   | IKE Gateway Peer                      | String    | Name , IKEv2 , Intfs , IPs , PSK , NAT-T                  |
| psk      | Prershare Key                         | String    | Shared Secret Between the IPSEC peers                     |
| p81_net  | Subnet assigned to P81 VPN            | IP Subnet | Policy Based example 10.255.0.0/16 / Route based 0.0.0.0/0 |
| prem_net | Subnet the client has on their equipment | IP Subnet | Policy Based example 10.0.0.0/16 / Route based 0.0.0.0/0  |
| ike_ver  | Which protocol version                | INT       | 1 or 2                                                    |
| encry    | The cipher suite to use               | List      | 3des , aes , aes256 , blowfish                            |
| integ    | Authentication Hash                   | List      | aes256 , sha1                                             |
| dhg      |                                       | List      | 2,5,14,19,20,21                                           |
| ph1_life |                                       |           |                                                           |
| ph2_life |                                       |           |                                                           |
| dpd      |                                       |           |                                                           |
