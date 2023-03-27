# Louis DeVictoria
# Script to build the variables file

import click
import yaml
from render import render_cfg
import time
import subprocess

ipsec_params = {}

@click.group()
def cli():
    pass

@click.command()
@click.option("--vendor", prompt=True, type=click.Choice(['cisco' , 'paloalto' , 'fortinet' , 'mikrotik'], case_sensitive=False,))
@click.option("--prem_ip", prompt="Premise IP Address", help="The person to greet.")
@click.option("--prem_net", prompt="Premise Subnet", help="The person to greet.")
@click.option("--p81_gw", prompt="VPN Name", help="The person to greet.")
@click.option("--p81_ip", prompt="Gateway IP", help="The person to greet.")
@click.option("--p81_net", prompt="P81 Subnet", help="The person to greet.")
@click.option("--psk", prompt="Preshare Key", help="The person to greet.")
@click.option("--encry",prompt=True, type=click.Choice(["3des", "blowfish128", "blowfish192", "blowfish256", "aes128", "aes192", "aes256"], case_sensitive=False, ))
@click.option("--integ",prompt=True, type=click.Choice(['md5', 'sha1', 'sha256', 'sha384'], case_sensitive=False, ))
@click.option("--dhg",prompt=True, type=click.Choice(['2','5','14','19','20','21'], case_sensitive=False, ))
@click.option("--ph1_life", prompt="Phase 1 Lifetime", required=True, type=int)
@click.option("--ph2_life", prompt="Phase 2 Lifetime", required=True, type=int)
@click.option("--dpd", prompt="Dead Peer Timer: ", required=True, type=int)
def collect(vendor,prem_ip,prem_net,p81_gw,p81_ip,p81_net,psk,encry,integ,dhg,ph1_life,ph2_life,dpd):
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
    print(ipsec_params)
    with open(f'./devices_vars/{vendor}.yml',"w+") as file:
        yaml.dump(ipsec_params,file,sort_keys=False)
        file.close()
    time.sleep(5)
    render_cfg(vendor)
    return ipsec_params








if __name__ == '__main__':
    collect()
