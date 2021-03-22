# Financials

import logging

from python.common import yahoo

"""
# Quarterly - Income Statement
	#"Breakdown"
	#"revenue" ??
	'costOfRevenue': {'raw': 271900000, 'fmt': '271.9M', 'longFmt': '271,900,000'},
	'grossProfit': {'raw': 142700000, 'fmt': '142.7M', 'longFmt': '142,700,000'}, 
	'sellingGeneralAdministrative': {'raw': 84500000, 'fmt': '84.5M', 'longFmt': '84,500,000'},

	'totalOperatingExpenses': {'raw': 340000000, 'fmt': '340M', 'longFmt': '340,000,000'},
	'operatingIncome': {'raw': 49500000, 'fmt': '49.5M', 'longFmt': '49,500,000'},
	'interestExpense': {'raw': -10100000, 'fmt': '-10.1M', 'longFmt': '-10,100,000'},
	'otherOperatingExpenses': {},
	'incomeBeforeTax': {'raw': 32700000, 'fmt': '32.7M', 'longFmt': '32,700,000'},

	'incomeTaxExpense': {'raw': 2900000, 'fmt': '2.9M', 'longFmt': '2,900,000'},
	'netIncomeFromContinuingOps': {'raw': 29800000, 'fmt': '29.8M', 'longFmt': '29,800,000'},
	'netIncome': {'raw': 29800000, 'fmt': '29.8M', 'longFmt': '29,800,000'},
	'netIncomeApplicableToCommonShares': {'raw': 8000000, 'fmt': '8M', 'longFmt': '8,000,000'}
	"Basic EPS"

	"Diluted EPS"
	"Basic Average Shares"
	"Diluted Average Shares"
	"EBITDA" 'ebit': {'raw': 19500000, 'fmt': '19.5M', 'longFmt': '19,500,000'},


# Quarterly - Balance Sheet
# Quarterly - Cash Flow
"""


class QuarterlyFinancials (yahoo.Yahoo):

	URL = "https://uk.finance.yahoo.com/quote/{sym}/financials?p={sym}"

	jsonMAP = { \
				# Quarterly - Income Statement
				#"breakdown" ??
				#"revenue" ??
				"costOfRevenue"						:	"""context.dispatcher.stores.QuoteSummaryStore.'incomeStatementHistoryQuarterly'.'incomeStatementHistory'[*].costOfRevenue.raw""",
				"grossProfit"						:	"""context.dispatcher.stores.QuoteSummaryStore.'incomeStatementHistoryQuarterly'.'incomeStatementHistory'[*].grossProfit.raw""",
				"sellingGeneralAdministrative"		:	"""context.dispatcher.stores.QuoteSummaryStore.'incomeStatementHistoryQuarterly'.'incomeStatementHistory'[*].sellingGeneralAdministrative.raw""",

				"totalOperatingExpenses"			:	"""context.dispatcher.stores.QuoteSummaryStore.'incomeStatementHistoryQuarterly'.'incomeStatementHistory'[*].totalOperatingExpenses.raw""",
				"operatingIncome"					:	"""context.dispatcher.stores.QuoteSummaryStore.'incomeStatementHistoryQuarterly'.'incomeStatementHistory'[*].operatingIncome.raw""",
				"interestExpense"					:	"""context.dispatcher.stores.QuoteSummaryStore.'incomeStatementHistoryQuarterly'.'incomeStatementHistory'[*].interestExpense.raw""",
				"otherOperatingExpenses"			:	"""context.dispatcher.stores.QuoteSummaryStore.'incomeStatementHistoryQuarterly'.'incomeStatementHistory'[*].otherOperatingExpenses.raw""",
				"incomeBeforeTax"					:	"""context.dispatcher.stores.QuoteSummaryStore.'incomeStatementHistoryQuarterly'.'incomeStatementHistory'[*].incomeBeforeTax.raw""",

				"incomeTaxExpense"					:	"""context.dispatcher.stores.QuoteSummaryStore.'incomeStatementHistoryQuarterly'.'incomeStatementHistory'[*].incomeTaxExpense.raw""",
				"netIncomeFromContinuingOps"		:	"""context.dispatcher.stores.QuoteSummaryStore.'incomeStatementHistoryQuarterly'.'incomeStatementHistory'[*].netIncomeFromContinuingOps.raw""",
				"netIncome"							:	"""context.dispatcher.stores.QuoteSummaryStore.'incomeStatementHistoryQuarterly'.'incomeStatementHistory'[*].netIncome.raw""",
				"netIncomeApplicableToCommonShares"	:	"""context.dispatcher.stores.QuoteSummaryStore.'incomeStatementHistoryQuarterly'.'incomeStatementHistory'[*].netIncomeApplicableToCommonShares.raw""",
				#"Basic EPS" ??

				#"Diluted EPS" ??
				#"Basic Average Shares" ??
				#"Diluted Average Shares" ??

				"ebit"	:	"""context.dispatcher.stores.QuoteSummaryStore.'incomeStatementHistoryQuarterly'.'incomeStatementHistory'[*].ebit.raw""",

				# Quarterly - Balance Sheet
				# Quarterly - Cash Flow
				# DEMO
				#"demo"			: """context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistoryQuarterly.incomeStatementHistory""",
				"demo"			: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistoryQuarterly.balanceSheetStatements""",
				#"demo"			: """context.dispatcher.stores.QuoteSummaryStore.cashflowStatementHistoryQuarterly.cashflowStatements""",
			}

	def __init__(self, symbol):
		super(QuarterlyFinancials, self).__init__(self.URL, symbol)
		self.logger		=	logging.getLogger('QuarterlyFinancials')

	def __del__(self):
		super(QuarterlyFinancials, self).__del__()

	#debug
	def debug(self):
		#Demo
#		self.debug_print("demo")
		# Quarterly - Income Statement
		#"breakdown" ??
		#"revenue" ??
		self.debug_print("costOfRevenue")
		self.debug_print("grossProfit")
		self.debug_print("sellingGeneralAdministrative")

		self.debug_print("totalOperatingExpenses")
		self.debug_print("operatingIncome")
		self.debug_print("interestExpense")
		self.debug_print("otherOperatingExpenses")
		self.debug_print("incomeBeforeTax")

		self.debug_print("incomeTaxExpense")
		self.debug_print("netIncomeFromContinuingOps")
		self.debug_print("netIncome")
		self.debug_print("netIncomeApplicableToCommonShares")
		#"Basic EPS" ??

		#"Diluted EPS" ??
		#"Basic Average Shares" ??
		#"Diluted Average Shares" ??

		self.debug_print("ebit")

