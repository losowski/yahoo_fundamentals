# Yahoo Timestamps

import logging
import time
import calendar

class TimeStamp:
	def __init__(self):
		self.logger     =   logging.getLogger('Timestamp')
		self.timestamp2010	=	1262304000
		self.timestamp2000	=	946684800
		self.epochNow		=	int(calendar.timegm(time.gmtime()))
		pass

	def __del__(self):
		pass

		
