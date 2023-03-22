# Louis DeVictoria
# Script to accept device variables input to create a file to be used in configuration
import sys
import pprint
import yaml
from validation import net_checks

# Present / Gather info from user
# Wrap data into dictionary
# Convert Dictonary to YAML file for vars
# kick off render script

ipsec_params = {}

encrypt_list = ["3des", "blowfish128", "blowfish192", "blowfish256", "aes128", "aes192", "aes256"]
integrity_list = ["md5", "sha1", "sha256", "sha384"]



ipsec_params['vendor'] = input("Enter Vendor: cisco , palo , fortinet , mikrotik: ")
ipsec_params['hostname'] = input("Enter the hostname: ")
ipsec_params['prem_ip'] = input("Enter Premise Public IP: ")
ipsec_params['prem_net'] = input("Enter the Premise Subnet: ")
ipsec_params['p81_gw'] = input("Name of the VPN: ex: Perimeter81: ")
ipsec_params['p81_ip'] = input("Public IP of Gateway: ")
ipsec_params['p81_net'] = input("Enter the P81 VPN Subnet: ")
ipsec_params['psk'] = input("Enter the PreShare Key: ")
ipsec_params['encry'] = input("[3des, blowfish128, blowfish192, blowfish256,aes128,aes192, aes256: ")
ipsec_params['integ'] = input("Select Integrity:  [md5 , sha1 , sha256 , sha384]: ")
ipsec_params['dhg'] = input("Select Diffie-Helllman Group: [2,5,14,19,20,21]: ")
ipsec_params['ph1_life'] = input("Enter the Phase 1 lifetime in hours: ")
ipsec_params['ph2_life'] = input("Enter the Phase 2 lifetime in hours: ")
pprint.pprint(ipsec_params)



hostname = ipsec_params['hostname']
with open(f'{hostname}.yml',"w+") as file:
	yaml.dump(ipsec_params,file,sort_keys=False)
