def main():
	
	n = int(input("Enter number of dices:"))
	a = int(input("Enter sum:"))
	t = []
	rollDice(n,t,a)

	print("Number of function calls:",calls)

calls = 0

def rollDice(n,t,a):

	global calls

	calls += 1

	if n == 0:
		if sum(t) == a:
			print(tuple(t))
	else:

		for i in range(1,7):
			
				t.append(i)
				rollDice(n-1,t,a)
				t.pop()

main()