# All Yahoo Data is formatted in the same way
# Shell equivalent
# grep "root.App.main" financials.html | sed 's#root.App.main = ##' | sed 's#;$##g' | python -m json.tool > financials_processed_pretty.json

import logging
import re

from python.http import http_library

class Yahoo (http_library.HTTPLibrary):

	yahooData = re.compile(".*root.App.main = (?P<json_data>(.)+);\s+</script>.*", re.DOTALL)

	def __init__(self, URL, symbol):
		super(Yahoo, self).__init__(URL, symbol)
		self.logger		=	logging.getLogger('Yahoo')
		self.jsonData	=	None


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
				self.jsonData = reMatch.group('json_data')
				self.logger.debug("JSON Data: \"%s\"", self.jsonData)
