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

def _generate_all_bit_strings_of_length_n(n, s, pos, strs, char_set=['0','1']):
    if pos == n:
        strs.append("".join(s))
        return
    
    for c in char_set:
        s[pos] = c
        _generate_all_bit_strings_of_length_n(n, s, pos+1, strs)
    
def generate_all_bit_strings_of_length_n(n):
    strs = []
    s = ['0']*n
    # this operates on strs
    _generate_all_bit_strings_of_length_n(n, s, 0, strs)
    return strs

def generate_all_permutations_with_char_set(n, char_set):
    pass

def generate_all_permutations(s):
    pass

def main():
    # generate bit strings of length n
    n = 5
    strs = generate_all_bit_strings_of_length_n(n)
    for s in strs:
        print(s)


if __name__ == '__main__':
    main()