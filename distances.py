import math

def hamming(string1, string2):
	diffs = 0
	if len(string1) != len(string2):
		diffs += abs(len(string1) - len(string2))

	for c1, c2 in zip(string1, string2):
		if c1 != c2:
			diffs += 1
	return 1 - (diffs / max(len(string1), len(string2)))


def euclidean(string1, string2):
	dist = 0
	temp1 = [ord(char) for char in string1]
	temp2 = [ord(char) for char in string2]

	res = math.sqrt(sum((t1 - t2) ** 2 for t1, t2 in zip(temp1, temp2)))
	max_distance = 26 * max(len(string1), len(string2))

	return 1 - (res / max_distance)


def manhattan(string1, string2):
	temp1 = [ord(char) for char in string1]
	temp2 = [ord(char) for char in string2]

	res = sum(abs(t1 - t2) for t1, t2 in zip(temp1, temp2))
	max_distance = 26 * max(len(string1), len(string2))

	return 1 - (res / max_distance)

if __name__ == "__main__":
	pass