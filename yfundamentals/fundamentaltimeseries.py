# Financials
import logging

from common import json_api

class FundamentalTimeSeries (json_api.JSONAPI):

	URL = "https://query2.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/timeseries/{sym}?lang=en-GB&region=GB&symbol={sym}&merge=false&period1={startTime}&period2={timeNow}&corsDomain=uk.finance.yahoo.com&padTimeSeries=true&type=quarterlyBasicEPS%2CquarterlyDilutedAverageShares%2CquarterlyNetIncomeCommonStockholders%2CquartetlyTotalRevenue%2CquarterlyCostOfRevenue%2CquarterlyGrossProfit%2CquarterlyTotalAssets%2CquarterlyTotalLiab%2CquarterlyNetIncomeApplicableToCommonShares%2CquarterlyCommonStock%2CquarterlyRetainedEarnings%2CquarterlyTotalStockholderEquity%2CquarterlyTotalReturnOnEquity"

	jsonMAP = { \
				"Quarterly.Dates"	:	"""timeseries.result[*].quarterlyBasicEPS[*].asOfDate""", #might be backwards
				"Quarterly.BasicEPS"	:	"""timeseries.result[*].quarterlyBasicEPS[*].reportedValue.raw""", #might be backwards
			}

	def __init__(self, symbol):
		super(FundamentalTimeSeries, self).__init__(self.URL, symbol)
		self.logger		=	logging.getLogger('FundamentalTimeSeries')

	def __del__(self):
		super(FundamentalTimeSeries, self).__del__()
