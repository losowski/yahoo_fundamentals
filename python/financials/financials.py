# Financials

import logging

from python.common import yahoo

"""
"""


class Financials (yahoo.Yahoo):

	URL = "https://uk.finance.yahoo.com/quote/{sym}/financials?p={sym}"

	jsonMAP = { \
				# DEMO
				"demo"			: """context.dispatcher.stores.QuoteSummaryStore.financialData""",
			}

	def __init__(self, symbol):
		super(Financials, self).__init__(self.URL, symbol)
		self.logger		=	logging.getLogger('Financials')

	def __del__(self):
		super(Financials, self).__del__()

	#debug
	def debug(self):
		self.debug_print("demo")

