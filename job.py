# from time import time

# def main():
# 	n         = int(input("Enter number of jobs:"))
# 	profits   = [int(p) for p in input("Enter profits:").split()]
# 	deadlines = [int(d) for d in input("Enter deadlines:").split()]

# 	s = time()
# 	jobs      = list(zip(range(n),profits,deadlines))

# 	jobs.sort(key=lambda x:x[1],reverse=True)

# 	slots = max(deadlines)

# 	schedule = [False]*(slots+1)

# 	for j in jobs:
# 		i = j[2]
		
# 		while i:
# 			if not schedule[i]:
# 				schedule[i] = j
# 				break

# 			i-=1

# 	print(schedule)
# 	print("time taken:"+str(time()-s))

# main()


a = [1,2,3,4]

for i in range(len(a)):
	for j in range(len(a)):
		if i!=j:
			a[i],a[j] = a[j],a[i]
		print(a)













