# Key Statistics

import logging
from python.common import yahoo

class Statistics (yahoo.Yahoo):

	URL = "https://uk.finance.yahoo.com/quote/{sym}/key-statistics?p={sym}"

	def __init__(self, symbol):
		super(Statistics, self).__init__(self.URL, symbol)
		self.logger		=	logging.getLogger('Statistics')

	def __del__(self):
		super(Statistics, self).__del__()

