import inspect # this lets us get function args

# include functions to compute vals
import bell
import catalan
import combinatorics
import fib
import relations
import sets

# TODO: take pic of docs so that they are higher res
# First item in value is function, second is documentation (png)
all_functions = {
    'Bell numbers' : [bell.bell_dp, bell.bell_doc],
    'Catalan numbers' : [catalan.catalan_dp, catalan.catalan_doc],
    'Fibonacci numbers' : [fib.fibonacci_dp, fib.fib_doc],
    'n choose k' : [combinatorics.n_choose_k, combinatorics.comb_no_rep_doc],
    'n pick k' : [combinatorics.n_pick_k, combinatorics.perm_no_rep_doc],
    'n choose k repetition allowed' : [combinatorics.n_choose_k_repetition_allowed, combinatorics.comb_w_rep_doc],
    'n pick k repetition allowed' : [combinatorics.n_pick_k_repetition_allowed, combinatorics.perm_w_rep_doc],
    'generate permutations of a string' : [combinatorics.generate_permutations, None],
    'generate all bit strings of length n' : [combinatorics.generate_bit_strings_of_length_n, None],
    'number of transitive relations' : [relations.count_transitive_relations, relations.count_trans_doc],
    'number of relations' : [relations.count_relations, relations.count_rel_doc],
    'number of reflexive/irreflexive relations' : [relations.count_reflexive_relations, relations.count_refl_rel_doc],
    'number of symmetric relations' : [relations.count_symmetric_relations, relations.count_sym_rel_doc],
    'number of antisymmetric relations' : [relations.count_antisymmetric_relations, relations.count_antisym_rel_doc],
    'number of equivalence relations' : [relations.count_equivalence_relations, relations.count_equiv_rel_doc],
    'generate power set' : [sets.generate_power_set, None],
    'generate cartesian product' : [sets.generate_cartesian_product, None]
}

default_doc = 'docs/default.png'

for item in all_functions:
    args = str(inspect.signature(all_functions[item][0]))[1:-1]
    all_functions[item].append([s.strip() for s in args.split(',')])

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

# TODO: figure out how to not wrap line in the middle of a word
def build_output_string(user_in, function_name, result, time):
    line_length = 60
    result = str(result) if type(result) == int or len(result) == 1 else ', '.join(result)
    i = 0
    new_res = []
    while i < len(result):
        new_res.append(f"{result[i:i+min(len(result), line_length)]}\n")
        i += line_length
    
    out1 = f"For input{'s' if len(user_in) != 1 else ''} {', '.join(user_in)}, {function_name} is"
    out2 = f"Computation took --- {time} seconds ---"
    return f"{out1}\n{''.join(new_res)}{out2}"

def build_error_string(expected_num_params, actual_num_params):
    return f"Expected {expected_num_params} input{'s' if expected_num_params != 1 else ''}, not {actual_num_params} input{'s' if actual_num_params != 1 else ''}"
