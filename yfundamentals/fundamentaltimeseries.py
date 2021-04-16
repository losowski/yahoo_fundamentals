# Financials
import logging

from common import json_api

class FundamentalTimeSeries (json_api.JSONAPI):

	URL = "https://query2.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/timeseries/{sym}?lang=en-GB&region=GB&symbol={sym}&padTimeSeries=true&type=quarterlyEbitda%2CtrailingEbitda%2CquarterlyDilutedAverageShares%2CtrailingDilutedAverageShares%2CquarterlyBasicAverageShares%2CtrailingBasicAverageShares%2CquarterlyDilutedEPS%2CtrailingDilutedEPS%2CquarterlyBasicEPS%2CtrailingBasicEPS%2CquarterlyNetIncomeCommonStockholders%2CtrailingNetIncomeCommonStockholders%2CquarterlyNetIncome%2CtrailingNetIncome%2CquarterlyNetIncomeContinuousOperations%2CtrailingNetIncomeContinuousOperations%2CquarterlyTaxProvision%2CtrailingTaxProvision%2CquarterlyPretaxIncome%2CtrailingPretaxIncome%2CquarterlyOtherIncomeExpense%2CtrailingOtherIncomeExpense%2CquarterlyInterestExpense%2CtrailingInterestExpense%2CquarterlyOperatingIncome%2CtrailingOperatingIncome%2CquarterlyOperatingExpense%2CtrailingOperatingExpense%2CquarterlySellingGeneralAndAdministration%2CtrailingSellingGeneralAndAdministration%2CquarterlyResearchAndDevelopment%2CtrailingResearchAndDevelopment%2CquarterlyGrossProfit%2CtrailingGrossProfit%2CquarterlyCostOfRevenue%2CtrailingCostOfRevenue%2CquarterlyTotalRevenue%2CtrailingTotalRevenue&merge=false&period1={startTime}&period2={timeNow}&corsDomain=uk.finance.yahoo.com"


	# NOTE: Data from this might be backwards
	jsonMAP = { \
				"Quarterly.PretaxIncome"						:	"""timeseries.result[*].quarterlyPretaxIncome[*].reportedValue.raw"""
				"Quarterly.OtherIncomeExpense"					:	"""timeseries.result[*].quarterlyOtherIncomeExpense[*].reportedValue.raw"""
				"Quarterly.CostOfRevenue"						:	"""timeseries.result[*].quarterlyCostOfRevenue[*].reportedValue.raw"""
				"Quarterly.TotalRevenue"						:	"""timeseries.result[*].quarterlyTotalRevenue[*].reportedValue.raw"""
				"Quarterly.DilutedEPS"							:	"""timeseries.result[*].quarterlyDilutedEPS[*].reportedValue.raw"""
				"Quarterly.NetIncomeContinuousOperations"		:	"""timeseries.result[*].quarterlyNetIncomeContinuousOperations[*].reportedValue.raw"""
				"Quarterly.NetIncome"							:	"""timeseries.result[*].quarterlyNetIncome[*].reportedValue.raw"""
				"Quarterly.Ebitda"								:	"""timeseries.result[*].quarterlyEbitda[*].reportedValue.raw"""
				"Quarterly.InterestExpense"						:	"""timeseries.result[*].quarterlyInterestExpense[*].reportedValue.raw"""
				"Quarterly.SellingGeneralAndAdministration"		:	"""timeseries.result[*].quarterlySellingGeneralAndAdministration[*].reportedValue.raw"""
				"Quarterly.OperatingIncome"						:	"""timeseries.result[*].quarterlyOperatingIncome[*].reportedValue.raw"""
				"Quarterly.DilutedAverageShares"				:	"""timeseries.result[*].quarterlyDilutedAverageShares[*].reportedValue.raw"""
				"Quarterly.NetIncomeCommonStockholders"			:	"""timeseries.result[*].quarterlyNetIncomeCommonStockholders[*].reportedValue.raw"""
				"Quarterly.OperatingExpense"					:	"""timeseries.result[*].quarterlyOperatingExpense[*].reportedValue.raw"""
				"Quarterly.BasicAverageShares"					:	"""timeseries.result[*].quarterlyBasicAverageShares[*].reportedValue.raw"""
				"Quarterly.GrossProfit"							:	"""timeseries.result[*].quarterlyGrossProfit[*].reportedValue.raw"""
				"Quarterly.TaxProvision"						:	"""timeseries.result[*].quarterlyTaxProvision[*].reportedValue.raw"""
				"Quarterly.BasicEPS"							:	"""timeseries.result[*].quarterlyBasicEPS[*].reportedValue.raw"""
			}

quarterlyPretaxIncome
quarterlyOtherIncomeExpense
quarterlyCostOfRevenue
quarterlyTotalRevenue
quarterlyDilutedEPS
quarterlyNetIncomeContinuousOperations
quarterlyNetIncome
quarterlyEbitda
quarterlyInterestExpense
quarterlySellingGeneralAndAdministration
quarterlyOperatingIncome
quarterlyDilutedAverageShares
quarterlyNetIncomeCommonStockholders
quarterlyOperatingExpense
quarterlyBasicAverageShares
quarterlyGrossProfit
quarterlyTaxProvision
quarterlyBasicEPS



	def __init__(self, symbol):
		super(FundamentalTimeSeries, self).__init__(self.URL, symbol)
		self.logger		=	logging.getLogger('FundamentalTimeSeries')

	def __del__(self):
		super(FundamentalTimeSeries, self).__del__()
