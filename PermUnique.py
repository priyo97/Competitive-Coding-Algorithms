from collections import Counter

def main():

	s = input("Enter string:")

	n = len(s)

	d = Counter(s)

	chosen = []

	permUnique(d,chosen,n)


def permUnique(d,chosen,n):

	if n == 0:

		print(",".join(chosen))

	else:

		for i in d:

			if d[i]:

				d[i] -= 1
				chosen.append(i)

				permUnique(d,chosen,n-1)

				d[i] += 1
				chosen.pop()

main()


