'''
Question youtube link: https://www.youtube.com/watch?v=l_5bPOV7qB8&index=36&t=0s&list=PL3pGy4HtqwD02GVgM96-V0sq4_DSinqvf
'''

def main():

	n = int(input("Enter grid size:"))

	visited = [[False for _ in range(n)] for _ in range(n)]

	Sx, Sy = [int(x) for x in input().split()]
	Tx, Ty = [int(x) for x in input().split()]

	q = [(Sx,Sy)]

	visited[Sx][Sy] = True

	while q:

		t = q.pop(0)

		N = neighbours(t,n)

		for (Nx,Ny) in N:

			if not visited[Nx][Ny]:

				q.append((Nx,Ny))
				visited[Nx][Ny] = True

	print("Target position ",(Tx,Ty)," reached: ",visited[Tx][Ty])


def neighbours(t,r):

	n = []
	x = [0]*8

	x[0] = t[0]+2, t[1]+1
	x[1] = t[0]+2, t[1]-1
	x[2] = t[0]-2, t[1]+1
	x[3] = t[0]-2, t[1]-1
	x[4] = t[0]+1, t[1]+2
	x[5] = t[0]+1, t[1]-2
	x[6] = t[0]-1, t[1]+2
	x[7] = t[0]-1, t[1]-2


	for i in range(8):
		if 0 <= x[i][0] < r and 0 <= x[i][1] < r:
			n.append(x[i])

	return n

main()
