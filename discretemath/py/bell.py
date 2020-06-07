from . import combinatorics
import time

bell_doc = 'docs/bell_doc.png'

def bell_recursive(n):
    if n < 0:
        raise ValueError("Not possible to partition a set with negative # of elements")
    if n == 0 or n == 1:
        return 1
    bn = 0
    for k in range(1, n+1):
        bn_k = bell_recursive(n-k)
        bn += combinatorics.n_choose_k(n-1,k-1) * bn_k
    return bn


bell_vals = [1, 1] # base cases
def bell_dp(n):
    if n < 0:
        raise ValueError("Not possible to partition a set with negative # of elements")
    if n == 0 or n == 1:
        return 1
    if len(bell_vals) > n:
        return bell_vals[n]
    
    bn = 0
    for k in range(1, n+1):
        bn_k = bell_vals[n-k] if len(bell_vals) > n-k else bell_dp(n-k)
        bn += combinatorics.n_choose_k(n-1,k-1) * bn_k
    bell_vals.append(bn)

    return bell_vals[n]


def main():
    n = 26
    # t0 = time.time()
    # for i in range(27):
    #     print(f"b_{i} = {bell_recursive(i)}")
    # this takes ~104 seconds
    # print(f"Bell recursive up to and including {n} takes {time.time()-0} seconds")

    t0 = time.time()
    for i in range(n+1):
        print(f"b_{i} = {bell_dp(i)}")
    # this takes ~.001 seconds
    print(f"Bell dp up to and including {n} takes {time.time()-t0} seconds")


if __name__ == '__main__':
    main()
