#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from dotmatrix import DotMatrix
from ipmodule import IpModule

# *** DEFINES START ***
# Join String
join_string = " / "
# Prefix String(space * 6 is default)
prefix = "     "
# Suffix String
suffix = ""
# *** DEFINES END ***

def main():
	# Create IP module
	ip_module = IpModule()

	# Loop
	while True:
		# Get IP Address
		ip_addr = join_string.join(ip_module.get_ip_addr())

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

