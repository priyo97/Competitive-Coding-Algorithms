def main():

	graph = [
		[1,2] ,
		[0,3,4] ,
		[0,4] ,
		[1,4,5] ,
		[1,2,3,5] ,
		[3,4]
	]

	n = len(graph)

	visited = [False]*n

	s = int(input("Source:"))

	dfs1(s,graph,visited)


vertex = ["A","B","C","D","E","F"]


def dfs1(s,graph,visited):


	print(vertex[s])

	visited[s] = True

	neighbours = graph[s]


	for idx in neighbours:

		if not visited[idx]:

			dfs(idx,graph,visited)


def dfs(at,graph,visited):

	if( visited[at] == True ):
		return

	print(vertex[at])

	visited[at] = True
	neighbours = graph[at]


	for next in neighbours:

		dfs(next,graph,visited)


main()