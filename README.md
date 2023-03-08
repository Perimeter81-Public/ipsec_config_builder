Configuration Samples for Perimeter81 Internal to various other vendor devices 
# config-snippets

### vendor_templates 
is the directory of all the vendors. each subdirectory refernces 
the platform and contains one file to build a base ipsec tunnel with generic firewall permission. There is
a second file for bgp configuration for multi-site tunnels
- mikrotik 
- palo alto

### device_vars
Sample Variable directory that contains the specific variables to each build 
along with the refernces in the jinja2 build 

### sample_config
This is the rendered output when the jinja2 and the yaml files are composed to produce function 
configuration per platform


