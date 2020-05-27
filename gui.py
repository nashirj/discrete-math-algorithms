# !/usr/bin/python3
# from tkinter import *
import tkinter as tk

# include functions to compute vals
import bell
import catalan
import combinatorics
import fib
import relations
import sets


top = tk.Tk()
top.geometry("600x400")

# Add a grid
mainframe = tk.Frame(top)
mainframe.grid(column=0,row=0, sticky=(tk.N,tk.W,tk.E,tk.S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)

# Create a Tkinter variable
tkvar = tk.StringVar(top)

# Dictionary with options
choices = {
    'Bell numbers' : bell.bell_dp,
    'Catalan numbers' : catalan.catalan_dp,
    'Fibonacci numbers' : fib.fibonacci_dp,
    'n choose k' : combinatorics.n_choose_k,
    'n pick k' : combinatorics.n_pick_k,
    'n choose k repetition allowed' : combinatorics.n_choose_k_repetition_allowed,
    'n pick k repetition allowed' : combinatorics.n_pick_k_repetition_allowed,
    'generate permutations of a string' : combinatorics.generate_permutations,
    'generate all bit strings of length n' : combinatorics.generate_bit_strings_of_length_n,
    'number of transitive relations' : relations.count_transitive_relations,
    'number of relations' : relations.count_relations,
    'number of reflexive/irreflexive relations' : relations.count_reflexive_relations,
    'number of symmetric relations' : relations.count_symmetric_relations,
    'number of antisymmetric relations' : relations.count_antisymmetric_relations,
    'number of equivalence relations' : relations.count_equivalence_relations,
    'generate power set' : sets.generate_power_set,
    'generate cartesian product' : sets.generate_cartesian_product_n_elements
    }
tkvar.set('<select an option here>') # set the default option

popupMenu = tk.OptionMenu(mainframe, tkvar, *choices)
tk.Label(mainframe, text="Choose something to compute").grid(row = 1, column = 1)
popupMenu.grid(row = 2, column =1)

# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get() )

# link function to change dropdown
tkvar.trace('w', change_dropdown)


tk.Label(mainframe, text="Enter comma separated inputs here (i.e. 5, 20)").grid(row=3,column=1)
e1 = tk.Entry(mainframe)
e1.grid(row=4,column=1)

res = tk.Label(mainframe, text="")
res.grid(row=6,column=1)

def compute():
    function = choices[tkvar.get()]
    args = e1.get().split(',')
    args = [int(i) for i in args]
    result = function(*args)
    res.config(text=f"result is {result}")

B = tk.Button(mainframe, text = "Compute", command = compute)
B.grid(row=5,column=1)
top.mainloop()




# master.mainloop()