#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import netifaces
from dotmatrix import DotMatrix

# *** DEFINES START ***
# Target Interface
interface = "wlan0"
# Prefix String(space * 6 is default)
prefix = "      "
# Suffix String
suffix = ""
# *** DEFINES END ***

# IP Address Getting Module
class GetIpAddr:
	# Constructor
	def __init__(self, if_name):
		# Properties
		self.if_name = if_name

		# Property Settings
		self.retry_limit = 0
		self.retry_interval = 3
		self.error_string = "stand by"

	# Is retval is error?
	def is_success(self, result):
		if result == self.error_string:
			return False
		else:
			return True

	# Get IP Address Function
	def get_ip_addr(self):
		# Return Value
		ip_addr = ""
		# Loo-Try Counter
		retry_count = 0

		while True:
			try:
				# Get IP using netifaces
				ip_addr = netifaces.ifaddresses(self.if_name).get(netifaces.AF_INET)[0]["addr"]
				break
			except Exception as e:
				# Countup
				retry_count = retry_count + 1
				# Exceeded limit -> break
				if retry_count > self.retry_limit:
					ip_addr = self.error_string
					break
				# Wait interval
				time.sleep(self.retry_interval)

		# Return result
		return ip_addr

def main():
	# Create IP module
	ip_module = GetIpAddr(interface)

	# Loop
	while True:
		# Get IP Address
		ip_addr = ip_module.get_ip_addr()

		# Write to matrix buffer
		print_value = prefix + ip_addr + suffix
		DotMatrix.render_string(print_value)

# Endpoint
if __name__ == "__main__":
	try:
		main()
	except Exception as e:
		print(str(e))
		exit(1)

