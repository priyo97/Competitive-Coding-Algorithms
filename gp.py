'''
1 1 3 2 9 4 27 8 81 16 243 32 729 64 2187 128
The above sequance consists of 2 GP series
Find the GP series upto n number of terms
'''

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
