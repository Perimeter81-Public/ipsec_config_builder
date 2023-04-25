# Louis DeVictoria
# Script to build the variables file

import click
import yaml
from scripts.render import render_cfg
import time
import ipaddress

ipsec_params = {}

# Function to validate IP Address
def isip(ctx, param, address):
    try:
        if ipaddress.ip_address(address).is_global:
            return address
        elif ipaddress.ip_address(address).is_private:
            return address
        else:
            raise click.BadParameter("IP Must be Public")
    except ValueError:
        raise click.BadParameter("Re-enter IPv4 Address ex 1.1.1.1 ")

def tunnelip(ctx, param, address):
    tun_space = ipaddress.ip_network("169.254.0.0/16")
    try:
        if ipaddress.ip_address(address).is_private and ipaddress.ip_address(address) in list(tun_space.hosts()):
            return address
        else:
            raise click.BadParameter("Tunnel IPs must be in 169.254.0.0/16 Space")
    except ValueError:
        raise click.BadParameter("Tunnel IPs must be in 169.254.0.0/16 Space")

#Function to validate ip prefix
def isnet(ctx, param , prefix):
    try:
        if ipaddress.IPv4Network(prefix) != True:
            return prefix
        else:
            raise click.BadParameter(f"Enter a valid subnet ex 10.0.0.0/24 {prefix}")
    except ValueError:
        raise click.BadParameter("Enter a valid subnet ex 10.0.0.0/24 ")

def passcheck(ctx, param , password):
    pw = str(password)
    result = pw.isalnum() and len(pw) < 63
    try:
        if result is True:
            return password
    except ValueError:
        raise click.BadParameter("Password can contain only alphanumeric characters , between 0 - 64 characters or start with 0.")

@click.group()
def cli():
    # Collection VPN Details from User input
    pass

@click.command("Get VPN Details")
@click.option("--vendor", prompt=True, type=click.Choice(['cisco' , 'paloalto' , 'fortinet' , 'mikrotik'], case_sensitive=False,))
@click.option("--prem_ip", prompt="Premise IP Address", callback=isip, help="Public IP Client Side.")
@click.option("--prem_net", prompt="Premise Subnet", callback=isnet, type=str )
@click.option("--p81_gw", prompt="VPN Name", default="Perimeter81", help="Name for the IKE GW.")
@click.option("--p81_ip", prompt="Gateway IP", callback=isip, help="P81 Gateway IP.")
@click.option("--p81_net", prompt="P81 Subnet", default="10.255.0.0/16", callback=isnet, type=str )
@click.option("--psk", prompt="Preshare Key", callback=passcheck, confirmation_prompt=True )
@click.option("--encry",prompt=True, default="aes256", type=click.Choice(["3des", "blowfish128", "blowfish192", "blowfish256", "aes128", "aes192", "aes256"],  case_sensitive=False,))
@click.option("--integ",prompt=True, default="sha256", type=click.Choice(['md5', 'sha1', 'sha256', 'sha384'], case_sensitive=False, ))
@click.option("--dhg",prompt=True, default="14", type=click.Choice(['2','5','14','19','20','21'], case_sensitive=False, ))
@click.option("--ph1_life", prompt="Phase 1 Lifetime",default=8, required=True, type=int)
@click.option("--ph2_life", prompt="Phase 2 Lifetime",default=1, required=True, type=int)
@click.option("--dpd", prompt="Dead Peer Timer: ",default=10, required=True, type=int)
@click.option("--bgp", prompt="HA Tunnel True or False: ",default=False, required=False, type=bool)
@click.option("--p81_asn", prompt="P81 BGP ASN: ",default=65000, required=False, type=int)
@click.option("--p81_bgp_ip", prompt="P81 Tunnel IP: ",default="169.254.1.1", callback=tunnelip)
@click.option("--prem_asn", prompt="P81 BGP ASN: ",default=65100, required=False, type=int)
@click.option("--prem_bgp_ip", prompt="Premise Tunnel IP: ",default="169.254.1.2", callback=tunnelip)
def collect(vendor,prem_ip,prem_net,p81_gw,p81_ip,p81_net,psk,encry,integ,dhg,ph1_life,ph2_life,dpd,bgp,p81_asn,p81_bgp_ip,prem_asn,prem_bgp_ip):
    ipsec_params['vendor'] = vendor
    ipsec_params['prem_ip'] = prem_ip
    ipsec_params['prem_net'] = prem_net
    ipsec_params['p81_gw'] = p81_gw
    ipsec_params['p81_ip'] = p81_ip
    ipsec_params['p81_net'] = p81_net
    ipsec_params['psk'] = psk
    ipsec_params['encry'] = encry
    ipsec_params['integ'] = integ
    ipsec_params['dhg'] = dhg
    ipsec_params['ph1_life'] = ph1_life
    ipsec_params['ph2_life'] = ph2_life
    ipsec_params['dpd'] = dpd
    ipsec_params['bgp'] = bgp
    ipsec_params['p81_asn'] = p81_asn
    ipsec_params['p81_bgp_ip'] = p81_bgp_ip
    ipsec_params['prem_asn'] = prem_asn
    ipsec_params['prem_bgp_ip'] = prem_bgp_ip
    print(ipsec_params)
    with open(f'../devices_vars/{vendor}.yml',"w+") as file:
        yaml.dump(ipsec_params,file,sort_keys=False)
        file.close()
    time.sleep(5)
    render_cfg(vendor)
    return ipsec_params


if __name__ == '__main__':
    collect()
