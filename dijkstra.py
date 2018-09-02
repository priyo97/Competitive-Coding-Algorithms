def main():
	graph = (
				(0, 4, 0, 0, 0, 0, 0, 8, 0),
				(4, 0, 8, 0, 0, 0, 0, 11, 0),
				(0, 8, 0, 7, 0, 4, 0, 0, 2),
				(0, 0, 7, 0, 9, 14, 0, 0, 0),
				(0, 0, 0, 9, 0, 10, 0, 0, 0),
				(0, 0, 4, 14, 10, 0, 2, 0, 0),
				(0, 0, 0, 0, 0, 2, 0, 1, 6),
				(8, 11, 0, 0, 0, 0, 1, 0, 7),
				(0, 0, 2, 0, 0, 0, 6, 7, 0)
			)

	n = int(input("Enter number of vertices:"))

	dist    = [999]*n
	prev    = [None]*n
	visited = [False]*n

	s = int(input("Source:"))
	t = int(input("Target:"))

	computeDistance(s,dist,prev,visited,graph)

	path = findPath(s,t,prev)

	if path:

		print("Distance:",dist)
		print("Path from {} to {}:".format(s,t),path)


def computeDistance(s,dist,prev,visited,graph):

	dist[s] = 0

	for _ in range(len(dist)):

		idx = min_distance(dist,visited)

		visited[idx] = True

		for i,cost in unvisited_neighbours(graph[idx],visited):

			d = dist[idx] + cost

			if d < dist[i]:

				dist[i] = d
				prev[i] = idx 


def min_distance(dist,visited):

	m = 999
	for i,d in enumerate(dist):

		if not visited[i]:
			if d < m:
				m = d
				idx = i

	return idx

def unvisited_neighbours(g,visited):

	return [(idx,cost) for idx,cost in enumerate(g) if cost and not visited[idx]]


def findPath(s,t,prev):

	path = []

	while t != None:

		path.append(t)
		t = prev[t]

	path.reverse()

	if path[0] == s:
		return path
	else:
		return False


main()