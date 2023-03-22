Configuration Samples for Perimeter81 Internal to various other vendor devices 
# ipsec config builder
This is a configuration repository to help build ipsec & bgp configuration for common firewall & device platforms 
and some basic commands to troubleshoot issues.

The configuration is for route based VPN solutions 

### vendor_templates 
is the directory of all the vendors. each subdirectory refernces 
the platform and contains one file to build a base ipsec tunnel with generic firewall permission. There is
a second file for bgp configuration for multi-site tunnels
- mikrotik 
- palo alto
- fortinet 
- cisco

### device_vars
Sample Variable directory that contains the specific variables to each build 
along with the refernces in the jinja2 build 

There is unique variable constraints so please make sure you review the chart 
for vendor to ensure you are complaint to produce functional config.


### sample_config
This is the rendered output when the jinja2 and the yaml files are composed to produce function 
configuration per platform

### vendor_cmds
This is a directory of troubleshooting & informational gathering commands 

