# All HTMLWrappedJson Data is formatted in the same way
# Shell equivalent
# grep "root.App.main" financials.html | sed 's#root.App.main = ##' | sed 's#;$##g' | python -m json.tool > financials_processed_pretty.json

import logging
import re
import json
import jsonpath_ng

from common import http_library

class JSONAPI (http_library.HTTPLibrary):

	jsonMAP = {}

	def __init__(self, URL, symbol):
		super(JSONAPI, self).__init__(URL, symbol)
		self.logger			=	logging.getLogger('JSONAPI')
		self.jsonData		=	None


	def __del__(self):
		super(JSONAPI, self).__del__()
		pass

	# def request()
	def parse(self):
		self.logger.debug("%s", self.req.text)
		#Convert into a JSON object
		self.jsonData = json.loads(self.req.text)


	# Operator[] for get (JSONPath)
	def __getitem__(self, jsonPath):
		return self.get(jsonPath)

	#Get data from JSONPath
	def getJSON(self, jsonPath):
		if ((jsonPath is None) or (jsonPath == "")):
			self.logger.warning("Empty jsonPath Key")
			return list()
		#Get json Expression
		jsonExpression = jsonpath_ng.parse(jsonPath)
		# Get the data
		matches = jsonExpression.find(self.jsonData)
		self.logger.debug("json: %s: %s", jsonPath, matches)
		match = None
		if (len(matches)):
			match = [m.value for m in  matches]
		return match


	#Get Key
	def get(self, key):
		# Get JSON address
		jsonPath = self.jsonMAP.get(key,"")
		self.logger.debug("jsonPath: (\"%s\"): %s:", key, jsonPath)
		return self.getJSON(jsonPath)

