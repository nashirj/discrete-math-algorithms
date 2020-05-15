import math
# from typing import

def n_choose_k(n,k):
    return math.factorial(n)//(math.factorial(n-k) * math.factorial(k))

def n_pick_k(n,k):
    return math.factorial(n)//math.factorial(n-k)

def n_choose_k_repetition_allowed(n,k):
    return n_choose_k(n+k-1,k)

def n_pick_k_repetition_allowed(n,k):
    return n**k