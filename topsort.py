def topsort(g):


	s = []

	n = len(g)

	visited = {}

	stack = []

	for v in g:

		if not visited.get(v,False):
			
			stack.append(v)

			visited[v] = True

			dfs(stack,visited,g,s)

	return s[::-1]



def dfs(stack,visited,g,s):

	while stack:

		current = stack[-1]

		next = univisited_neighbours(g[current],visited)

		if next != None:

			visited[next] = True

			stack.append(next)

		else:

			t = stack.pop()
			s.append(t)
			


def univisited_neighbours(n,visited):

	for i in n:

		if not visited.get(i,False):

			return i
	else:

		return None



def main():

	graph_unsorted = {
					2 : [], 
					5 : [11],
					11: [2, 9, 10],
					7 : [11, 8],
					9 : [],
					10: [],
					8 : [9],
					3 : [10, 8]

					}

	s = topsort(graph_unsorted)

	print(s)


main()
