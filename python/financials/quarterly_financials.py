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
	'endDate': {'raw': 1609372800, 'fmt': '2020-12-31'},
	#Assets					
	#Current assets					
	'cash': {'raw': 36600000, 'fmt': '36.6M', 'longFmt': '36,600,000'},
	'netReceivables': {'raw': 356000000, 'fmt': '356M', 'longFmt': '356,000,000'},
	'inventory': {'raw': 305100000, 'fmt': '305.1M', 'longFmt': '305,100,000'},
	'otherCurrentAssets': {'raw': 30500000, 'fmt': '30.5M', 'longFmt': '30,500,000'},
	'totalCurrentAssets': {'raw': 728200000, 'fmt': '728.2M', 'longFmt':'728,200,000'},

	#Non-current assets					
	#Property, plant and equipment					
	'propertyPlantEquipment': {'raw': 330600000, 'fmt': '330.6M', 'longFmt': '330,600,000'},

	'goodWill': {'raw': 827400000, 'fmt': '827.4M', 'longFmt': '827,400,000'},
	{'intangibleAssets': {'raw': 977000000, 'fmt': '977M', 'longFmt': '977,000,000'},
	# Other long-term assets	49,000	36,500	24,900	19,700	17,400
	Total non-current assets	2,320,500	1,930,800	1,909,200	1,915,200	1,982,600
	'totalAssets': {'raw': 3048700000, 'fmt': '3.05B', 'longFmt': '3,048,700,000'},

	Liabilities and stockholders' equity

	Liabilities					
	Current liabilities					
	Current debt	76,500	35,800	49,900	67,200	33,200
	'accountsPayable': {'raw': 180200000, 'fmt': '180.2M', 'longFmt': '180,200,000'}
	Accrued liabilities	91,400	76,900	64,100	64,200	99,700
	Other current liabilities	145,200	124,200	105,500	104,000	139,900
	Total current liabilities	556,900	470,300	484,100	469,500	588,800


	Non-current liabilities					
	Long-term debt	1,054,600	876,300	971,400	856,900	777,200
	Deferred tax liabilities	170,600	170,700	168,400	167,300	177,500
	Other long-term liabilities	130,300	108,200	95,200	91,000	98,400
	Total non-current liabilities	1,749,100	1,500,300	1,580,900	1,465,800	1,426,100
	'totalLiab': {'raw': 2306000000, 'fmt': '2.31B', 'longFmt': '2,306,000,000'},

	Stockholders' equity					
	'commonStock': {'raw': 1000000, 'fmt': '1M', 'longFmt': '1,000,000'},
	'retainedEarnings': {'raw': -537300000, 'fmt': '-537.3M', 'longFmt': '-537,300,000'},
	'otherStockholderEquity': {'raw': -564200000, 'fmt': '-564.2M', 'longFmt': '-564,200,000'},
	'totalStockholderEquity': {'raw': 742700000, 'fmt': '742.7M', 'longFmt': '742,700,000'},


# Quarterly - Cash Flow
"""


class QuarterlyFinancials (yahoo.Yahoo):

	URL = "https://uk.finance.yahoo.com/quote/{sym}/financials?p={sym}"

	jsonMAP = { \
				# Quarterly - Income Statement
				"endDate"							: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistoryQuarterly.balanceSheetStatements[*].endDate.fmt""",
				#"revenue" ??
				"costOfRevenue"						:	"""context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistoryQuarterly.incomeStatementHistory[*].costOfRevenue.raw""",
				"grossProfit"						:	"""context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistoryQuarterly.incomeStatementHistory[*].grossProfit.raw""",
				"sellingGeneralAdministrative"		:	"""context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistoryQuarterly.incomeStatementHistory[*].sellingGeneralAdministrative.raw""",

				"totalOperatingExpenses"			:	"""context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistoryQuarterly.incomeStatementHistory[*].totalOperatingExpenses.raw""",
				"operatingIncome"					:	"""context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistoryQuarterly.incomeStatementHistory[*].operatingIncome.raw""",
				"interestExpense"					:	"""context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistoryQuarterly.incomeStatementHistory[*].interestExpense.raw""",
				"otherOperatingExpenses"			:	"""context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistoryQuarterly.incomeStatementHistory[*].otherOperatingExpenses.raw""",
				"incomeBeforeTax"					:	"""context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistoryQuarterly.incomeStatementHistory[*].incomeBeforeTax.raw""",

				"incomeTaxExpense"					:	"""context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistoryQuarterly.incomeStatementHistory[*].incomeTaxExpense.raw""",
				"netIncomeFromContinuingOps"		:	"""context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistoryQuarterly.incomeStatementHistory[*].netIncomeFromContinuingOps.raw""",
				"netIncome"							:	"""context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistoryQuarterly.incomeStatementHistory[*].netIncome.raw""",
				"netIncomeApplicableToCommonShares"	:	"""context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistoryQuarterly.incomeStatementHistory[*].netIncomeApplicableToCommonShares.raw""",
				#"Basic EPS" ??

				#"Diluted EPS" ??
				#"Basic Average Shares" ??
				#"Diluted Average Shares" ??

				"ebit"	:	"""context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistoryQuarterly.incomeStatementHistory[*].ebit.raw""",

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
		self.debug_print("endDate")
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
		#Demo
		#self.debug_print("demo")
