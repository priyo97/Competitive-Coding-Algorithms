def bfs(s,graph,visited,prev):

	q = [s]

	visited[s] = True

	while q:

		t = q.pop(0)
		neighbours = graph[t]

		for i,j in enumerate(neighbours):

			if j and not visited[i]:
				q.append(i)
				visited[i] = True
				prev[i] = t



def findPath(s,e,prev):

	t = e
	path = []

	while t != None:
		
		path.append(t)
		t = prev[t]

	path.reverse()

	if path[0] == s:
		print(path)
	else:
		print("No path")



def main():
	graph = (
			(0,1,1,0,0,0),
			(1,0,0,1,1,0),
			(1,0,0,0,1,0),
			(0,1,0,0,1,1),
			(0,1,1,1,0,1),
			(0,0,0,1,1,0)
		)

	n = int(input("Enter Number of Vertices:"))
	s = int(input("Enter starting vertex:"))

	visited = [False]*n
	prev = [None]*n

	
	bfs(s,graph,visited,prev)

	e = int(input("Enter ending vertex:"))

	findPath(s,e,prev)

main()
