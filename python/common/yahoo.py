# All Yahoo Data is formatted in the same way
# Shell equivalent
# grep "root.App.main" financials.html | sed 's#root.App.main = ##' | sed 's#;$##g' | python -m json.tool > financials_processed_pretty.json

import logging
import re

from python.http import http_library

class Yahoo (http_library.HTTPLibrary):

	yahooData = re.compile("^.*root.App.main = (?P<json_data>.*);.*$")

	def __init__(self, URL, symbol):
		super(Yahoo, self).__init__(URL, symbol)
		self.logger		=	logging.getLogger('Yahoo')

	def __del__(self):
		super(Yahoo, self).__del__()
		pass

	# def request()
	def parse(self):
		self.logger.debug("%s", self.req.text)
		#TODO: Conver the file into XML
		#TODO: Get the <script> that contains the string in question (root.App.main)
		#data = self.req.text.replace('><', '>\n<')
		#self.logger.info("DATA %s", data)
		# Parse this substring through the regex matcher to get the desired substring
		#reMatch = self.yahooData.match(data)
		#self.logger.info("JSON Match: \"%s\"", reMatch)
		#if (reMatch != None):
		#	jsonData = reMatch.group('json_data')
		#	self.logger.info("JSON Data: \"%s\"", jsonData)
