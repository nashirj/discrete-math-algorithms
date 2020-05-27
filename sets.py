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


def generate_cartesian_product(elements):
    res = []
    for i in range(len(elements)):
        for j in range(len(elements)):
            res.append((elements[i], elements[j]))

    return res
