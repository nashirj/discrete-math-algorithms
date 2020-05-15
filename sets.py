def generate_power_set(elements):
    power_set = []
    for counter in range(2**(len(elements))):
        subset = []
        for j in range(len(elements)):
            # I got inspiration for this line from geeks for geeks
            # https://www.geeksforgeeks.org/power-set/
            if ((counter & (1 << j)) > 0):
                subset.append(elements[j])
        power_set.append(subset)

    return power_set


def generate_cartesian_product_n_elements(n):
    elements = []
    for i in range(1,n+1):
        for j in range(1,n+1):
            elements.append((i, j))

    return elements
