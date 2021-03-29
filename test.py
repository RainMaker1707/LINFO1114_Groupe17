import unittest
from scripts.dijkstra import Dijkstra
from scripts.bellmanFord import Bellman_Ford
from scripts.fcts import csv_to_mtx
from os import system


def run_test():
    system('python3 test.py')


class TestDijkstra(unittest.TestCase):
    def all_tests(self):
        self.test_dijkstra()
        self.test_dijkstra_bad_matrix()
        self.test_dijkstra_two_same_path()
        self.test_dijkstra_one_disjoint_point()
        self.test_dijkstra_disjoint_points()

    def test_dijkstra(self):
        self.assertEqual(0, 0)
        return 1

    def test_dijkstra_bad_matrix(self):
        return 1

    def test_dijkstra_two_same_path(self):
        return 1

    def test_dijkstra_one_disjoint_point(self):
        return 1

    def test_dijkstra_disjoint_points(self):
        return 1


class TestBellmanFord(unittest.TestCase):
    def test_bellman_ford(self):
        return 1

    def test_bellman_ford_bad_matrix(self):
        return 1

    def test_bellman_ford_one_disjoint_point(self):
        return 1

    def test_bellman_ford_disjoint_points(self):
        return 1


class TestFloydWarshall(unittest.TestCase):
    def test_floyd_warshall(self):
        return 1

    def test_floyd_warshall_bad_matrix(self):
        return 1

    def test_floyd_warshall_one_disjoint_point(self):
        return 1

    def test_floyd_warshall_disjoint_points(self):
        return 1


if __name__ == "__main__":
    unittest.main()
