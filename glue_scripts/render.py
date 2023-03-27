#Louis DeVictoria
#Python Script to load the dictionary file and jinja2 template to create a configuration
import sys

from jinja2 import Environment, FileSystemLoader, StrictUndefined
#Local Directory
file_loader = FileSystemLoader('')
#Load Environment
env = Environment(loader=file_loader)
import yaml
template = env.get_template('/vendor_templates/cisco/iosxe_17/iosxe.j2')

def render_cfg(file):
    with open(f'./devices_vars/{file}') as info2:
        device_dict = yaml.load(info2, Loader=yaml.FullLoader)
        #Opens the host device dictionary and pulls the values
        hostname = (device_dict['hostname'])
        #This will take the hostfile file variables and run through the jinja2 file and output a yaml file
        leaf_config = template.render(device_dict, undefined=StrictUndefined)
        #Create the leaf yaml file
        leaf_file = hostname+".yml"
        print(leaf_file)

    with open("./sample_config/"+leaf_file, 'w+') as leafcfg:
        leafcfg.write(leaf_config)
        leafcfg.close()

    #Print the output
        print(leaf_config)

if __name__ == '__main__':
    file = sys.argv[1]
    render_cfg(file)
