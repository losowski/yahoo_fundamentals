# Key Statistics

import logging
import json

from python.common import yahoo

class Statistics (yahoo.Yahoo):

	URL = "https://uk.finance.yahoo.com/quote/{sym}/key-statistics?p={sym}"

	jsonMAP = {"52WeekChange":"context.dispatcher.stores.QuoteSummaryStore.defaultKeyStatistics.52WeekChange.raw",
			}

	def __init__(self, symbol):
		super(Statistics, self).__init__(self.URL, symbol)
		self.logger		=	logging.getLogger('Statistics')

	def __del__(self):
		super(Statistics, self).__del__()

	#debug
	def debug(self):
		print ("{0}".format(self.get("52WeekChange")))
