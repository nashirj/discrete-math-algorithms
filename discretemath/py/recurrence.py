import numpy as np
import collections

def solve_lin_recurrence_relation(coefficients, base_cases):
	if len(coefficients) != len(base_cases):
		raise ValueError("For a kth degree LHCCRR, need k base cases")
	coeff = coefficients.copy()
	coeff.insert(0, -1)
	coeff = np.multiply(coeff, -1)
	roots = np.roots(coeff)

	if (roots.imag > 10e-6).any():
		raise ValueError("No implementation exists for complex roots of LHCCRR")

	roots = np.round(roots.real,4)
	root_multiplicities = dict()
	for r in roots:
		if r in root_multiplicities:
			root_multiplicities[r] += 1
		else:
			root_multiplicities[r] = 1

	has_repeated_roots = any(c > 1 for c in root_multiplicities.values())
	
	matrix = []
	for i in range(len(base_cases)):
		curr = []
		for root, mult in root_multiplicities.items():
			curr.append(root**i)
			for j in range(1,mult):
				curr.append((root**i)*(i**j))
		matrix.append(np.array(curr))
	
	inv = np.linalg.inv(np.array(matrix))
	base = np.array(base_cases)

	constants = inv.dot(base)

	res = dict()
	i = 0
	for root, mult in root_multiplicities.items():
		res[root] = constants[i:i+mult]
		i += mult

	return res

if __name__ == '__main__':
	# distinct real roots
	coeff = [1,2]
	base = [2,7]
	print(solve_lin_recurrence_relation(coeff,base))

	# repeated real roots
	coeff = [6,-9]
	base = [1,6]
	print(solve_lin_recurrence_relation(coeff,base))

	# higher order w/ distinct real roots
	coeff = [6,-11,6]
	base = [2,5,15]
	print(solve_lin_recurrence_relation(coeff,base))

	# complex real roots
	coeff = [0,-4]
	base = [1,1]
	try:
		print(solve_lin_recurrence_relation(coeff,base))
	except ValueError:
		print("No implementation exists for complex roots of LHCCRR")

	# higher order w/ repeated real roots
	coeff = [-3,-3,-1]
	base = [5,-9,15]
	print(solve_lin_recurrence_relation(coeff,base))

	coeff = [0,7,-6]
	base = [1,3,5]
	print(solve_lin_recurrence_relation(coeff,base))
