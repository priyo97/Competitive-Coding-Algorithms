def GCD(m,n):
	
	'''
	Euclid's Algorithm to find GCD of two numbers using iteration
	'''

	 while n:

		m, n = n, m % n

	return m


def isCoprime(m,n):

	'''
	Modifying the above function to check whether two numbers are coprime or not
	by checking whether the GCD is 1 or not
	'''

	while n:

		m, n = n, m % n

	if m == 1:
		return True
	else:
		return False