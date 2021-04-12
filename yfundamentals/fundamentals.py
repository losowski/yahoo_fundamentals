# Financials
import logging

from . import fundamentals_base

class Fundamentals (fundamentals_base.FundamentalsBase):

	jsonMAP = { \
				#-- Quarterly - 
				# Quarterly - Income Statement
				"Quarterly.endDate"								:	fundamentals_base.FundamentalsBase.FINANCIALS,
				#"revenue" ??
				"Quarterly.costOfRevenue"						:	fundamentals_base.FundamentalsBase.FINANCIALS,
				"Quarterly.grossProfit"							:	fundamentals_base.FundamentalsBase.FINANCIALS,
				"Quarterly.sellingGeneralAdministrative"		:	fundamentals_base.FundamentalsBase.FINANCIALS,

				"Quarterly.totalOperatingExpenses"				:	fundamentals_base.FundamentalsBase.FINANCIALS,
				"Quarterly.operatingIncome"						:	fundamentals_base.FundamentalsBase.FINANCIALS,
				"Quarterly.interestExpense"						:	fundamentals_base.FundamentalsBase.FINANCIALS,
				"Quarterly.otherOperatingExpenses"				:	fundamentals_base.FundamentalsBase.FINANCIALS,
				"Quarterly.incomeBeforeTax"						:	fundamentals_base.FundamentalsBase.FINANCIALS,

				"Quarterly.incomeTaxExpense"					:	fundamentals_base.FundamentalsBase.FINANCIALS,
				"Quarterly.netIncomeFromContinuingOps"			:	fundamentals_base.FundamentalsBase.FINANCIALS,
				"Quarterly.netIncome"							:	fundamentals_base.FundamentalsBase.FINANCIALS,
				"Quarterly.netIncomeApplicableToCommonShares"	:	fundamentals_base.FundamentalsBase.FINANCIALS,
				#"Basic EPS" ??

				#"Diluted EPS" ??
				#"Basic Average Shares" ??
				#"Diluted Average Shares" ??

				"Quarterly.ebit"								:	fundamentals_base.FundamentalsBase.FINANCIALS,

				# Quarterly - Balance Sheet
				#Assets
				#Current assets
				"Quarterly.cash"								:	fundamentals_base.FundamentalsBase.FINANCIALS,
				"Quarterly.netReceivables"						:	fundamentals_base.FundamentalsBase.FINANCIALS,
				"Quarterly.inventory"							:	fundamentals_base.FundamentalsBase.FINANCIALS,
				"Quarterly.otherCurrentAssets"					:	fundamentals_base.FundamentalsBase.FINANCIALS,

				#Non-current assets
				#Property, plant and equipment
				"Quarterly.propertyPlantEquipment"				:	fundamentals_base.FundamentalsBase.FINANCIALS,
				"Quarterly.goodWill"							:	fundamentals_base.FundamentalsBase.FINANCIALS,
				"Quarterly.intangibleAssets"					:	fundamentals_base.FundamentalsBase.FINANCIALS,

				# Other long-term assets
				# Total non-current assets
				"Quarterly.totalAssets"							:	fundamentals_base.FundamentalsBase.FINANCIALS,

				# Liabilities and stockholders' equity

				# Liabilities
				# Current liabilities
				# Current debt
				"Quarterly.accountsPayable"						:	fundamentals_base.FundamentalsBase.FINANCIALS,
				# Accrued liabilities
				# Other current liabilities
				# Total current liabilities


				# Non-current liabilities
				# Long-term debt
				# Deferred tax liabilities
				# Other long-term liabilities
				# Total non-current liabilities
				"Quarterly.totalLiab"							:	fundamentals_base.FundamentalsBase.FINANCIALS,

				# Stockholders' equity
				"Quarterly.commonStock"							:	fundamentals_base.FundamentalsBase.FINANCIALS,
				"Quarterly.retainedEarnings"					:	fundamentals_base.FundamentalsBase.FINANCIALS,
				"Quarterly.otherStockholderEquity"				:	fundamentals_base.FundamentalsBase.FINANCIALS,
				"Quarterly.totalStockholderEquity"				:	fundamentals_base.FundamentalsBase.FINANCIALS,


				# Quarterly - Cash Flow

				#  - Income Statement
				#"breakdown" ??
				#"revenue" ??
				"Yearly.costOfRevenue"						:	fundamentals_base.FundamentalsBase.FINANCIALS,
				"Yearly.grossProfit"						:	fundamentals_base.FundamentalsBase.FINANCIALS,
				"Yearly.sellingGeneralAdministrative"		:	fundamentals_base.FundamentalsBase.FINANCIALS,

				"Yearly.totalOperatingExpenses"				:	fundamentals_base.FundamentalsBase.FINANCIALS,
				"Yearly.operatingIncome"					:	fundamentals_base.FundamentalsBase.FINANCIALS,
				"Yearly.interestExpense"					:	fundamentals_base.FundamentalsBase.FINANCIALS,
				"Yearly.otherOperatingExpenses"				:	fundamentals_base.FundamentalsBase.FINANCIALS,
				"Yearly.incomeBeforeTax"					:	fundamentals_base.FundamentalsBase.FINANCIALS,

				"Yearly.incomeTaxExpense"					:	fundamentals_base.FundamentalsBase.FINANCIALS,
				"Yearly.netIncomeFromContinuingOps"			:	fundamentals_base.FundamentalsBase.FINANCIALS,
				"Yearly.netIncome"							:	fundamentals_base.FundamentalsBase.FINANCIALS,
				"Yearly.netIncomeApplicableToCommonShares"	:	fundamentals_base.FundamentalsBase.FINANCIALS,
				#"Basic EPS" ??

				#"Diluted EPS" ??
				#"Basic Average Shares" ??
				#"Diluted Average Shares" ??

				"Yearly.ebit"	:	fundamentals_base.FundamentalsBase.FINANCIALS,

				#  - Balance Sheet
				#Assets
				#Current assets
				"Yearly.cash"								:	fundamentals_base.FundamentalsBase.FINANCIALS,
				"Yearly.netReceivables"						:	fundamentals_base.FundamentalsBase.FINANCIALS,
				"Yearly.inventory"							:	fundamentals_base.FundamentalsBase.FINANCIALS,
				"Yearly.otherCurrentAssets"					:	fundamentals_base.FundamentalsBase.FINANCIALS,

				#Non-current assets
				#Property, plant and equipment
				"Yearly.propertyPlantEquipment"				:	fundamentals_base.FundamentalsBase.FINANCIALS,
				"Yearly.goodWill"							:	fundamentals_base.FundamentalsBase.FINANCIALS,
				"Yearly.intangibleAssets"					:	fundamentals_base.FundamentalsBase.FINANCIALS,

				# Other long-term assets
				# Total non-current assets
				"Yearly.totalAssets"						:	fundamentals_base.FundamentalsBase.FINANCIALS,

				# Liabilities and stockholders' equity

				# Liabilities
				# Current liabilities
				# Current debt
				"Yearly.accountsPayable"					:	fundamentals_base.FundamentalsBase.FINANCIALS,
				# Accrued liabilities
				# Other current liabilities
				# Total current liabilities


				# Non-current liabilities
				# Long-term debt
				# Deferred tax liabilities
				# Other long-term liabilities
				# Total non-current liabilities
				"Yearly.totalLiab"							:	fundamentals_base.FundamentalsBase.FINANCIALS,

				# Stockholders' equity
				"Yearly.commonStock"						:	fundamentals_base.FundamentalsBase.FINANCIALS,
				"Yearly.retainedEarnings"					:	fundamentals_base.FundamentalsBase.FINANCIALS,
				"Yearly.otherStockholderEquity"				:	fundamentals_base.FundamentalsBase.FINANCIALS,
				"Yearly.totalStockholderEquity"				:	fundamentals_base.FundamentalsBase.FINANCIALS,


				#  - Cash Flow

				## BUFFETOLOGY
				##	-- Time for earnings
				"Quarterly.currentEarningsDates"			:	fundamentals_base.FundamentalsBase.FINANCIALS,

				#-- Historic Earnings per share
				"Quarterly.historicEarningsEPSDate"			:	fundamentals_base.FundamentalsBase.FINANCIALS,
				"Quarterly.historicEarningsEPS"				:	fundamentals_base.FundamentalsBase.FINANCIALS,

				#-- Historic Earnings
				"Quarterly.historicEarningsDate"			:	fundamentals_base.FundamentalsBase.FINANCIALS,
				"Quarterly.historicEarningsEarnings"		:	fundamentals_base.FundamentalsBase.FINANCIALS,
				"Quarterly.historicEarningsRevenue"			:	fundamentals_base.FundamentalsBase.FINANCIALS,

				#-- Historic Earnings
				"Yearly.historicEarningsDate"				:	fundamentals_base.FundamentalsBase.FINANCIALS,
				"Yearly.historicEarningsEarnings"			:	fundamentals_base.FundamentalsBase.FINANCIALS,
				"Yearly.historicEarningsRevenue"			:	fundamentals_base.FundamentalsBase.FINANCIALS,

				# DEMO
				#"demo"			:	fundamentals_base.FundamentalsBase.FINANCIALS,
				#"demo"			:	fundamentals_base.FundamentalsBase.FINANCIALS,
				#"demo"			:	fundamentals_base.FundamentalsBase.FINANCIALS,
				#"demo"			:	fundamentals_base.FundamentalsBase.FINANCIALS,
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
