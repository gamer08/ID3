
import sys;
import os;
import random;
from random import randint;
from datetime import datetime;

if __name__ == '__main__':
	if (len(sys.argv) != 5):
		print("usage: " + sys.argv[0] + " inputfile outputfile lineToBegin percentToRemove");
		sys.exit(1);

	random.seed(datetime.now());
	inputfile = open(sys.argv[1], "rt");
	outputfile = open(sys.argv[2], "wt");
	skip = 0;
	percentToRemove = 0;
	try:
		skip = int(sys.argv[3]);
		percentToRemove = int(sys.argv[4]);

	except ValueError as e:
		print("Enter integer for lineToBegin and percentToRemove (" + e + ")");

	try:
		for i in range(skip):
			outputfile.write(inputfile.readline());

	except (EOFError, IOError, IndexError) as e:
		print("Error end of file before " + str(skip) + " lines (" + e + ")");
		sys.exit(1);

	try:
		while True:
			line = inputfile.readline();
			if line is None or line == '':
				break;
			if (randint(0,100) > percentToRemove):
				outputfile.write(line);

	except (EOFError, IOError, IndexError) as e:
		pass;
	print("Done !");
