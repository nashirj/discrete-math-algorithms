'''
Provide operations on sets, including generation of power set and cartesian product
    given a list of elements and the cartesian product of an n element set.
'''

gen_pset_doc = 'docs/gen_pset_doc.png'
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

gen_cart_prod_doc = 'docs/gen_cart_prod_doc.png'
def generate_cartesian_product(set1, set2=None):
    res = []
    if not set2:
        set2 = set1.copy()
    for i in range(len(set1)):
        for j in range(len(set2)):
            res.append((set1[i], set2[j]))

    return res


def generate_cartesian_product_n_elements(n):
    elements = [i for i in range (1,n+1)]
    return generate_cartesian_product(elements)
