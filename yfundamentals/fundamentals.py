# Financials
import logging

from . import fundamentals_base

class Fundamentals (fundamentals_base.FundamentalsBase):

	jsonMAP = { \
				#-- Quarterly - 
				# Quarterly - Income Statement
				"Quarterly.endDate"								:	FINANCIALS,
				#"revenue" ??
				"Quarterly.costOfRevenue"						:	FINANCIALS,
				"Quarterly.grossProfit"							:	FINANCIALS,
				"Quarterly.sellingGeneralAdministrative"		:	FINANCIALS,

				"Quarterly.totalOperatingExpenses"				:	FINANCIALS,
				"Quarterly.operatingIncome"						:	FINANCIALS,
				"Quarterly.interestExpense"						:	FINANCIALS,
				"Quarterly.otherOperatingExpenses"				:	FINANCIALS,
				"Quarterly.incomeBeforeTax"						:	FINANCIALS,

				"Quarterly.incomeTaxExpense"					:	FINANCIALS,
				"Quarterly.netIncomeFromContinuingOps"			:	FINANCIALS,
				"Quarterly.netIncome"							:	FINANCIALS,
				"Quarterly.netIncomeApplicableToCommonShares"	:	FINANCIALS,
				#"Basic EPS" ??

				#"Diluted EPS" ??
				#"Basic Average Shares" ??
				#"Diluted Average Shares" ??

				"Quarterly.ebit"								:	FINANCIALS,

				# Quarterly - Balance Sheet
				#Assets
				#Current assets
				"Quarterly.cash"								:	FINANCIALS,
				"Quarterly.netReceivables"						:	FINANCIALS,
				"Quarterly.inventory"							:	FINANCIALS,
				"Quarterly.otherCurrentAssets"					:	FINANCIALS,

				#Non-current assets
				#Property, plant and equipment
				"Quarterly.propertyPlantEquipment"				:	FINANCIALS,
				"Quarterly.goodWill"							:	FINANCIALS,
				"Quarterly.intangibleAssets"					:	FINANCIALS,

				# Other long-term assets
				# Total non-current assets
				"Quarterly.totalAssets"							:	FINANCIALS,

				# Liabilities and stockholders' equity

				# Liabilities
				# Current liabilities
				# Current debt
				"Quarterly.accountsPayable"						:	FINANCIALS,
				# Accrued liabilities
				# Other current liabilities
				# Total current liabilities


				# Non-current liabilities
				# Long-term debt
				# Deferred tax liabilities
				# Other long-term liabilities
				# Total non-current liabilities
				"Quarterly.totalLiab"							:	FINANCIALS,

				# Stockholders' equity
				"Quarterly.commonStock"							:	FINANCIALS,
				"Quarterly.retainedEarnings"					:	FINANCIALS,
				"Quarterly.otherStockholderEquity"				:	FINANCIALS,
				"Quarterly.totalStockholderEquity"				:	FINANCIALS,


				# Quarterly - Cash Flow

				#  - Income Statement
				#"breakdown" ??
				#"revenue" ??
				"Yearly.costOfRevenue"						:	FINANCIALS,
				"Yearly.grossProfit"						:	FINANCIALS,
				"Yearly.sellingGeneralAdministrative"		:	FINANCIALS,

				"Yearly.totalOperatingExpenses"				:	FINANCIALS,
				"Yearly.operatingIncome"					:	FINANCIALS,
				"Yearly.interestExpense"					:	FINANCIALS,
				"Yearly.otherOperatingExpenses"				:	FINANCIALS,
				"Yearly.incomeBeforeTax"					:	FINANCIALS,

				"Yearly.incomeTaxExpense"					:	FINANCIALS,
				"Yearly.netIncomeFromContinuingOps"			:	FINANCIALS,
				"Yearly.netIncome"							:	FINANCIALS,
				"Yearly.netIncomeApplicableToCommonShares"	:	FINANCIALS,
				#"Basic EPS" ??

				#"Diluted EPS" ??
				#"Basic Average Shares" ??
				#"Diluted Average Shares" ??

				"Yearly.ebit"	:	FINANCIALS,

				#  - Balance Sheet
				#Assets
				#Current assets
				"Yearly.cash"								:	FINANCIALS,
				"Yearly.netReceivables"						:	FINANCIALS,
				"Yearly.inventory"							:	FINANCIALS,
				"Yearly.otherCurrentAssets"					:	FINANCIALS,

				#Non-current assets
				#Property, plant and equipment
				"Yearly.propertyPlantEquipment"				:	FINANCIALS,
				"Yearly.goodWill"							:	FINANCIALS,
				"Yearly.intangibleAssets"					:	FINANCIALS,

				# Other long-term assets
				# Total non-current assets
				"Yearly.totalAssets"						:	FINANCIALS,

				# Liabilities and stockholders' equity

				# Liabilities
				# Current liabilities
				# Current debt
				"Yearly.accountsPayable"					:	FINANCIALS,
				# Accrued liabilities
				# Other current liabilities
				# Total current liabilities


				# Non-current liabilities
				# Long-term debt
				# Deferred tax liabilities
				# Other long-term liabilities
				# Total non-current liabilities
				"Yearly.totalLiab"							:	FINANCIALS,

				# Stockholders' equity
				"Yearly.commonStock"						:	FINANCIALS,
				"Yearly.retainedEarnings"					:	FINANCIALS,
				"Yearly.otherStockholderEquity"				:	FINANCIALS,
				"Yearly.totalStockholderEquity"				:	FINANCIALS,


				#  - Cash Flow

				## BUFFETOLOGY
				##	-- Time for earnings
				"Quarterly.currentEarningsDates"			:	FINANCIALS,

				#-- Historic Earnings per share
				"Quarterly.historicEarningsEPSDate"			:	FINANCIALS,
				"Quarterly.historicEarningsEPS"				:	FINANCIALS,

				#-- Historic Earnings
				"Quarterly.historicEarningsDate"			:	FINANCIALS,
				"Quarterly.historicEarningsEarnings"		:	FINANCIALS,
				"Quarterly.historicEarningsRevenue"			:	FINANCIALS,

				#-- Historic Earnings
				"Yearly.historicEarningsDate"				:	FINANCIALS,
				"Yearly.historicEarningsEarnings"			:	FINANCIALS,
				"Yearly.historicEarningsRevenue"			:	FINANCIALS,

				# DEMO
				#"demo"			:	FINANCIALS,
				#"demo"			:	FINANCIALS,
				#"demo"			:	FINANCIALS,
				#"demo"			:	FINANCIALS,
			}

	def __init__(self, symbol):
		super(Fundamentals, self).__init__(symbol)
		self.logger		=	logging.getLogger('Financials')

	def __del__(self):
		super(Fundamentals, self).__del__()

	# Operator[]
	def __getitem__(self, key):
		data = None
		obj = self.getRequestObject(key)
		if (obj is not None):
			data = obj[key]
