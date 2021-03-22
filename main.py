"""
Here please type only the code to run the main program with is argument in CLI options
DON T MAKE YOUR FUNCTIONS HERE PLEASE
"""
from scripts.fcts import csv_to_mtx
from scripts.bellmanFord import Bellman_Ford
from scripts.dijkstra import Dijkstra

if __name__ == "__main__":
    print('\t**********************\t')
    print('\t\t\tRunning')
    print('\t**********************\t\n')

    C = csv_to_mtx('res/graph.csv')
    print('Costs matrix:\n')
    print(C)
    print("\n\n")

    print("Bellman_Ford:\n")
    print(Bellman_Ford(C))  # print the matrix returned by Bellman_Ford algorithm
    print('\n\n')

    print("Dijkstra:\n")
    print(Dijkstra(C))  # print the matrix returned by Dijkstra algorithm
    print('\n\n')

    print("Floyd_Warshall:\n")
    print("WAITING FOR GG")  # print the matrix returned by Floyd_Warshall algorithm
    print('\n\n\n')
