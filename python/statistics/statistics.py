# Key Statistics

import logging

from python.common import yahoo

"""
-- Valuation measures
-**- Financial Highlights
-- Profitability
'profitMargins': {'raw': 0.03746, 'fmt': '3.75%'},
+ Operating margin (financialData.operatingMargins)
'grossMargins': {'raw': 0.29543, 'fmt': '29.54%'},

-- Management effectiveness (last year)
'returnOnAssets': {'raw': 0.026700001, 'fmt': '2.67%'},
'returnOnEquity': {'raw': 0.08177, 'fmt': '8.18%'},


-- Income statement (last year)
-- Balance Sheet (last quarter)
'totalCash': {'raw': 36600000, 'fmt': '36.6M', 'longFmt': '36,600,000'},
'totalCashPerShare': {'raw': 0.385, 'fmt': '0.38'},
'totalDebt': {'raw': 1230200064, 'fmt': '1.23B', 'longFmt': '1,230,200,064'},
'debtToEquity': {'raw': 165.639, 'fmt': '165.64'},
'currentRatio': {'raw': 1.308, 'fmt': '1.31'},
defaultKeyStatistics.'bookValue': {'raw': 7.823, 'fmt': '7.82'},


-- Cash flow statement (last year)
'operatingCashflow': {'raw': 119200000, 'fmt': '119.2M', 'longFmt': '119,200,000'},
'freeCashflow': {'raw': 128587504, 'fmt': '128.59M', 'longFmt': '128,587,504'},


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
				##-**- Financial Highlights
				# -- Profitability
				"profitMargins"				: """context.dispatcher.stores.QuoteSummaryStore.defaultKeyStatistics.'profitMargins'.fmt""",
				"operatingMargins"			: """context.dispatcher.stores.QuoteSummaryStore.financialData.'operatingMargins'.fmt""",

				#-- Management effectiveness (last year)
				"returnOnAssets"			: """context.dispatcher.stores.QuoteSummaryStore.financialData.'returnOnAssets'.fmt""",
				"returnOnEquity"			: """context.dispatcher.stores.QuoteSummaryStore.financialData.'returnOnEquity'.fmt""",

				#-- Income statement (last year)
				#-- Balance Sheet (last quarter)
				"totalCash"					: """context.dispatcher.stores.QuoteSummaryStore.financialData.'totalCash'.fmt""",
				"totalCashPerShare"			: """context.dispatcher.stores.QuoteSummaryStore.financialData.'totalCashPerShare'.fmt""",
				"totalDebt"					: """context.dispatcher.stores.QuoteSummaryStore.financialData.'totalDebt'.fmt""",
				"debtToEquity"				: """context.dispatcher.stores.QuoteSummaryStore.financialData.'debtToEquity'.fmt""",
				"currentRatio"				: """context.dispatcher.stores.QuoteSummaryStore.financialData.'currentRatio'.fmt""",
				"bookValue"					: """context.dispatcher.stores.QuoteSummaryStore.defaultKeyStatistics.'bookValue'.fmt""",

				#-- Cash flow statement (last year)
				"operatingCashflow"			: """context.dispatcher.stores.QuoteSummaryStore.financialData.'operatingCashflow'.fmt""",
				"freeCashflow"				: """context.dispatcher.stores.QuoteSummaryStore.financialData.'freeCashflow'.fmt""",

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
				#"demo"			: """context.dispatcher.stores.QuoteSummaryStore.defaultKeyStatistics""",
				"demo"			: """context.dispatcher.stores.QuoteSummaryStore.financialData""",
				#"demo"			: """context.dispatcher.stores.QuoteSummaryStore.summaryDetail""",
			}

	def __init__(self, symbol):
		super(Statistics, self).__init__(self.URL, symbol)
		self.logger		=	logging.getLogger('Statistics')

	def __del__(self):
		super(Statistics, self).__del__()

	#debug
	def debug(self):
		self.debug_print("demo")
		#-- Valuation measures
		# -**- Financial Highlights
		# -- Profitability
		self.debug_print("profitMargins")
		self.debug_print("operatingMargins")

		#-- Management effectiveness (last year)
		self.debug_print("returnOnAssets")
		self.debug_print("returnOnEquity")

		#-- Income statement (last year)

		#-- Balance Sheet (last quarter)
		self.debug_print("totalCash")
		self.debug_print("totalCashPerShare")
		self.debug_print("totalDebt")
		self.debug_print("debtToEquity")
		self.debug_print("currentRatio")

		#-- Cash flow statement (last year)
		self.debug_print("operatingCashflow")
		self.debug_print("freeCashflow")

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

