import time
import binomial

def catalan_recursive(n):
    if n < 0:
        raise ValueError("Expected argument greater than or equal to 0")
    if n == 0 or n == 1:
        return 1

    cn = 0
    for k in range(0, n):
        cn_k = catalan_recursive(n-k-1)
        c_k = catalan_recursive(k)
        cn += cn_k * c_k
    return cn


catalan_vals = [1, 1] # base cases
def catalan_dp(n):
    if n < 0:
        raise ValueError("Expected argument greater than or equal to 0")
    if len(catalan_vals) > n:
        return catalan_vals[n]
    
    cn = 0
    for k in range(0, n):
        cn_k = catalan_vals[n-k-1] if len(catalan_vals) > n-k-1 else catalan_dp(n-k-1)
        c_k = catalan_vals[k] if len(catalan_vals) > k else catalan_dp(k)
        cn += cn_k * c_k
    catalan_vals.append(cn)

    return catalan_vals[n]


def catalan_closed_form(n):
    return binomial.n_choose_k(2*n,n) // (n+1)


def main():
    n = 26
    # t0 = time.time()
    # for i in range(n+1):
    #     print(f"c_{i} = {catalan_recursive(i)}")
    # # I let this run for an hour and it only got to n = 20
    # print(f"Catalan recursive up to and including {n} takes {time.time()-t0} seconds")

    t0 = time.time()
    for i in range(n+1):
        print(f"c_{i} = {catalan_dp(i)}")
    # this takes ~.0006 seconds
    print(f"Catalan dp up to and including {n} takes {time.time()-t0} seconds")

    t0 = time.time()
    for i in range(n+1):
        print(f"c_{i} = {catalan_closed_form(i)}")
    # this takes ~.0003 seconds
    print(f"Catalan closed form up to and including {n} takes {time.time()-t0} seconds")


if __name__ == '__main__':
    main()
