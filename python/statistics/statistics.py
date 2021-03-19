# Key Statistics

import logging

from python.common import yahoo

"""
-- Valuation measures
-- Profitability
'profitMargins': {'raw': 0.03746, 'fmt': '3.75%'},
+ Operating margin (financialData.operatingMargins)

-- Management effectiveness (last year)
-- Income statement (last year)
-- Balance Sheet (last quarter)
-- Cash flow statement (last year)

-- Share statistics
'sharesOutstanding': {'raw': 94496800, 'fmt': '94.5M', 'longFmt': '94,496,800'},
'floatShares': {'raw': 91625226, 'fmt': '91.63M', 'longFmt': '91,625,226'},
'heldPercentInsiders': {'raw': 0.028719999, 'fmt': '2.87%'},
'heldPercentInstitutions': {'raw': 0.94201, 'fmt': '94.20%'},
'sharesShort': {'raw': 2830005, 'fmt': '2.83M', 'longFmt': '2,830,005'},

'shortRatio': {'raw': 5.69, 'fmt': '5.69'},
'shortPercentOfFloat': {'raw': 0.0307, 'fmt': '3.07%'},
'sharesPercentSharesOut': {'raw': 0.0298, 'fmt': '2.98%'},
'sharesShortPriorMonth': {'raw': 3801824, 'fmt': '3.8M', 'longFmt': '3,801,824'},
"""


class Statistics (yahoo.Yahoo):

	URL = "https://uk.finance.yahoo.com/quote/{sym}/key-statistics?p={sym}"

	jsonMAP = { \
				#-- Valuation measures
				# -- Profitability
				"profitMargins"				: """context.dispatcher.stores.QuoteSummaryStore.defaultKeyStatistics.'profitMargins'.fmt""",
				"operatingMargins"			: """context.dispatcher.stores.QuoteSummaryStore.financialData.'operatingMargins'.fmt""",

				#-- Management effectiveness (last year)
				#-- Income statement (last year)
				#-- Balance Sheet (last quarter)
				#-- Cash flow statement (last year)
				# -- Share statistics
				"sharesOutstanding"			: """context.dispatcher.stores.QuoteSummaryStore.defaultKeyStatistics.'sharesOutstanding'.fmt""",
				"floatShares"				: """context.dispatcher.stores.QuoteSummaryStore.defaultKeyStatistics.'floatShares'.fmt""",
				"heldPercentInsiders"		: """context.dispatcher.stores.QuoteSummaryStore.defaultKeyStatistics.'heldPercentInsiders'.fmt""",
				"heldPercentInstitutions"	: """context.dispatcher.stores.QuoteSummaryStore.defaultKeyStatistics.'heldPercentInstitutions'.fmt""",
				"sharesShort"				: """context.dispatcher.stores.QuoteSummaryStore.defaultKeyStatistics.'sharesShort'.fmt""",

				"shortRatio"				: """context.dispatcher.stores.QuoteSummaryStore.defaultKeyStatistics.'shortRatio'.fmt""",
				"shortPercentOfFloat"		: """context.dispatcher.stores.QuoteSummaryStore.defaultKeyStatistics.'shortPercentOfFloat'.fmt""",
				"sharesPercentSharesOut"	: """context.dispatcher.stores.QuoteSummaryStore.defaultKeyStatistics.'sharesPercentSharesOut'.fmt""",
				"sharesShortPriorMonth"		: """context.dispatcher.stores.QuoteSummaryStore.defaultKeyStatistics.'sharesShortPriorMonth'.fmt""",
				# DEMO
				"demo"			: """context.dispatcher.stores.QuoteSummaryStore.financialData""",
			}

	def __init__(self, symbol):
		super(Statistics, self).__init__(self.URL, symbol)
		self.logger		=	logging.getLogger('Statistics')

	def __del__(self):
		super(Statistics, self).__del__()

	#debug
	def debug(self):
		self.debug_print("demo")
		# -- Share statistics
		self.debug_print("sharesOutstanding")
		self.debug_print("floatShares")
		self.debug_print("heldPercentInsiders")
		self.debug_print("heldPercentInstitutions")
		self.debug_print("sharesShort")

		self.debug_print("shortRatio")
		self.debug_print("shortPercentOfFloat")
		self.debug_print("sharesPercentSharesOut")
		self.debug_print("sharesShortPriorMonth")


		# -- Profitability
		self.debug_print("profitMargins")
		self.debug_print("operatingMargins")
		#-- Valuation measures
		#-- Management effectiveness (last year)
		#-- Income statement (last year)
		#-- Balance Sheet (last quarter)
		#-- Cash flow statement (last year)
