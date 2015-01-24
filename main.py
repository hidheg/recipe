
def parse_args(arglist):
	return arglist[1]
	
def print_from_file(input_filename):
	my_file = open(input_filename, "r+")
	print my_file.read()

if __name__ == '__main__':
	# print 'hi'
	import sys
	filename = parse_args(sys.argv)
	print_from_file(filename)