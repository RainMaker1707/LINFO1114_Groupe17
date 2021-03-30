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


def Floyd_Warshall(m):
    mtx = m.copy()
    # Setting the solution matrix
    for k in range(len(mtx)):
        for i in range(len(mtx)):
            for j in range(len(mtx)):
                if i == j:
                    mtx[i][j] = 0
                else:
                    mtx[i][j] = min(mtx[i][j], mtx[i][k] + mtx[k][j])

    return np.array(mtx)
