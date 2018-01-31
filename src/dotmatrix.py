#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from microdotphat import write_string, scroll, clear, show

# Pimonori pHat DotMatrix Class
class DotMatrix:
	# All clear
	@staticmethod
	def clear():
		clear()
		show()

	# Write string and scrolling to last
	@staticmethod
	def render_string(s, scroll_x = 8, scroll_y = 0, scroll_sleep = 1, kerning_flag = False):
		# init view
		clear()

		# render string
		write_string(s, kerning = kerning_flag)
		show()
		time.sleep(scroll_sleep)

		# render to end
		for i in range(len(s)):
			# scroll -> render
			scroll(scroll_x, scroll_y)
			show()
			time.sleep(scroll_sleep)

		

# Endpoint - TestLogic
if __name__ == "__main__":
	DotMatrix.init()
	DotMatrix.render_string("  rendering test")

