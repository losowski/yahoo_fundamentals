#!/usr/bin/python3
'''
Query Yahoo Finance for specific Symbols
'''
#import
import argparse
import logging

from python.statistics import statistics


def main():
	logging.basicConfig(format='%(asctime)s\t%(name)-16s\t%(funcName)-16s\t[%(levelname)-8s] %(message)s', level=logging.INFO)
	logger = logging.getLogger('main')
	blurb = "Query Yahoo Finance for specific Symbols"
	## ARGPARSE
	parser = argparse.ArgumentParser(description = blurb)
	#Model building
	parser.add_argument('--detail', dest='detail', nargs=1, type=str, help='financials, holders, options, statistics')
	parser.add_argument('--symbol', dest='symbol', nargs=1, type=str, help='symbol')
	#Get the arguments
	args = parser.parse_args()
	logger.info("Args: %s", args)
	if (args.detail = 'statistics'):
		s = statistics.Statistics(args.symbol)
	#Generic behaviour
	s.request()
	s.parse()

# Assign a start point to the executable
if __name__ == "__main__":
	main()

