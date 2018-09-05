drinks = 999
a = None

def main():

	N = int(input("Enter number of drinks:"))
	C = int(input("Enter number of customers:"))

	d = [[int(x) for x in input().split()] for _ in range(C)]

	s = list(set([j for i in d for j in i]))

	chosen = []

	combination(s,chosen,d,len(s))

	print(drinks)
	print(a)



def combination(s,chosen,d,n):

	global drinks
	global a

	if n == 0:

		m = set(chosen)

		for i in d:

			if not set(i).intersection(m):

				break
		else:

			l = len(m)

			if l < drinks:

				drinks = l
				a = m			
	else:

		c = s[0]

		s.pop(0)

		chosen.append(c)

		combination(s,chosen,d,n-1)

		
		chosen.pop()

		combination(s,chosen,d,n-1)

		s.insert(0,c)

main()
