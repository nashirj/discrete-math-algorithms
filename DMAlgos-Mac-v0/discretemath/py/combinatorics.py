'''
Provide functions to count combinations with and without repetition, permutations
    with and without repetition, generate permutations of a string, and generate
    all bit strings of length n.
'''

import math

comb_no_rep_doc = 'docs/comb_no_rep_doc.png'
def n_choose_k(n,k):
    if n <= k:
        return 1
    return math.factorial(n)//(math.factorial(n-k) * math.factorial(k))

perm_no_rep_doc = 'docs/perm_no_rep_doc.png'
def n_pick_k(n,k):
    if n < k:
        return 1
    return math.factorial(n)//math.factorial(n-k)

comb_w_rep_doc = 'docs/comb_w_rep_doc.png'
def n_choose_k_repetition_allowed(n,k):
    if n <= k:
        return 1
    return n_choose_k(n+k-1,k)

perm_w_rep_doc = 'docs/perm_w_rep_doc.png'
def n_pick_k_repetition_allowed(n,k):
    if n < k:
        return 1
    return n**k

def _generate_permutations(n, s, pos, strs, char_set, repetition_allowed):
    if pos == n:
        strs.append("".join(s))
        return

    for i in range(len(char_set)):
        if not repetition_allowed:
            if not char_set[i]:
                continue
            else:
                s[pos] = char_set[i]
                char_set[i] = None
        else:
            s[pos] = char_set[i]
        _generate_permutations(n, s, pos+1, strs, char_set, repetition_allowed)
        char_set[i] = s[pos]

gen_perm_doc = 'docs/gen_perm_doc.png'
def generate_permutations(s):
    strs = []
    _generate_permutations(len(s), list(s), 0, strs, list(s), False)
    strs.sort()

    # if char_set has duplicates or repetititon allowed, remove duplicates
    if len(s) != len(set(s)):
        strs = list(set(strs))

    return strs
    
gen_bstrings_doc = 'docs/gen_bstrings_doc.png'
def generate_bit_strings_of_length_n(n):
    strs = []
    s = ['0']*n
    # this operates on strs
    _generate_permutations(n, s, 0, strs, ['0','1'], True)
    return strs

def main():
    # generate bit strings of length n
    n = 5
    strs = generate_bit_strings_of_length_n(n)
    for s in strs:
        print(s)

    strs = generate_permutations('blegh', False)
    for s in strs:
        print(s)

    strs = generate_permutations('needy', False)
    for s in strs:
        print(s)


if __name__ == '__main__':
    main()