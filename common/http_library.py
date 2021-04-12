#!/usr/bin/python3

import logging
import requests

from common import timestamps

class HTTPLibrary(timestamps.TimeStamp):

	jsonMAP = {}

	OPTIONS="https://uk.finance.yahoo.com/quote/{sym}/options?p={sym}"
	HOLDERS="https://uk.finance.yahoo.com/quote/{sym}/holders?p={sym}"
	FINANCIALS="https://uk.finance.yahoo.com/quote/{sym}/financials?p={sym}"

	def __init__(self, URL, symbol):
		super(HTTPLibrary, self).__init__()
		self.logger		=	logging.getLogger('HTTPLibrary')
		self.url		=	URL.format(sym= symbol)
		self.req	=	None
		self.logger.info("GET: %s", self.url)


	def __del__(self):
		super(HTTPLibrary, self).__del__()

	def request (self):
		self.req = requests.get(self.url)
		self.logger.info("HTTP status: %s", self.req.status_code)

	#debug print
	def debug_print(self, key):
		print ("{0}: {1}".format(key, self.get(key)))

	#debug
	def debug(self):
		for key in self.jsonMAP.keys():
			self.debug_print(key)
