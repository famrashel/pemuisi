import os
import sys
import time
import argparse

###############################################################################

__author__ = 'Fam Rashel <fam.rashel@gmail.com>'

__date__, __version__ = '22/03/2021', '0.1' # Creation

__description__ = 'The main program for pemuisi'

__verbose__ = False		# Gives information about timing, etc. to the user.
__trace__ = False		# To be used by the developper for debugging.

###############################################################################

def read_argv():

	this_version = 'v%s (c) %s %s' % (__version__, __date__.split('/')[2], __author__)
	this_description = __description__
	this_usage = """
	%(prog)s  <  TEXT_FILE
	"""

	parser = argparse.ArgumentParser(description=this_description, usage=this_usage, epilog=this_version)
	parser.add_argument('-r', '--ratio',
                  action='store', dest='ratio', type=float, default=0.5,
                  help='ratio between keywords and poetic words')
	parser.add_argument('-V', '--verbose',
                  action='store_true', dest='verbose', default=False,
                  help='runs in verbose mode')
	parser.add_argument('-t', '--trace',
                  action='store_true', dest='trace', default=False,
                  help='runs in tracing mode')
	parser.add_argument('-T', '--test',
                  action='store_true', dest='test', default=False,
                  help='run all unitary tests')
						
	return parser.parse_args()

def convert_time(duration):
	"""
	Convert time data (s) to human-friendly format
	"""
	m, s = divmod(round(duration), 60)
	h, m = divmod(m, 60)
	hms = "%d:%02d:%02d" % (h, m,s)
	return hms

###############################################################################
def _test():
	import doctest
	doctest.testmod()
	sys.exit(0)

def main(file=sys.stdin):
	# Reading from stdin and preprocess the text
	text = [ line.strip() for line in file ]

	# Generate the poetry

if __name__ == '__main__':
	options = read_argv()
	if options.test:
		_test()

	t_start = time.time()
	main(sys.stdin)
	if options.verbose: print(f'# {os.path.basename(__file__)} - Processing time: {(convert_time(time.time() - t_start))}', file=sys.stderr)