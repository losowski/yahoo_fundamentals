# Key Statistics

import logging

from ..common import html_wrapped_json

class Statistics (html_wrapped_json.HTMLWrappedJson):

	URL = "https://uk.finance.yahoo.com/quote/{sym}/key-statistics?p={sym}"

	jsonMAP = { \
				#-- Valuation measures
				##-**- Financial Highlights
				"marketCap"					: """context.dispatcher.stores.QuoteSummaryStore.summaryDetail.'marketCap'.raw""",
				"enterpriseValue"			: """context.dispatcher.stores.QuoteSummaryStore.defaultKeyStatistics.'enterpriseValue'.raw""",
				"trailingPE"				: """context.dispatcher.stores.QuoteSummaryStore.summaryDetail.'trailingPE'.raw""",
				"forwardPE"					: """context.dispatcher.stores.QuoteSummaryStore.summaryDetail.'forwardPE'.raw""",
				"pegRatio"					: """context.dispatcher.stores.QuoteSummaryStore.defaultKeyStatistics.'pegRatio'.raw""",

				"priceToSalesTrailing12Months"		: """context.dispatcher.stores.QuoteSummaryStore.summaryDetail.'priceToSalesTrailing12Months'.raw""",
				"priceToBook"				: """context.dispatcher.stores.QuoteSummaryStore.defaultKeyStatistics.'priceToBook'.raw""",
				"enterpriseToRevenue"		: """context.dispatcher.stores.QuoteSummaryStore.defaultKeyStatistics.'enterpriseToRevenue'.raw""",
				"enterpriseToEbitda"		: """context.dispatcher.stores.QuoteSummaryStore.defaultKeyStatistics.'enterpriseToEbitda'.raw""",

				# -- Profitability
				"profitMargins"				: """context.dispatcher.stores.QuoteSummaryStore.defaultKeyStatistics.'profitMargins'.raw""",
				"operatingMargins"			: """context.dispatcher.stores.QuoteSummaryStore.financialData.'operatingMargins'.raw""",

				#-- Management effectiveness (last year)
				"returnOnAssets"			: """context.dispatcher.stores.QuoteSummaryStore.financialData.'returnOnAssets'.raw""",
				"returnOnEquity"			: """context.dispatcher.stores.QuoteSummaryStore.financialData.'returnOnEquity'.raw""",

				#-- Income statement (last year)
				#-- Balance Sheet (last quarter)
				"totalCash"					: """context.dispatcher.stores.QuoteSummaryStore.financialData.'totalCash'.raw""",
				"totalCashPerShare"			: """context.dispatcher.stores.QuoteSummaryStore.financialData.'totalCashPerShare'.raw""",
				"totalDebt"					: """context.dispatcher.stores.QuoteSummaryStore.financialData.'totalDebt'.raw""",
				"debtToEquity"				: """context.dispatcher.stores.QuoteSummaryStore.financialData.'debtToEquity'.raw""",
				"currentRatio"				: """context.dispatcher.stores.QuoteSummaryStore.financialData.'currentRatio'.raw""",
				"bookValue"					: """context.dispatcher.stores.QuoteSummaryStore.defaultKeyStatistics.'bookValue'.raw""",

				#-- Cash flow statement (last year)
				"operatingCashflow"			: """context.dispatcher.stores.QuoteSummaryStore.financialData.'operatingCashflow'.raw""",
				"freeCashflow"				: """context.dispatcher.stores.QuoteSummaryStore.financialData.'freeCashflow'.raw""",

				# -- Share statistics
				"sharesOutstanding"			: """context.dispatcher.stores.QuoteSummaryStore.defaultKeyStatistics.'sharesOutstanding'.raw""",
				"floatShares"				: """context.dispatcher.stores.QuoteSummaryStore.defaultKeyStatistics.'floatShares'.raw""",
				"heldPercentInsiders"		: """context.dispatcher.stores.QuoteSummaryStore.defaultKeyStatistics.'heldPercentInsiders'.raw""",
				"heldPercentInstitutions"	: """context.dispatcher.stores.QuoteSummaryStore.defaultKeyStatistics.'heldPercentInstitutions'.raw""",
				"sharesShort"				: """context.dispatcher.stores.QuoteSummaryStore.defaultKeyStatistics.'sharesShort'.raw""",
				"shortRatio"				: """context.dispatcher.stores.QuoteSummaryStore.defaultKeyStatistics.'shortRatio'.raw""",
				"shortPercentOfFloat"		: """context.dispatcher.stores.QuoteSummaryStore.defaultKeyStatistics.'shortPercentOfFloat'.raw""",
				"sharesPercentSharesOut"	: """context.dispatcher.stores.QuoteSummaryStore.defaultKeyStatistics.'sharesPercentSharesOut'.raw""",
				"sharesShortPriorMonth"		: """context.dispatcher.stores.QuoteSummaryStore.defaultKeyStatistics.'sharesShortPriorMonth'.raw""",
				# DEMO
				#"demo"			: """context.dispatcher.stores.QuoteSummaryStore.defaultKeyStatistics""",
				#"demo"			: """context.dispatcher.stores.QuoteSummaryStore.financialData""",
				#"demo"			: """context.dispatcher.stores.QuoteSummaryStore.summaryDetail""",
			}

	def __init__(self, symbol):
		super(Statistics, self).__init__(self.URL, symbol)
		self.logger		=	logging.getLogger('Statistics')

	def __del__(self):
		super(Statistics, self).__del__()
