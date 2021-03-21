# All Yahoo Data is formatted in the same way
# Shell equivalent
# grep "root.App.main" financials.html | sed 's#root.App.main = ##' | sed 's#;$##g' | python -m json.tool > financials_processed_pretty.json

import logging
import re
import json
import jsonpath_ng

from python.http import http_library

class Yahoo (http_library.HTTPLibrary):

	jsonMAP = {}

	yahooData = re.compile(".*root.App.main = (?P<json_data>(.)+)\s?\}\s?\(this\)\);\s+</script>.*", re.DOTALL)

	def __init__(self, URL, symbol):
		super(Yahoo, self).__init__(URL, symbol)
		self.logger			=	logging.getLogger('Yahoo')
		self.jsonData		=	None


	def __del__(self):
		super(Yahoo, self).__del__()
		pass

	# def request()
	def parse(self):
		#self.logger.debug("%s", self.req.text)
		# Convert the HTML string into a series of scripts
		scripts = self.req.text.split('<script')
		for scr in scripts:
			self.logger.debug("Script: %s", scr)
			# Check against regex
			reMatch = self.yahooData.match(scr)
			self.logger.debug("JSON Match: \"%s\"", reMatch)
			# If it is a match - store the json in the object
			if (reMatch != None):
				jMatch = reMatch.group('json_data')
				jData = jMatch.replace(';','')
				#self.logger.debug("JSON Data: \"%s\"", jsonData)
				#print ("{json}".format(json=jsonData))
				# Convert the data into a JSON object
				self.jsonData = json.loads(jData)
				#self.logger.info("jsonData = \"%s\"", self.jsonData.keys())


	#Get Key
	def get(self, key):
		# Get JSON address
		jsonKey = self.jsonMAP.get(key,"")
		self.logger.debug("jsonkey: \"%s\"", jsonKey)
		#Get json Expression
		jsonExpression = jsonpath_ng.parse(jsonKey)
		# Get the data
		matches = jsonExpression.find(self.jsonData)
		self.logger.info("json: %s (\"%s\"): %s", key, jsonKey, matches)
		# Return only the first value (not using a doc - so expect single values)
		match = None
		if (len(matches)):
			match = [m.value for m in  matches]
		return match

	#debug print
	def debug_print(self, key):
		print ("{0}: {1}".format(key, self.get(key)))

	#debug
	def debug(self):
		pass

