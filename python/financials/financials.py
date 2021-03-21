# Financials

import logging

from python.common import yahoo

"""
"""


class Financials (yahoo.Yahoo):

	URL = "https://uk.finance.yahoo.com/quote/{sym}/financials?p={sym}"

	jsonMAP = { \
				# Quarterly - Income Statement
				#"revenue" ??
				"costOfRevenue"	:	"""context.dispatcher.stores.QuoteSummaryStore.'incomeStatementHistoryQuarterly'.'incomeStatementHistory'[*].costOfRevenue.raw""",
				# Quarterly - Balance Sheet
				# Quarterly - Cash Flow
				# DEMO
				"demo"			: """context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistoryQuarterly.incomeStatementHistory""",
				#"demo"			: """context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistoryQuarterly.balanceSheetHistoryQuarterly""",
				#"demo"			: """context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistoryQuarterly.cashflowStatementHistoryQuarterly""",
			}

	def __init__(self, symbol):
		super(Financials, self).__init__(self.URL, symbol)
		self.logger		=	logging.getLogger('Financials')

	def __del__(self):
		super(Financials, self).__del__()

	#debug
	def debug(self):
		#Demo
		self.debug_print("demo")
		# Quarterly - Income Statement
		#self.debug_print("revenue")
		self.debug_print("costOfRevenue")

