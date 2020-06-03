import inspect # this lets us get function args
import time # get execution time of a method

# include functions to compute vals
from py_modules import catalan, combinatorics, bell, fib, relations, sets

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

functions_with_string_parameters = {
    'generate_permutations'
}

functions_with_list_parameters = {
    'generate power set',
    'generate cartesian product'
}

def build_output_string(user_in, function_name, result, time):
    if type(result) == int:
        result = str(result)
    elif type(result) == list:
        if function_name in functions_with_list_parameters:
            new_res = []
            for r in result:
                new_res.append(f"{{{', '.join(r)}}}")
            result = ', '.join(new_res)
        else:
            result = ', '.join(result)
    
    out1 = f"For input{'s' if len(user_in) != 1 else ''} {', '.join(user_in)}, {function_name} is"
    out2 = f"Computation took --- {time} seconds ---"
    return f"{out1}\n{''.join(result)}\n{out2}"

def build_error_string(exp_num_ps, num_ps):
    exp_inputs = f"input{'s' if exp_num_ps != 1 else ''}"
    actual_inputs = f"input{'s' if num_ps != 1 else ''}"
    return f"Expected {exp_num_ps} {exp_inputs}, not {num_ps} {actual_inputs}"

def parse_input(function_name, unformatted_input):
    function = all_functions[function_name][0]
    user_in = [arg.strip() for arg in unformatted_input.split(',')]
    if function_name in functions_with_int_parameters:
        try:
            args = [int(i) for i in user_in]
        except:
            raise TypeError()
        if len(args) != functions_with_int_parameters[function_name]:
            raise ValueError()
        t0 = time.time()
        result = function(*args)
        t1 = time.time()-t0
    else:
        t0 = time.time()
        if function_name == 'generate power set' or function_name == 'generate cartesian product':
            result = function(user_in)
        else:
            result = function(user_in[0])
        t1 = time.time()-t0
    return user_in, t1, result


