# include functions to compute vals
import bell
import catalan
import combinatorics
import fib
import relations
import sets

# First item in value is function, second is documentation (png)
all_functions = {
    'Bell numbers' : [bell.bell_dp, 'bell_doc.png'],
    'Catalan numbers' : [catalan.catalan_dp, None],
    'Fibonacci numbers' : [fib.fibonacci_dp, 'fib_doc.png'],
    'n choose k' : [combinatorics.n_choose_k, None],
    'n pick k' : [combinatorics.n_pick_k, None],
    'n choose k repetition allowed' : [combinatorics.n_choose_k_repetition_allowed, None],
    'n pick k repetition allowed' : [combinatorics.n_pick_k_repetition_allowed, None],
    'generate permutations of a string' : [combinatorics.generate_permutations, None],
    'generate all bit strings of length n' : [combinatorics.generate_bit_strings_of_length_n, None],
    'number of transitive relations' : [relations.count_transitive_relations, None],
    'number of relations' : [relations.count_relations, None],
    'number of reflexive/irreflexive relations' : [relations.count_reflexive_relations, None],
    'number of symmetric relations' : [relations.count_symmetric_relations, None],
    'number of antisymmetric relations' : [relations.count_antisymmetric_relations, None],
    'number of equivalence relations' : [relations.count_equivalence_relations, None],
    'generate power set' : [sets.generate_power_set, None],
    'generate cartesian product' : [sets.generate_cartesian_product, None]
}

functions_with_int_parameters = {
    'Bell numbers' : 1,
    'Catalan numbers' : 1,
    'Fibonacci numbers' : 1,
    'n choose k' : 2,
    'n pick k' : 2,
    'n choose k repetition allowed' : 2,
    'n pick k repetition allowed' : 2,
    'generate all bit strings of length n' : 1,
    'number of transitive relations' : 1,
    'number of relations' : 1,
    'number of reflexive/irreflexive relations' : 1,
    'number of symmetric relations' : 1,
    'number of antisymmetric relations' : 1,
    'number of equivalence relations' : 1
}

function_img = "graphAutos.png"