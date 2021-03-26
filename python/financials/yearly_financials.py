# Financials

import logging

from python.common import yahoo


class YearlyFinancials (yahoo.Yahoo):

	URL = "https://uk.finance.yahoo.com/quote/{sym}/financials?p={sym}"

	jsonMAP = { \
				#  - Income Statement
				#"breakdown" ??
				#"revenue" ??
				"costOfRevenue"						:	"""context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistory.incomeStatementHistory[*].costOfRevenue.raw""",
				"grossProfit"						:	"""context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistory.incomeStatementHistory[*].grossProfit.raw""",
				"sellingGeneralAdministrative"		:	"""context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistory.incomeStatementHistory[*].sellingGeneralAdministrative.raw""",

				"totalOperatingExpenses"			:	"""context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistory.incomeStatementHistory[*].totalOperatingExpenses.raw""",
				"operatingIncome"					:	"""context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistory.incomeStatementHistory[*].operatingIncome.raw""",
				"interestExpense"					:	"""context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistory.incomeStatementHistory[*].interestExpense.raw""",
				"otherOperatingExpenses"			:	"""context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistory.incomeStatementHistory[*].otherOperatingExpenses.raw""",
				"incomeBeforeTax"					:	"""context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistory.incomeStatementHistory[*].incomeBeforeTax.raw""",

				"incomeTaxExpense"					:	"""context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistory.incomeStatementHistory[*].incomeTaxExpense.raw""",
				"netIncomeFromContinuingOps"		:	"""context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistory.incomeStatementHistory[*].netIncomeFromContinuingOps.raw""",
				"netIncome"							:	"""context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistory.incomeStatementHistory[*].netIncome.raw""",
				"netIncomeApplicableToCommonShares"	:	"""context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistory.incomeStatementHistory[*].netIncomeApplicableToCommonShares.raw""",
				#"Basic EPS" ??

				#"Diluted EPS" ??
				#"Basic Average Shares" ??
				#"Diluted Average Shares" ??

				"ebit"	:	"""context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistory.incomeStatementHistory[*].ebit.raw""",

				#  - Balance Sheet
				#Assets
				#Current assets
				"cash"								: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistory.balanceSheetStatements[*].cash.raw""",
				"netReceivables"					: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistory.balanceSheetStatements[*].netReceivables.raw""",
				"inventory"							: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistory.balanceSheetStatements[*].inventory.raw""",
				"otherCurrentAssets"				: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistory.balanceSheetStatements[*].otherCurrentAssets.raw""",

				#Non-current assets
				#Property, plant and equipment
				"propertyPlantEquipment"			: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistory.balanceSheetStatements[*].propertyPlantEquipment.raw""",
				"goodWill"							: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistory.balanceSheetStatements[*].goodWill.raw""",
				"intangibleAssets"					: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistory.balanceSheetStatements[*].intangibleAssets.raw""",

				# Other long-term assets
				# Total non-current assets
				"totalAssets"						: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistory.balanceSheetStatements[*].totalAssets.raw""",

				# Liabilities and stockholders' equity

				# Liabilities
				# Current liabilities
				# Current debt
				"accountsPayable"					: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistory.balanceSheetStatements[*].accountsPayable.raw""",
				# Accrued liabilities
				# Other current liabilities
				# Total current liabilities


				# Non-current liabilities
				# Long-term debt
				# Deferred tax liabilities
				# Other long-term liabilities
				# Total non-current liabilities
				"totalLiab"							: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistory.balanceSheetStatements[*].totalLiab.raw""",

				# Stockholders' equity
				"commonStock"						: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistory.balanceSheetStatements[*].commonStock.raw""",
				"retainedEarnings"					: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistory.balanceSheetStatements[*].retainedEarnings.raw""",
				"otherStockholderEquity"			: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistory.balanceSheetStatements[*].otherStockholderEquity.raw""",
				"totalStockholderEquity"			: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistory.balanceSheetStatements[*].totalStockholderEquity.raw""",


				#  - Cash Flow


				## BUFFETOLOGY
				##	-- Time for earnings
				"currentEarningsDates"				: """context.dispatcher.stores.QuoteSummaryStore.earnings.earningsChart.earningsDate.earningsDate[*].fmt"""

				#-- Historic Earnings
				"historicYearlyEarningsDate"		: """context.dispatcher.stores.QuoteSummaryStore.earnings.financialsChart.yearly[*].date""",
				"historicYearlyEarningsEarnings"	: """context.dispatcher.stores.QuoteSummaryStore.earnings.financialsChart.yearly[*].earnings.raw""",
				"historicYearlyEarningsRevenue"		: """context.dispatcher.stores.QuoteSummaryStore.earnings.financialsChart.yearly[*].revenue.raw""",


				# DEMO
				#"demo"			: """context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistory.incomeStatementHistory""",
				"demo"			: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistory.balanceSheetStatements""",
				#"demo"			: """context.dispatcher.stores.QuoteSummaryStore.cashflowStatementHistory.cashflowStatements""",
			}

	def __init__(self, symbol):
		super(YearlyFinancials, self).__init__(self.URL, symbol)
		self.logger		=	logging.getLogger('YearlyFinancials')

	def __del__(self):
		super(YearlyFinancials, self).__del__()

	#debug
	def debug(self):
		#Demo
#		self.debug_print("demo")
		#  - Income Statement
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

		# - Balance Sheet
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
