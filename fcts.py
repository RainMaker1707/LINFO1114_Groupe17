def csv_to_mtx(path):
	mtx = []
	try:
		with open(path) as file:
			for line in file.readlines():
				mtx.append(line.strip().split(","))
				for i in range(len(mtx[-1])):
					mtx[-1][i] = int(mtx[-1][i])
	except:
		pass

	return mtx