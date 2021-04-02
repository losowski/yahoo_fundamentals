#!/usr/bin/python3
'''
Query Yahoo Finance for specific Symbols
'''
#import
import argparse
import logging
import sys

from python.statistics import statistics
from python.financials import financials

print ("PYTHON_PATH: {0}".format(sys.path))

def main():
	logging.basicConfig(format='%(asctime)s\t%(name)-16s\t%(funcName)-16s\t[%(levelname)-8s] %(message)s', level=logging.INFO)
	logger = logging.getLogger('main')
	blurb = "Query Yahoo Finance for specific Symbols"
	## ARGPARSE
	parser = argparse.ArgumentParser(description = blurb)
	#Model building
	parser.add_argument(dest='detail', nargs=1, type=str, help='financials, holders, options, statistics')
	parser.add_argument(dest='symbol', nargs=1, type=str, help='symbol')
	parser.add_argument('--debug', dest='debug', type=bool, help='debug', default=False)
	#Get the arguments
	args = parser.parse_args()
	logger.info("Args: %s", args)
	req = None
	if (args.detail[0] == 'statistics'):
		logger.info("Statistics: %s", args.symbol[0])
		req = statistics.Statistics(args.symbol[0])
	elif (args.detail[0] == 'financials'):
		logger.info("financials: %s", args.symbol[0])
		req = financials.Financials(args.symbol[0])

	#Generic behaviour
	req.request()
	req.parse()
	if (args.debug):
		#test
		req.debug()

# Assign a start point to the executable
if __name__ == "__main__":
	main()

