## Variables Chart 

### Palo 
| Variable | Description                              | Type      | Options                                                                     |
|----------|------------------------------------------| --------- |-----------------------------------------------------------------------------|
| phase1   | IKE Profile                              | String    | AlphaNumeric Characters                                                     |
| phase2   | IPSEC Profile                            | String    | AlphaNumeric Characters                                                     |
| p81_gw   | IKE Gateway Peer                         | String    | ex: 192.168.1.1                                                             |
| psk      | Prershare Key                            | String    | alphanumeric characters 0 - 64 and can not start with 0                     |
| p81_net  | Subnet assigned to P81 VPN               | IP Subnet | ex: 10.130.0.0 255.255.0.0                                                  |
| prem_net | Subnet the client has on their equipment | IP Subnet | ex: 172.17.100.0 255.255.255.0                                              |
| ike_ver  | Which protocol version                   | INT       | 1 or 2                                                                      |
| encry    | The cipher suite to use                  | List      | aes-256-gcm, aes-256-cbc, aes-192-cbc, aes-128-gcm,  aes-128-cbc, 3des, des |
| integ    | Authentication Hash                      | List      | sha512, sha384, sha256, sha1, md5                                           |
| dhg      | Diffie Hellman                           | List      | group1, group2, group5, group14, group19, or group20                        |
| ph1_life | Lifetime of Phase 1 Tunnel               | Integer   | Time in Hours                                                               |
| ph2_life | Lifetime of Phase 2 Tunnel               | Integer   | Time in Hours                                                               |
| dpd      | Dead Peer Detection                      | Integer   | Time in Seconds                                                                              |

### Mikrotik 
| Variable | Description                              | Type      | Options                                                                                                         |
|----------|------------------------------------------|-----------|-----------------------------------------------------------------------------------------------------------------|
| phase1   | IKE Profile                              | String    | AlphaNumeric Characters                                                                                         |
| phase2   | IPSEC Profile                            | String    | AlphaNumeric Characters                                                                                         |
| p81_gw   | IKE Gateway Peer                         | String    | ex: 192.168.1.1                                                                                                 |
| psk      | Prershare Key                            | String    | alphanumeric characters 0 - 64 and can not start with 0                                                                    |
| p81_net  | Subnet assigned to P81 VPN               | IP Subnet | ex: 10.130.0.0 255.255.0.0                                                        |
| prem_net | Subnet the client has on their equipment | IP Subnet | ex: 172.17.100.0 255.255.255.0                                                        |
| ike_ver  | Which protocol version                   | INT       | 1 or 2                                                                                                          |
| encry    | The cipher suite to use                  | List      | 3des , aes , aes256 , blowfish                                                                                  |
| integ    | Authentication Hash                      | List      | aes256 , sha1                                                                                                   |
| dhg      | Diffie Hellman Group                     | List      | ec2n155  ec2n185  ecp256  ecp384  ecp521  modp768  modp1024  modp1536  modp2048  modp3072  modp4096  modp6144  modp8192 |
| ph1_life | Lifetime of Phase 1 Tunnel               | Integer   | Time in Hours                                                                                                   |
| ph2_life | Lifetime of Phase 2 Tunnel               | Integer   | Time in Hours                                                                                                   |
| dpd      | Dead Peer Detection                      | Integer   | Time in Seconds                                                                                                 |

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
| encry    | The cipher suite to use                 | List               | 3des, blowfish128 192 256 , aes128 192 256       |
| integ    | Authentication Hash                     | List               | md5 , sha1 , sha256 , sha384           |
| dhg      | Diffie Hellman Group                    | List               | 2,5,14,19,20,21          |
| ph1_life |                                         | Integer            | Time in Hours                                           |
| ph2_life |                                         | Integer            | Time in Hours                                           |
| dpd      |                                         | Integer            | Number 1-60                                             |

### Cisco
| Variable | Description                           | Type      | Options                                                    |
|----------| ------------------------------------- | --------- |------------------------------------------------------------|
| phase1   | IKE Profile                           | String    | AlphaNumeric Characters                                    |
| phase2   | IPSEC Profile                         | String    | AlphaNumeric Characters                                    |
| p81_gw   | IKE Gateway Peer                      | String    | Name , IKEv2 , Intfs , IPs , PSK , NAT-T                   |
| psk      | Prershare Key                         | String    | Shared Secret Between the IPSEC peers                      |
| p81_net  | Subnet assigned to P81 VPN            | IP Subnet | Policy Based example 10.255.0.0/16 / Route based 0.0.0.0/0 |
| prem_net | Subnet the client has on their equipment | IP Subnet | Policy Based example 10.0.0.0/16 / Route based 0.0.0.0/0   |
| ike_ver  | Which protocol version                | INT       | 2                                                          |
| encry    | The cipher suite to use               | List      | 3des, blowfish128 192 256 , aes128 192 256                 |
| integ    | Authentication Hash                   | List      | md5 , sha1 , sha256 , sha384                               |
| dhg      |                                       | List      | 2,5,14,19,20,21                                            |
| ph1_life |                                       |           |                                                            |
| ph2_life |                                       |           |                                                            |
| dpd      |                                       |           |                                                            |
