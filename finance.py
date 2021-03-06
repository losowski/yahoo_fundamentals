#!/usr/bin/python3
'''
Query Yahoo Finance for specific Symbols
'''
#import
import argparse
import logging

from python.yfundamentals import fundamentals


def main():
	logging.basicConfig(format='%(asctime)s\t%(name)-16s\t%(funcName)-16s\t[%(levelname)-8s] %(message)s', level=logging.INFO)
	logger = logging.getLogger('main')
	blurb = "Query Yahoo Finance for specific Symbols"
	## ARGPARSE
	parser = argparse.ArgumentParser(description = blurb)
	#Model building
	parser.add_argument(dest='symbol', nargs=1, type=str, help='symbol')
	parser.add_argument( dest='param', nargs=1, type=str, help='param')
	parser.add_argument('--debug', dest='debug', type=bool, help='debug', default=False)
	#Get the arguments
	args = parser.parse_args()
	logger.info("Args: %s", args)
	req = fundamentals.Fundamentals(args.symbol[0])
	# Get a specific request
	if (args.param):
		print ("{0}: {1}".format(args.param[0], req[ args.param[0] ]))

	#Generic behaviour
	if (args.debug):
		#test
		req.debug()

# Assign a start point to the executable
if __name__ == "__main__":
	main()

