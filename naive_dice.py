def main():
	
	n = int(input("Enter number of dices:"))
	t = []
	rollDice(n,t)

	print("Number of function calls:",calls)


calls = 0

def rollDice(n,t):

	global calls

	calls += 1

	if n == 0:
		print(tuple(t))
	else:

		for i in range(1,7):
			
				t.append(i)
				rollDice(n-1,t)
				t.pop()

main()