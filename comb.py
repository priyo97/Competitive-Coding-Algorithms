def main():

	l = [x for x in input("Enter elements:").split()]

	chosen = []

	combinations1(l,chosen)


def combinations1(l,chosen):

	if not l:

		print(chosen)

	else:

		c = l[0]

		l.remove(l[0])

		chosen.append(c)
		combinations(l,chosen)
		
		chosen.remove(c)
		combinations(l,chosen)

		l.insert(0,c)



def combinations2(l,chosen,start):

	print(chosen)

	if start == len(l):

		return

	else:

		for i in range(start,len(l)):
			
			chosen.append(l[i])

			combinations(l,chosen,i+1)
			
			chosen.remove(l[i])


main()