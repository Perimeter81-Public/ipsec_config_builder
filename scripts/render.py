#Louis DeVictoria
#Python Script to load the dictionary file and jinja2 template to create a configuration
import sys
import os
from jinja2 import Environment, FileSystemLoader, StrictUndefined, ChoiceLoader
#Local Directory
file_loader = FileSystemLoader('.')
#Load Environment
env = Environment(loader=file_loader)
import yaml



def load_templ(vendor):
    os.chdir('./vendor_templates/')
    if vendor == 'cisco':
        file = ('cisco/cisco.j2')
        template = env.get_template(file)
        return template
    elif vendor == 'fortinet':
        file = ('fortinet/fortios.j2')
        template = env.get_template(file)
        return template
    elif vendor == 'paloalto':
        file = ('paloalto/panos.j2')
        template = env.get_template(file)
        return template
    elif vendor == 'mikrotik':
        file = ('mikrotik/routeros.j2')
        template = env.get_template(file)
        return template
    else:
        file = ('cisco/cisco.j2')
        template = env.get_template(file)
        return template

def render_cfg(vendor):
    template = load_templ(vendor)
    with open(f'../devices_vars/{vendor}.yml') as info2:
        device_dict = yaml.load(info2, Loader=yaml.FullLoader)
        #This will take the hostfile file variables and run through the jinja2 file and output a yaml file
        vendor_config = template.render(device_dict, undefined=StrictUndefined)
        #Create the config file
        vendor_file = vendor+".yml"
        print(vendor_file)

    with open("../sample_config/"+vendor_file, 'w+') as ipseccfg:
        ipseccfg.write(vendor_config)
        ipseccfg.close()

    #Print the output
        print(vendor_config)

if __name__ == '__main__':
    print(os.getcwd())
    vendor = sys.argv[1]
    render_cfg(vendor)
