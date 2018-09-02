def main():

	p = int(input())

	for n in range(1,p+1):
		if n % 2:
			m = n // 2
			print(3**m,end=" ")
		else:
			m = n // 2 - 1
			print(2**m,end=" ")

main()
