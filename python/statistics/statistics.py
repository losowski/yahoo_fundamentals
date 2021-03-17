# Key Statistics

import logging
from python.http import http_library

class Statistics (http_library.HTTPLibrary):

	URL = "https://uk.finance.yahoo.com/quote/{sym}/key-statistics?p={sym}"

	def __init__(self, symbol):
		super(Statistics, self).__init__(self.URL, symbol)
		self.logger		=	logging.getLogger('Statistics')

	def __del__(self):
		pass

	# def request()
	def parse(self):
		self.logger.debug("%s", self.req.text)
		data = self.req.text.replace('><', '>\n<')
		#self.logger.info("DATA %s", data)

