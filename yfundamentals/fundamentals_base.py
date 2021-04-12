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

	reqMap = {}

	def __init__(self, symbol):
		self.logger		=	logging.getLogger('FinancialsBase')
		self.symbol		=	symbol
		self.objMap		=	dict() #KeyName : object

	def __del__(self):
		pass


	# Initialise/return object
	def getRequestObject(self, objectKey):
		self.logger.debug("RequestObject: objectKey = %s", objectKey)
		obj = None
		# Get the relevant object type
		reqKey = self.reqMap.get(objectKey)
		self.logger.debug("reqKey: %s = %s", reqKey, objectKey)
		# Check if object exists
		if (reqKey in self.objMap):
			self.logger.debug("RequestObject:  %s found", objectKey)
			#Fetch the data
			obj = self.objMap[reqKey]
		else:
			self.logger.debug("RequestObject: %s NOT found, initialising", objectKey)
			# If not exists, initialise
			fn = self.initMap[reqKey]
			obj = fn(self.symbol)
			# Perform initalisation
			obj.request()
			obj.parse()
			# Store the object
			self.objMap[reqKey] = obj
		return obj

	# debug
	def debug(self):
		for key in self.reqMap.keys():
			obj = self.getRequestObject(key)
			obj.debug_print(key)
