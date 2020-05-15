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

def generate_permutations(s, repetition_allowed):
    strs = []
    _generate_permutations(len(s), list(s), 0, strs, list(s), repetition_allowed)
    strs.sort()

    # if char_set has duplicates or repetititon allowed, remove duplicates
    if len(s) != len(set(s)) or repetition_allowed:
        strs = list(set(strs))

    return strs
    
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