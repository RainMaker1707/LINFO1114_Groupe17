"""
Here please type only the code to run the main program with is argument in CLI options
DON T MAKE YOUR FUNCTIONS HERE PLEASE
"""
from scripts.fcts import csv_to_mtx
from scripts.bellmanFord import Bellman_Ford

if __name__ == "__main__":
    def print_mtx(mtx):
        for elem in mtx:
            print(elem)


    print_mtx(Bellman_Ford(csv_to_mtx('res/graph.csv')))
