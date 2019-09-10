import codecs
import random
import sys

if __name__ == "__main__":
	# print(sys.getdefaultencoding())
	# print(sys.getdefaultencoding()=="utf-8")

	start = int(input("Start row:"))
	end = int(input("End row:  "))

	dFile = "hiragana.txt"

	f = codecs.open(dFile, "r", "utf-8")
	linesArray = f.readlines()
	charArray = []
	for i in range(start-1, end):
		subCharArray = linesArray[i].rstrip().split("\t")[1:]
		for char in subCharArray:
			charArray.append(char)

	charArray = charArray * 5
	random.shuffle(charArray)
	charArray = charArray[:int(len(charArray)*4/5)]
	# print("".join(charArray))

	size = 10
	iArray = [[x,x+size] for x in range(0,len(charArray),size)]

	for each in iArray:
		print("\n", "".join(charArray[each[0]:each[1]]), "\n")

	f.closed
