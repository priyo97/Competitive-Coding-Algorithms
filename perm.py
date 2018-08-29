def permute(l,i,n):

	if i == n:
		permute.count += 1
		# print("".join(l))
	else:
		for j in range(i,n):

			l[i],l[j] = l[j],l[i]
			permute(l,i+1,n)
			# l[i],l[j] = l[j],l[i]


def main():

	s = input("Enter string:")

	l = list(s)

	permute.count = 0

	permute(l,0,len(l))

	print(permute.count)
	
main()