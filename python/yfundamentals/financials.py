# Financials
import logging

from ..common import html_wrapped_json


class Financials (html_wrapped_json.HTMLWrappedJson):

	URL = "https://uk.finance.yahoo.com/quote/{sym}/financials?p={sym}"

	jsonMAP = { \
				#-- Quarterly - 
				# Quarterly - Income Statement
				"Quarterly.endDate"								: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistoryQuarterly.balanceSheetStatements[*].endDate.fmt""",
				#"revenue" ??
				"Quarterly.costOfRevenue"						: """context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistoryQuarterly.incomeStatementHistory[*].costOfRevenue.raw""",
				"Quarterly.grossProfit"							: """context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistoryQuarterly.incomeStatementHistory[*].grossProfit.raw""",
				"Quarterly.sellingGeneralAdministrative"		: """context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistoryQuarterly.incomeStatementHistory[*].sellingGeneralAdministrative.raw""",

				"Quarterly.totalOperatingExpenses"				: """context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistoryQuarterly.incomeStatementHistory[*].totalOperatingExpenses.raw""",
				"Quarterly.operatingIncome"						: """context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistoryQuarterly.incomeStatementHistory[*].operatingIncome.raw""",
				"Quarterly.interestExpense"						: """context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistoryQuarterly.incomeStatementHistory[*].interestExpense.raw""",
				"Quarterly.otherOperatingExpenses"				: """context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistoryQuarterly.incomeStatementHistory[*].otherOperatingExpenses.raw""",
				"Quarterly.incomeBeforeTax"						: """context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistoryQuarterly.incomeStatementHistory[*].incomeBeforeTax.raw""",

				"Quarterly.incomeTaxExpense"					: """context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistoryQuarterly.incomeStatementHistory[*].incomeTaxExpense.raw""",
				"Quarterly.netIncomeFromContinuingOps"			: """context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistoryQuarterly.incomeStatementHistory[*].netIncomeFromContinuingOps.raw""",
				"Quarterly.netIncome"							: """context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistoryQuarterly.incomeStatementHistory[*].netIncome.raw""",
				"Quarterly.netIncomeApplicableToCommonShares"	: """context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistoryQuarterly.incomeStatementHistory[*].netIncomeApplicableToCommonShares.raw""",
				#"Basic EPS" ??

				#"Diluted EPS" ??
				#"Basic Average Shares" ??
				#"Diluted Average Shares" ??

				"Quarterly.ebit"								: """context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistoryQuarterly.incomeStatementHistory[*].ebit.raw""",

				# Quarterly - Balance Sheet
				#Assets
				#Current assets
				"Quarterly.cash"								: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistoryQuarterly.balanceSheetStatements[*].cash.raw""",
				"Quarterly.netReceivables"						: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistoryQuarterly.balanceSheetStatements[*].netReceivables.raw""",
				"Quarterly.inventory"							: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistoryQuarterly.balanceSheetStatements[*].inventory.raw""",
				"Quarterly.otherCurrentAssets"					: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistoryQuarterly.balanceSheetStatements[*].otherCurrentAssets.raw""",

				#Non-current assets
				#Property, plant and equipment
				"Quarterly.propertyPlantEquipment"				: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistoryQuarterly.balanceSheetStatements[*].propertyPlantEquipment.raw""",
				"Quarterly.goodWill"							: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistoryQuarterly.balanceSheetStatements[*].goodWill.raw""",
				"Quarterly.intangibleAssets"					: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistoryQuarterly.balanceSheetStatements[*].intangibleAssets.raw""",

				# Other long-term assets
				# Total non-current assets
				"Quarterly.totalAssets"							: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistoryQuarterly.balanceSheetStatements[*].totalAssets.raw""",

				# Liabilities and stockholders' equity

				# Liabilities
				# Current liabilities
				# Current debt
				"Quarterly.accountsPayable"						: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistoryQuarterly.balanceSheetStatements[*].accountsPayable.raw""",
				# Accrued liabilities
				# Other current liabilities
				# Total current liabilities


				# Non-current liabilities
				# Long-term debt
				# Deferred tax liabilities
				# Other long-term liabilities
				# Total non-current liabilities
				"Quarterly.totalLiab"							: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistoryQuarterly.balanceSheetStatements[*].totalLiab.raw""",

				# Stockholders' equity
				"Quarterly.commonStock"							: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistoryQuarterly.balanceSheetStatements[*].commonStock.raw""",
				"Quarterly.retainedEarnings"					: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistoryQuarterly.balanceSheetStatements[*].retainedEarnings.raw""",
				"Quarterly.otherStockholderEquity"				: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistoryQuarterly.balanceSheetStatements[*].otherStockholderEquity.raw""",
				"Quarterly.totalStockholderEquity"				: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistoryQuarterly.balanceSheetStatements[*].totalStockholderEquity.raw""",


				# Quarterly - Cash Flow
				"Yearly.endDate"							: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistory.balanceSheetStatements[*].endDate.fmt""",
				#  - Income Statement
				#"breakdown" ??
				#"revenue" ??
				"Yearly.costOfRevenue"						: """context.dispatcher.stores.QuoteTimeSeriesStore.timeSeries.annualCostOfRevenue[*].reportedValue.raw""",
				"Yearly.grossProfit"						: """context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistory.incomeStatementHistory[*].grossProfit.raw""",
				"Yearly.sellingGeneralAdministrative"		: """context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistory.incomeStatementHistory[*].sellingGeneralAdministrative.raw""",

				"Yearly.totalOperatingExpenses"				: """context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistory.incomeStatementHistory[*].totalOperatingExpenses.raw""",
				"Yearly.operatingIncome"					: """context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistory.incomeStatementHistory[*].operatingIncome.raw""",
				"Yearly.interestExpense"					: """context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistory.incomeStatementHistory[*].interestExpense.raw""",
				"Yearly.otherOperatingExpenses"				: """context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistory.incomeStatementHistory[*].otherOperatingExpenses.raw""",
				"Yearly.incomeBeforeTax"					: """context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistory.incomeStatementHistory[*].incomeBeforeTax.raw""",

				"Yearly.incomeTaxExpense"					: """context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistory.incomeStatementHistory[*].incomeTaxExpense.raw""",
				"Yearly.netIncomeFromContinuingOps"			: """context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistory.incomeStatementHistory[*].netIncomeFromContinuingOps.raw""",
				"Yearly.netIncome"							: """context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistory.incomeStatementHistory[*].netIncome.raw""",
				"Yearly.netIncomeApplicableToCommonShares"	: """context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistory.incomeStatementHistory[*].netIncomeApplicableToCommonShares.raw""",
				"Yearly.BasicEPS"							: """context.dispatcher.stores.QuoteTimeSeriesStore.timeSeries.annualBasicEPS[*].reportedValue.raw""",
				"Yearly.DilutedEPS"							: """context.dispatcher.stores.QuoteTimeSeriesStore.timeSeries.annualDilutedEPS[*].reportedValue.raw""",
				"Yearly.BasicAverageShares"					: """context.dispatcher.stores.QuoteTimeSeriesStore.timeSeries.annualBasicAverageShares[*].reportedValue.raw""",
				"Yearly.DilutedAverageShares"				: """context.dispatcher.stores.QuoteTimeSeriesStore.timeSeries.annualDilutedAverageShares[*].reportedValue.raw""",

				"Yearly.Ebitda"								: """context.dispatcher.stores.QuoteTimeSeriesStore.timeSeries.annualEbitda[*].reportedValue.raw""",

				#  - Balance Sheet
				#Assets
				#Current assets
				"Yearly.cash"								: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistory.balanceSheetStatements[*].cash.raw""",
				"Yearly.netReceivables"						: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistory.balanceSheetStatements[*].netReceivables.raw""",
				"Yearly.inventory"							: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistory.balanceSheetStatements[*].inventory.raw""",
				"Yearly.otherCurrentAssets"					: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistory.balanceSheetStatements[*].otherCurrentAssets.raw""",

				#Non-current assets
				#Property, plant and equipment
				"Yearly.propertyPlantEquipment"				: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistory.balanceSheetStatements[*].propertyPlantEquipment.raw""",
				"Yearly.goodWill"							: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistory.balanceSheetStatements[*].goodWill.raw""",
				"Yearly.intangibleAssets"					: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistory.balanceSheetStatements[*].intangibleAssets.raw""",

				# Other long-term assets
				# Total non-current assets
				"Yearly.totalAssets"						: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistory.balanceSheetStatements[*].totalAssets.raw""",

				# Liabilities and stockholders' equity

				# Liabilities
				# Current liabilities
				# Current debt
				"Yearly.accountsPayable"					: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistory.balanceSheetStatements[*].accountsPayable.raw""",
				# Accrued liabilities
				# Other current liabilities
				# Total current liabilities


				# Non-current liabilities
				# Long-term debt
				# Deferred tax liabilities
				# Other long-term liabilities
				# Total non-current liabilities
				"Yearly.totalLiab"							: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistory.balanceSheetStatements[*].totalLiab.raw""",

				# Stockholders' equity
				"Yearly.commonStock"						: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistory.balanceSheetStatements[*].commonStock.raw""",
				"Yearly.retainedEarnings"					: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistory.balanceSheetStatements[*].retainedEarnings.raw""",
				"Yearly.otherStockholderEquity"				: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistory.balanceSheetStatements[*].otherStockholderEquity.raw""",
				"Yearly.totalStockholderEquity"				: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistory.balanceSheetStatements[*].totalStockholderEquity.raw""",


				#  - Cash Flow

				## BUFFETOLOGY
				##	-- Time for earnings
				"Quarterly.currentEarningsDates"			: """context.dispatcher.stores.QuoteSummaryStore.earnings.earningsChart.earningsDate.earningsDate[*].fmt""",

				#-- Historic Earnings per share
				"Quarterly.historicEarningsEPSDate"			: """context.dispatcher.stores.QuoteSummaryStore.earnings.earningsChart.quarterly[*].date""",
				"Quarterly.historicEarningsEPS"				: """context.dispatcher.stores.QuoteSummaryStore.earnings.earningsChart.quarterly[*].actual.raw""",

				#-- Historic Earnings
				"Quarterly.historicEarningsDate"			: """context.dispatcher.stores.QuoteSummaryStore.earnings.financialsChart.quarterly[*].date""",
				"Quarterly.historicEarningsEarnings"		: """context.dispatcher.stores.QuoteSummaryStore.earnings.financialsChart.quarterly[*].earnings.raw""",
				"Quarterly.historicEarningsRevenue"			: """context.dispatcher.stores.QuoteSummaryStore.earnings.financialsChart.quarterly[*].revenue.raw""",

				#-- Historic Earnings
				"Yearly.historicEarningsDate"				: """context.dispatcher.stores.QuoteSummaryStore.earnings.financialsChart.yearly[*].date""",
				"Yearly.historicEarningsEarnings"			: """context.dispatcher.stores.QuoteSummaryStore.earnings.financialsChart.yearly[*].earnings.raw""",
				"Yearly.historicEarningsRevenue"			: """context.dispatcher.stores.QuoteSummaryStore.earnings.financialsChart.yearly[*].revenue.raw""",

				# DEMO
				#"demo"			: """context.dispatcher.stores.QuoteSummaryStore.incomeStatementHistoryQuarterly.incomeStatementHistory""",
				#"demo"			: """context.dispatcher.stores.QuoteSummaryStore.balanceSheetHistoryQuarterly.balanceSheetStatements""",
				#"demo"			: """context.dispatcher.stores.QuoteSummaryStore.cashflowStatementHistoryQuarterly.cashflowStatements""",
				#"demo"			: """context.dispatcher.stores.QuoteSummaryStore.earnings""",
			}

	def __init__(self, symbol):
		super(Financials, self).__init__(self.URL, symbol)
		self.logger		=	logging.getLogger('Financials')

	def __del__(self):
		super(Financials, self).__del__()
