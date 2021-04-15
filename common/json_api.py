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
		self.logger.info("%s", self.req.text)
		# Convert the HTML string into a series of scripts
	#	scripts = self.req.text.split('<script')
	#	for scr in scripts:
	#		self.logger.debug("Script: %s", scr)
	#		# Check against regex
	#		reMatch = self.yahooData.match(scr)
	#		self.logger.debug("JSON Match: \"%s\"", reMatch)
	#		# If it is a match - store the json in the object
	#		if (reMatch != None):
	#			jMatch = reMatch.group('json_data')
	#			jData = jMatch.replace(';','')
	#			#self.logger.debug("JSON Data: \"%s\"", jsonData)
	#			#print ("{json}".format(json=jsonData))
	#			# Convert the data into a JSON object
	#			self.jsonData = json.loads(jData)
	#			#self.logger.info("jsonData = \"%s\"", self.jsonData.keys())
	#			break


	# Operator[] for get (JSONPath)
	def __getitem__(self, jsonPath):
		return self.get(jsonPath)

	#Get data from JSONPath
	def getJSON(self, jsonPath):
		return None


	#Get Key
	def get(self, key):
		# Get JSON address
		jsonPath = self.jsonMAP.get(key,"")
		self.logger.debug("jsonPath: (\"%s\"): %s:", key, jsonPath)
		return self.getJSON(jsonPath)

