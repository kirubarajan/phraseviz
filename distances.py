import numpy as np

def hamming(string1, string2):
	diffs = 0
	for c1, c2 in zip(string1, string2):
		if ch1 != ch2:
			diffs += 1
	return diffs


def euclidean(string1, string2):
	dist = 0
	for c1, c2 in zip(string1, string2):
		dist += np.linalg.norm(c1, c2)
	return dist


def manhattan(string1, string2):
	return 0

if __name__ == "__main__":
	s1 = "Hello"
	s2 = "Hullo"

	res = hamming(s1, s2)
	print(res)