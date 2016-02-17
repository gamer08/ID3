
import sys;
import os;
import random;
from random import randint;
from datetime import datetime;

if __name__ == '__main__':
	if (len(sys.argv) != 4):
		print("usage: " + sys.argv[0] + " inputfile outputfile keep");
		sys.exit(1);

	random.seed(datetime.now());
	inputfile = open(sys.argv[1], "rt");
	outputfile = open(sys.argv[2], "wt");
	keep=sys.argv[3];

	try:
		for i in range(20):
			outputfile.write(inputfile.readline());

	except (EOFError, IOError, IndexError) as e:
		print("Error end of file before " + str(20) + " lines (" + e + ")");
		sys.exit(1);

	try:
		while True:
			line = inputfile.readline();
			if line is None or line == '':
				break;
			if line.endswith("normal.\n") or line.endswith(keep + ".\n"):
				outputfile.write(line);
			

	except (EOFError, IOError, IndexError) as e:
		pass;
	print("Done !");
