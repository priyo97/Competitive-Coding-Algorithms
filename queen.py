def main():

	n = int(input("Enter size of board:"))

	pos = [-1 for _ in range(n)]

	print(placeQueen(0,n,pos))


def placeQueen(queen,n,pos):

	if queen == n:
		return True

	for j in range(n):

		flag = 0

		for q in range(queen):

			if pos[q] == j or pos[q] + q == j + queen or pos[q] - q == j - queen:
				
				flag = 1
				break

		if not flag:

			pos[queen] = j

			if placeQueen(queen+1,n,pos):
				return True
	else:
		return False


main()
