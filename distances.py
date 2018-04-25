import math

class SenLen(object):
	def __init__(self, a):
		self.val = len(a)

	def __ne__(a, b):
		return a.val != b.val

	def __sub__(a, b):
		return a.val - b.val

	def __gr__(a, b):
		return a.val > b.val

	def maxi(self, a):
		if self.val > a.val:
			return self.val
		return a.val

	def __str__(self):
		return '%d' % self.val


def hamming(string1, string2):
	diffs = 0
	s1 = SenLen(string1)
	s2 = SenLen(string2)
	if s1 != s2:
		diffs += abs(s1 - s2)

	for c1, c2 in zip(string1, string2):
		if c1 != c2:
			diffs += 1

	return 1 - (diffs / s1.maxi(s2))


def euclidean(string1, string2):
	dist = 0
	s1 = SenLen(string1)
	s2 = SenLen(string2)
	temp1 = [ord(char) for char in string1]
	temp2 = [ord(char) for char in string2]

	i = abs(len(temp1) - len(temp2))
	if len(temp1) > len(temp2):
		for x in range(i):
			temp2.append(ord('a'))
	else:
		for x in range(i):
			temp1.append(ord('a'))

	res = math.sqrt(sum((t1 - t2) ** 2 for t1, t2 in zip(temp1, temp2)))
	max_distance = 26 * s1.maxi(s2)

	return 1 - (res / max_distance)


def manhattan(string1, string2):
	s1 = SenLen(string1)
	s2 = SenLen(string2)
	temp1 = [ord(char) for char in string1]
	temp2 = [ord(char) for char in string2]

	i = abs(len(temp1) - len(temp2))
	if len(temp1) > len(temp2):
		for x in range(i):
			temp2.append(ord('a'))
	else:
		for x in range(i):
			temp1.append(ord('a'))

	res = sum(abs(t1 - t2) for t1, t2 in zip(temp1, temp2))
	max_distance = 26 * s1.maxi(s2)

	return 1 - (res / max_distance)

if __name__ == "__main__":
	a = "americans"
	b = "america"

	res1 = hamming(a, b)
	print(res1)

	res2 = euclidean(a, b)
	print(res2)

	res3 = manhattan(a, b)
	print(res3)

	pass