import numpy as np


def solve_lin_recurrence_relation(coefficients: list, base_cases: list):
	coefficients.insert(0, -1)
	coefficients = np.multiply(coefficients, -1)
	roots = np.roots(coefficients)

	print(f"Coefficients: {coefficients}")
	print(f"Roots: {roots}")

	matrix = []
	for i in range(len(base_cases)):
		matrix.append(np.power(roots, i))

	print(matrix)
	inv = np.linalg.inv(np.array(matrix))
	base = np.array(base_cases)

	res = inv.dot(base)
	ret = []
	for i in range(len(res)):
		ret.append((res[i], roots[i]))

	return ret
	