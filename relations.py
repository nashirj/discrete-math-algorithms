import time
import sets
import bell
import combinatorics

def _get_all_pairs_with_same_first_elem(relation, val):
    return [(a, b) for a,b in relation if a == val]

count_trans_doc = 'docs/trans_doc.png'
def count_transitive_relations(n):
    relations = sets.generate_power_set(sets.generate_cartesian_product_n_elements(n))
    num_trans = 0
    for relation in relations:
        processed = []
        transitive = True
        for i in range(len(relation)):
            trans_candidates = _get_all_pairs_with_same_first_elem(relation, relation[i][1])
            if not all([(relation[i][0], cand[1]) in relation for cand in trans_candidates]):
                transitive = False
                break
        num_trans += 1 if transitive else 0

    return num_trans

count_rel_doc = 'docs/rel_doc.png'
def count_relations(n):
    return 2**(n**2)

count_refl_rel_doc = 'docs/refl_rel_doc.png'
def count_reflexive_relations(n):
    return 2**(n*(n-1))

count_sym_rel_doc = 'docs/sym_rel_doc.png'
def count_symmetric_relations(n):
    return 2**((n*(n+1))//2)

count_antisym_rel_doc = 'docs/antisym_rel_doc.png'
def count_antisymmetric_relations(n):
    return (2**n)*(3**(combinatorics.n_choose_k(n,2)))

count_equiv_rel_doc = 'docs/equiv_rel_doc.png'
def count_equivalence_relations(n):
    return bell.bell_dp(n)


def main():
    start_time = time.time()

    n = 7

    print(f"There are {count_relations(n)} relations for a {n} element set")
    print(f"Computing n = {n} took --- {(time.time() - start_time)} seconds ---")

    print(f"There are {count_reflexive_relations(n)} reflexive relations for a {n} element set")
    print(f"Computing n = {n} took --- {(time.time() - start_time)} seconds ---")

    print(f"There are {count_irreflexive_relations(n)} irreflexive relations for a {n} element set")
    print(f"Computing n = {n} took --- {(time.time() - start_time)} seconds ---")

    print(f"There are {count_symmetric_relations(n)} symmetric relations for a {n} element set")
    print(f"Computing n = {n} took --- {(time.time() - start_time)} seconds ---")

    print(f"There are {count_antisymmetric_relations(n)} antisymmetric relations for a {n} element set")
    print(f"Computing n = {n} took --- {(time.time() - start_time)} seconds ---")

    print(f"There are {count_equivalence_relations(n)} equivalence relations for a {n} element set")
    print(f"Computing n = {n} took --- {(time.time() - start_time)} seconds ---")

    # print(f"There are {count_transitive_relations(n)} transitive relations for a {n} element set")
    # print(f"Computing n = {n} took --- {(time.time() - start_time)} seconds ---")



if __name__ == '__main__':
    main()