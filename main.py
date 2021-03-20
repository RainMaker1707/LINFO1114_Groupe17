"""
Here please type only the code to run the main program with is argument in CLI options
DON T MAKE YOUR FUNCTIONS HERE PLEASE
"""
from scripts.fcts import csv_to_mtx
from scripts.bellmanFord import Bellman_Ford
from scripts.dijkstra import Dijkstra

if __name__ == "__main__":
    def print_mtx(mtx):
        for elem in mtx:
            print(elem)

    C = csv_to_mtx('res/graph.csv')
    import numpy as np
    print(np.array(C))

    print("Dijkstra")
    print(Dijkstra(C))  # print the matrix returned by Dijkstra algorithm
    print('\n\n\n')

    print("Bellman_Ford:")
    print_mtx(Bellman_Ford(C))  # print the matrix returned by Bellman_Ford algorithm
    print('\n\n\n')

    print("Floyd_Warshall:")
    print("WAITING FOR GG")  # print the matrix returned by Floyd_Warshall algorithm
    print('\n\n\n')
