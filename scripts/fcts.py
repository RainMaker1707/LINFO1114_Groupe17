import numpy as np


def csv_to_mtx(path):
	mtx = []
	try:
		with open(path) as file:
			for line in file.readlines():
				mtx.append(line.strip().split(","))
				mtx[-1] = [float(mtx[-1][i]) for i in range(len(mtx[-1]))]
	except FileNotFoundError:
		raise FileNotFoundError("File not found, path tested: '{}'".format(path))
	return np.array(mtx)
