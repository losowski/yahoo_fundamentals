# Financials
import logging

from . import financials
from . import statistics


class FundamentalsBase (object):

	FINANCIALS	=	"financials"
	STATISTICS	=	"statistics"

	initMap =	{
					FINANCIALS	:	financials.Financials,
					STATISTICS	:	statistics.Statistics
				}

	def __init__(self, symbol):
		self.logger		=	logging.getLogger('FinancialsBase')
		self.symbol		=	symbol
		self.objMap		=	dict() #KeyName : object

	def __del__(self):
		pass


	# Initialise/return object
	def getRequestObject(self, objectKey):
		self.logger.info("objectKey = %s", objectKey)
		obj = None
		# Check if object exists
		if (objectKey in self.objMap):
			self.logger.info("%s found", objectKey)
			obj = self.objMap[objectKey]
		else:
			self.logger.info("%s NOT found, initialising", objectKey)
			# If not exists, initialise
			fn = self.initMap[objectKey]
			obj = fn(self.symbol)
			# Perform initalisation
			obj.request()
			obj.parse()
		#Fetch the data
		self.objMap[objectKey] = obj
		return obj

	# debug
	def debug(self):
		for init in self.initMap.keys():
			obj = self.getRequestObject(init)
			obj.debug()
