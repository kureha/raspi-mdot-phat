#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import netifaces
from microdotphat import write_string, scroll, clear, show, fill

# *** DEFINES START ***
# Target Interface
interface = "wlan0"
# Time Interval(sec)
#scroll_sleep = 0.05
scroll_sleep = 1
# Prefix String(space * 6 is default)
prefix = "      "
# Suffix String
suffix = ""
# Kerning
kerning_flag = False
# Scroll X Setting(0[=1] is default, 8 is ONE MATRIX BLOCK)
#scroll_x = 0
scroll_x = 8
# Scroll Y Setting
scroll_y = 0
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
    # Get IP Address
    ip_module = GetIpAddr(interface)
    ip_addr = ip_module.get_ip_addr()

    # Reset all matrix
    clear()

    # Write to matrix buffer
    print_value = prefix + ip_addr + suffix
    write_string(print_value, kerning=kerning_flag)

    # Refresh IP Counter
    refresh_counter = 0
    refresh_timing = len(print_value)

    try:
        # Main loop
        while True:
            # Scroll
            scroll(scroll_x, scroll_y)
            # Render
            show()
            # Countup refresh
            refresh_counter = refresh_counter + 1

            # Refresh logic
            if refresh_counter == refresh_timing:
                # Re-Get IP Address
                ip_addr = ip_module.get_ip_addr()

                # Reset all matrix
                clear()

                # Create print value
                print_value = prefix + ip_addr + suffix
                write_string(print_value, kerning=kerning_flag)

                # Reset refresh counter
                refresh_counter = 0
                refresh_timing = len(print_value)

            # Sleep
            time.sleep(scroll_sleep)
    except KeyboardInterrupt:
        # SIGINT or Ctrl + C
        # Reset all matrix
        clear()
        show()

# Endpoint
try:
    main()
except Exception as e:
    print(str(e))
    exit(1)

