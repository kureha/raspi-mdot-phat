#!/usr/bin/python
# -*- coding: utf-8 -*-

import netifaces

# IP Address Getting Module
class IpModule:
	# Constas
	ignore_ip_list = ["127.0.0.1"]

	# Constructor
	def __init__(self):
		# Instance variables
		self.if_list = netifaces.interfaces()

		# Property Settings
		self.error_string = "stand by"

	# Is retval is error?
	def is_success(self, result):
		if result == [ self.error_string ]:
			return False
		else:
			return True

	# Get IP Address Function
	def get_ip_addr(self):
		# Return Value
		ip_list = []

		# Refresh if list
		self.if_list = netifaces.interfaces()

		# Loop netif list
		for if_name in self.if_list:
			# Check 1 : is netif connected?
			if netifaces.ifaddresses(if_name).get(netifaces.AF_INET) is None:
				continue

			# Get IP info list
			for v in netifaces.ifaddresses(if_name).get(netifaces.AF_INET):	
				# Skip ignore list
				if v["addr"] in self.ignore_ip_list:
					continue

				# if all check passed, add IP to return list
				ip_list.append(v["addr"])

		if len(ip_list) == 0:
			ip_list.append(self.error_string)

		return ip_list

# Endpoint - TestLogic
if __name__ == "__main__":
	ip_module = GetIpAddr()
	print(" / ".join(ip_module.get_ip_addr()))

