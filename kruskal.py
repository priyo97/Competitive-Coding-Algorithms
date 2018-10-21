def getParent(e,s):

	while e != s[e]:

		e = s[e]

	return e



def main():

	edges = [(0,1,4),(0,7,8),(1,2,8),
	(1,7,11),(2,8,2),(2,5,4),(2,3,7),
	(3,5,14),(3,4,9),(4,5,10),(5,6,2),
	(6,7,1),(6,8,6),(7,8,7)]


	s = {i:i for i in range(9)}


	edges.sort(key=lambda x:x[2])


	print(edges)

	total = 0

	for e in edges:

		p1 = getParent(e[0],s)
		p2 = getParent(e[1],s)

		if p1 != p2:

			s[p1] = p2
			total += e[2]


	print(total)

main()