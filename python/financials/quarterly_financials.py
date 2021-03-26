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
	# Other long-term assets
	Total non-current assets
	'totalAssets': {'raw': 3048700000, 'fmt': '3.05B', 'longFmt': '3,048,700,000'},

	Liabilities and stockholders' equity

	Liabilities
	Current liabilities
	Current debt
	'accountsPayable': {'raw': 180200000, 'fmt': '180.2M', 'longFmt': '180,200,000'}
	Accrued liabilities
	Other current liabilities
	Total current liabilities


	Non-current liabilities
	Long-term debt
	Deferred tax liabilities
	Other long-term liabilities
	Total non-current liabilities
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
				#Assets
				#Current assets
				"cash"								: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistoryQuarterly.balanceSheetStatements[*].cash.raw""",
				"netReceivables"					: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistoryQuarterly.balanceSheetStatements[*].netReceivables.raw""",
				"inventory"							: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistoryQuarterly.balanceSheetStatements[*].inventory.raw""",
				"otherCurrentAssets"				: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistoryQuarterly.balanceSheetStatements[*].otherCurrentAssets.raw""",

				#Non-current assets
				#Property, plant and equipment
				"propertyPlantEquipment"			: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistoryQuarterly.balanceSheetStatements[*].propertyPlantEquipment.raw""",
				"goodWill"							: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistoryQuarterly.balanceSheetStatements[*].goodWill.raw""",
				"intangibleAssets"					: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistoryQuarterly.balanceSheetStatements[*].intangibleAssets.raw""",

				# Other long-term assets
				# Total non-current assets
				"totalAssets"						: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistoryQuarterly.balanceSheetStatements[*].totalAssets.raw""",

				# Liabilities and stockholders' equity

				# Liabilities
				# Current liabilities
				# Current debt
				"accountsPayable"					: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistoryQuarterly.balanceSheetStatements[*].accountsPayable.raw""",
				# Accrued liabilities
				# Other current liabilities
				# Total current liabilities


				# Non-current liabilities
				# Long-term debt
				# Deferred tax liabilities
				# Other long-term liabilities
				# Total non-current liabilities
				"totalLiab"							: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistoryQuarterly.balanceSheetStatements[*].totalLiab.raw""",

				# Stockholders' equity
				"commonStock"					: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistoryQuarterly.balanceSheetStatements[*].commonStock.raw""",
				"retainedEarnings"				: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistoryQuarterly.balanceSheetStatements[*].retainedEarnings.raw""",
				"otherStockholderEquity"		: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistoryQuarterly.balanceSheetStatements[*].otherStockholderEquity.raw""",
				"totalStockholderEquity"		: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistoryQuarterly.balanceSheetStatements[*].totalStockholderEquity.raw""",


				# Quarterly - Cash Flow

				## BUFFETOLOGY
				##	-- Time for earnings
				"currentEarningsDates"				: """context.dispatcher.stores.QuoteSummaryStore.earnings.earningsChart.earningsDate.earningsDate[*].fmt""",

				#-- Historic Earnings per share
				"historicQuarterlyEarningsEPSDate"	: """context.dispatcher.stores.QuoteSummaryStore.earnings.earningsChart.quarterly[*].date""",
				"historicQuarterlyEarningsEPS"		: """context.dispatcher.stores.QuoteSummaryStore.earnings.earningsChart.quarterly[*].actual.raw""",

				#-- Historic Earnings
				"historicQuarterlyEarningsDate"		: """context.dispatcher.stores.QuoteSummaryStore.earnings.financialsChart.quarterly[*].date""",
				"historicQuarterlyEarningsEarnings"	: """context.dispatcher.stores.QuoteSummaryStore.earnings.financialsChart.quarterly[*].earnings.raw""",
				"historicQuarterlyEarningsRevenue"	: """context.dispatcher.stores.QuoteSummaryStore.earnings.financialsChart.quarterly[*].revenue.raw""",

				# DEMO
				#"demo"			: """context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistoryQuarterly.incomeStatementHistory""",
				#"demo"			: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistoryQuarterly.balanceSheetStatements""",
				#"demo"			: """context.dispatcher.stores.QuoteSummaryStore.cashflowStatementHistoryQuarterly.cashflowStatements""",
				"demo"			: """context.dispatcher.stores.QuoteSummaryStore.earnings""",
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

		# Quarterly - Balance Sheet
		#Assets
		#Current assets
		self.debug_print("cash")
		self.debug_print("netReceivables")
		self.debug_print("inventory")
		self.debug_print("otherCurrentAssets")

		#Non-current assets
		#Property, plant and equipment
		self.debug_print("propertyPlantEquipment")
		self.debug_print("goodWill")
		self.debug_print("intangibleAssets")

		# Other long-term assets
		# Total non-current assets
		self.debug_print("totalAssets")

		# Liabilities and stockholders' equity

		# Liabilities
		# Current liabilities
		# Current debt
		self.debug_print("accountsPayable")
		# Accrued liabilities
		# Other current liabilities
		# Total current liabilities


		# Non-current liabilities
		# Long-term debt
		# Deferred tax liabilities
		# Other long-term liabilities
		# Total non-current liabilities
		self.debug_print("totalLiab")

		# Stockholders' equity
		self.debug_print("commonStock")
		self.debug_print("retainedEarnings")
		self.debug_print("otherStockholderEquity")
		self.debug_print("totalStockholderEquity")

		## BUFFETOLOGY
		##	-- Time for earnings
		self.debug_print("currentEarningsDates")

		#-- Historic Earnings per share
		self.debug_print("historicQuarterlyEarningsEPSDate")
		self.debug_print("historicQuarterlyEarningsEPS")

		#-- Historic Earnings
		self.debug_print("historicQuarterlyEarningsDate")
		self.debug_print("historicQuarterlyEarningsEarnings")
		self.debug_print("historicQuarterlyEarningsRevenue")
