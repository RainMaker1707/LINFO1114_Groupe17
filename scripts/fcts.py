def csv_to_mtx(path):
	mtx = []
	try:
		with open(path) as file:
			for line in file.readlines():
				mtx.append(line.strip().split(","))
				for i in range(len(mtx[-1])):
					mtx[-1][i] = float(mtx[-1][i])
	except FileNotFoundError:
		pass
	return mtx
