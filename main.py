"""
Here please type only the code to run the main program with is argument in CLI options
DON T MAKE YOUR FUNCTIONS HERE PLEASE
"""
from scripts.fcts import csv_to_mtx
from scripts.bellmanFord import Bellman_Ford
from scripts.dijkstra import Dijkstra
from datetime import datetime
import argparse


def main(path: str = "res/graph.csv", verbosity: bool = False):
    if verbosity:
        print("\nFile to use: ", path, "\n")  # print the used file is verbosity is active in option
    else:
        print()  # add a blank line in top of file

    C = csv_to_mtx(path)
    print('Costs matrix:\n', C, '\n')  # print the result of the transformation of the file .csv to matrix

    start = datetime.now()  # get time of the algorithm running
    bellman_ford = Bellman_Ford(C)   # running Bellman_Ford algorithm and storing reference in bellman_ford identifier
    stop = datetime.now()  # get the stop time of the algorithm
    print("Bellman_Ford:\n", bellman_ford)  # print the matrix returned by Bellman_Ford algorithm
    if verbosity:
        print("Running time: ", stop - start)  # print the running time of the algorithm if verbosity is active
    print('\n')

    print()
    start = datetime.now()  # get the start time of the algorithm
    dijkstra = Dijkstra(C)  # running Dijkstra algorithm and storing reference in dijkstra identifier
    stop = datetime.now()  # get the stop time of the algorithm
    print("Dijkstra:\n", dijkstra)  # print the matrix returned by Dijkstra algorithm
    if verbosity:
        print("Running time: ", stop - start)  # print the running time of the algorithm if verbosity is active
    print('\n')

    start = datetime.now()  # get the start time of the algorithm
    floyd_warshall = []  # TODO call the algorithm of Floyd-Warshall here
    stop = datetime.now()  # get the stop time of the algorithm
    print("Floyd-Warshall:\n", floyd_warshall)  # print the matrix returned by Floyd_Warshall algorithm
    if verbosity:
        print("Running time: ", stop - start)  # print the running time of the algorithm if verbosity is active


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help="File .csv you want to use as costs graph", type=str)
    parser.add_argument('-v', '--verbose', help="Verbosity", action="store_true")
    args = parser.parse_args()
    if args.verbose:
        print('\t**********************\t')
        print('\t\tRunning')
        print('\t**********************\t\n')

    if not args.file:
        main(verbosity=args.verbose)
    else:
        main(path=args.file, verbosity=args.verbose)
