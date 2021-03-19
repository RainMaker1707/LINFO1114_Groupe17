#         A,B,C,D
"""
graph = [[0,1,3,5,0,0,0,0,0,0],
		 [1,0,2,0,2,0,3,0,0,0],
		 [3,2,0,2,5,4,0,0,0,0],
		 [5,0,2,0,0,4,0,0,2,0],
		 [0,2,0,5,0,5,2,5,0,0],
		 [0,0,4,4,5,0,0,1,5,0],
		 [0,3,0,0,2,0,0,5,0,2],
		 [0,0,0,0,5,1,5,0,5,5],
		 [0,0,0,2,0,5,0,5,0,4],
		 [0,0,0,0,0,0,2,5,4,0]]"""

def Bellman_Ford(mtx):
	sol = []
	for start in range(len(mtx)):
		dist = [99999 for _ in range(len(mtx))]
		dist[start] = 0

		for _ in range(len(mtx)-1):
			for pivot in range(len(mtx)):
				for node in range(len(mtx)):
					if mtx[pivot][node] != 0:
						if dist[node] > dist[pivot] + mtx[pivot][node]:
							print(pivot,node)
							dist[node] = dist[pivot] + mtx[pivot][node]
				sol.append(dist)
	return sol