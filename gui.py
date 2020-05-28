# !/usr/bin/python3
# from tkinter import *
import tkinter as tk
import time

import backend

# display images/documentation about functions
from PIL import ImageTk, Image

top = tk.Tk()
top.attributes("-fullscreen", True)

# Add a grid
mainframe = tk.Frame(top)
mainframe.grid(column=0,row=0, sticky=(tk.N,tk.W,tk.E,tk.S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)

# Create a Tkinter variable
tkvar = tk.StringVar(top)

tkvar.set('<select an option here>') # set the default option

popupMenu = tk.OptionMenu(mainframe, tkvar, *backend.all_functions)
tk.Label(mainframe, text="Choose something to compute").grid(row = 1, column = 1)
popupMenu.grid(row = 2, column =1)

# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get() )

# link function to change dropdown
tkvar.trace('w', change_dropdown)

tk.Label(mainframe, text="Enter comma separated inputs here (i.e. 5, 20)").grid(row=3,column=1)
e1 = tk.Entry(mainframe)
e1.grid(row=4,column=1) # TODO: make this have a label that describes what input arguments are expected

res = tk.Label(mainframe, text="", font=("Monospace", 16), fg='red')
res.grid(row=6,column=1)

def compute():
    # TODO: make function call asynchronous and have a buffering animation while computation is happening with an option to cancel the function
    # TODO: print result from function as a string and have it wrap around if it's too long

    choice = backend.all_functions[tkvar.get()]
    function = choice[0]
    user_in = [foo.strip() for foo in e1.get().split(',')]
    if tkvar.get() in backend.functions_with_int_parameters:
        try:
            args = [int(i) for i in user_in]
        except:
            res.config(text=f"Expected integer inputs, please try again")
            return
        expected_num_params = backend.functions_with_int_parameters[tkvar.get()]
        if len(args) != expected_num_params:
            res.config(text=f"Expected {expected_num_params} input{'s' if expected_num_params != 1 else ''}, not {len(args)} input{'s' if len(args) != 1 else ''}")
            return
        t0 = time.time()
        result = function(*args)
        t1 = time.time()-t0
    else:
        t0 = time.time()
        result = function(args)
        t1 = time.time()-t0
    res.config(text=f"For input{'s' if len(user_in) != 1 else ''} {', '.join(user_in)}, {tkvar.get()} is\n{result}\nComputation took --- {(t1)} seconds ---")

    img_path = choice[1] if choice[1] else 'default.png'
    img = Image.open(img_path)

    zoom = .5

    #multiple image size by zoom
    pixels_x, pixels_y = tuple([int(zoom * x)  for x in img.size])

    img = ImageTk.PhotoImage(img.resize((pixels_x, pixels_y)))
    panel.configure(image=img)
    panel.image = img

img_path = None # "placeholder.png"

img = None # Image.open(img_path)

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(mainframe, image = img)

#The Pack geometry manager packs widgets in rows or columns.
panel.grid(row=7,column=1)

B = tk.Button(mainframe, text = "Compute", command = compute)
B.grid(row=5,column=1)
top.mainloop()







