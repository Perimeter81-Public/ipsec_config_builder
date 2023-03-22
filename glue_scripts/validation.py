# Louis DeVictoria
import socket
import json
import ipaddress
from ipwhois import IPWhois
import requests


class net_checks:
	def __init__(self, address):
		self.address = address

	# Check if the address is valid
	def _isIP(self):
		address = self.address
		try:
			#Check if global
			valid_ip = ipaddress.ip_address(address).is_global
			return True
		except:
			return False
	def _isNet(self):
		prefix = self.address
		try:
			valid_net = ipaddress.ip_network(prefix)
			return prefix
		except:
			return False
