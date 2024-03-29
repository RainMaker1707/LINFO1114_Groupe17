#         A,B,C,D
import numpy as np
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
		[0,0,0,0,0,0,2,5,4,0]]
"""


def Bellman_Ford(mtx):
	sol = []
	for start in range(len(mtx)):
		dist = [float('inf') for _ in range(len(mtx))]
		dist[start] = 0

		# start bellman ford
		# the worst path between two point is n-1 steps
		for _ in range(len(mtx)-1):
			# we go trough each node adjusting the weight of 
			#	every connection it has
			for pivot in range(len(mtx)):
				for node in range(len(mtx)):
					# only ajust if there is a connection between nodes
					if mtx[pivot][node] != 0:
						# ajust for the smalest path
						# since unconected paths have infinite weight,
						# they are absorbant in this operation, and remain infinite
						if dist[node] > dist[pivot] + mtx[pivot][node]:
							dist[node] = dist[pivot] + mtx[pivot][node]
		sol.append(dist)
	return np.array(sol)
