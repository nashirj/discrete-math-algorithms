import numpy as np


def solve_lin_recurrence_relation(coefficients, base_cases):
	if len(coefficients) != len(base_cases):
		raise ValueError("For an nth degree LHCCRR, need n base cases")
	coeff = coefficients.copy()
	coeff.insert(0, -1)
	coeff = np.multiply(coeff, -1)
	roots = np.roots(coeff)

	matrix = []
	for i in range(len(base_cases)):
		matrix.append(np.power(roots, i))

	inv = np.linalg.inv(np.array(matrix))
	base = np.array(base_cases)

	res = inv.dot(base)
	ret = []
	for i in range(len(res)):
		ret.append((res[i], roots[i]))

	return ret
