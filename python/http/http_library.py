#!/usr/bin/python3

import logging
import requests

class HTTPLibrary:

	OPTIONS="https://uk.finance.yahoo.com/quote/ACCO/options?p="
	HOLDERS="https://uk.finance.yahoo.com/quote/ACCO/holders?p="
	FINANCIALS="https://uk.finance.yahoo.com/quote/ACCO/financials?p="

	def __init__(self, URL, symbol):
		self.logger		=	logging.getLogger('HTTPLibrary')
		self.url		=	URL+symbol
		self.request	=	None
		self.logger.info("GET: %s", self.url)


	def __del__(self):
		pass

	def request (self):
		self.requests = requests.get(self.url)
