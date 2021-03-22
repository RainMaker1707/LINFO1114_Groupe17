import numpy as np


def custom_min_sup(A: (np.ndarray, np.generic), prev_min: float, visited_nodes: list):
    """
    :param A: list L of shortest path current states
    :param prev_min: previous_minimum registered
    :param visited_nodes: list of visited nodes
    :return:
    """
    greater = []
    for i in range(len(A)):
        if i not in visited_nodes:
            if A[i] == prev_min:
                return i
            if A[i] > prev_min:
                greater.append((A[i], i))
    if greater:
        greater.sort()
        return greater[0][1]
    return -1


def Dijkstra(W):
    """
    Return the shortest path between all the vertices by running the dijkstra algorithm several times
    :param W: is the matrix of edges costs
    :return: L matrix of all shortest path between each node
    """
    # check if list is already an numpy array, if not it convert it
    if not isinstance(W, (np.ndarray, np.generic)):
        W = np.array(W)

    W_shape_x, W_shape_y = W.shape  # get shape in var for optimisation (not call it in loop for example)
    # check if matrix is square with a shape of n x n
    if W_shape_x != W_shape_y:
        raise Exception('Matrix of costs must be a n x n square matrix')

    # check if matrix is symmetrical
    if not np.allclose(W, W.T):
        raise Exception('Matrix must be symmetrical')

    # Start of Dijkstra algorithm
    L = np.full(W.shape, float('inf'))  # setup matrix L of all shortest path as infinite and same shape as W
    for i in range(W_shape_x):
        L[i][i] = 0  # setup all shortest path between a node and itself to 0
    for elem in L:
        S = []  # list of visited node
        u = np.where(np.amin(elem) == elem)[0][0]  # first minimum in the line of the L matrix
        while len(elem) != len(S):
            if S:
                u = custom_min_sup(elem, elem[u], S)  # take a vertex u with minimal L(u)
            S.append(u)  # append vertex to visited node list
            for i in range(len(elem)):  # for vertex not in S
                if i not in S:
                    if elem[u] + W[u][i] < elem[i]:  # if L(u) + w(u,v) < L(v)
                        elem[i] = elem[u] + W[u][i]  # L(v) := L(u) + w(u,v)
    return L
