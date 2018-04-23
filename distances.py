import math
import numpy as np

def hamming(string1, string2):
	diffs = 0
	for c1, c2 in zip(string1, string2):
		if c1 != c2:
			diffs += 1
	return diffs


def euclidean(string1, string2):
	dist = 0
	temp1 = [ord(char) for char in string1]
	temp2 = [ord(char) for char in string2]
	for c1, c2 in zip(temp1, temp2):
		dist += (c1 - c2) ** 2
	return math.sqrt(dist)


def manhattan(string1, string2):
	return 0

if __name__ == "__main__":
	s1 = "Helno"
	s2 = "Hullo"

	res1 = hamming(s1, s2)
	print(res1)

	res2 = euclidean(s1, s2)
	print(res2)