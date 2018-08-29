def main():
	n = int(input("Enter number of dices:"))
	a = int(input("Enter sum:"))
	t = []

	rollDice(n,t,0,a)

	print("Number of function calls:",calls)

calls = 0

def rollDice(n,t,sumSoFar,a):

	global calls

	calls += 1

	if n == 0:
		if sumSoFar == a:
			print(tuple(t))
	else:

		for i in range(1,7):
			
			# if count + i + 1*(n-1)<= a and count + i + 6*(n-1) >= a:
			if sumSoFar + i <= a:
				t.append(i)
				rollDice(n-1,t,sumSoFar+i,a)
				t.pop()

main()