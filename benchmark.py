import sets
import csets
import time

def compare_run_times(functions, args, print_res=True):
    for function in functions:
        t0 = time.time()
        res = function(args)
        if print_res:
            print(res)
        t1 = time.time()
        print(f"Function {function.__name__} took {t1-t0} seconds to run")

def main():
    arg = [i+1 for i in range(4)]
    # functions = [sets.generate_power_set, sets.generate_cartesian_product]
    print("Power set: ")
    compare_run_times([sets.generate_power_set, csets.generate_pset], arg)
    print("\nCartesian product: ")
    compare_run_times([sets.generate_cartesian_product_n_elements, csets.generate_cartesian_product_n_elements], 20000, False)   

if __name__ == '__main__':
    main()
    
