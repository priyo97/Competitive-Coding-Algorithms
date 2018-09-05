def main():

	l = [x for x in input("Enter elements:").split()]

	chosen = []

	combinations1(l,chosen)

	print("\n\n")

	combinations2(l,chosen,0)


def combinations1(l,chosen):

	if not l:

		print(",".join(chosen))

	else:

		c = l[0]

		l.remove(l[0])

		chosen.append(c)
		combinations1(l,chosen)
		
		chosen.remove(c)
		combinations1(l,chosen)

		l.insert(0,c)



def combinations2(l,chosen,start):

	print(",".join(chosen))

	if start == len(l):

		return

	else:

		for i in range(start,len(l)):
			
			chosen.append(l[i])

			combinations2(l,chosen,i+1)
			
			chosen.remove(l[i])


main()