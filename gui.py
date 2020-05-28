# !/usr/bin/python3
# from tkinter import *
import tkinter as tk
import time

import backend

# display images/documentation about functions
from PIL import ImageTk, Image

# Create top level GUI
top = tk.Tk()
top.attributes("-fullscreen", True)
top.option_add( "*font", "Monospace 16" )

# Add a grid
mainframe = tk.Frame(top)
mainframe.grid(column=0,row=0, sticky=(tk.N,tk.W,tk.E,tk.S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)

# Create a Tkinter variable
tkvar = tk.StringVar(top)

tkvar.set('------') # set the default option

popupMenu = tk.OptionMenu(mainframe, tkvar, *backend.all_functions)
tk.Label(mainframe, text="Choose something to compute").grid(row = 1, column = 1)
popupMenu.grid(row = 2, column =1)

# on change dropdown value
def on_change_dropdown(*args):
    img_path, args = backend.all_functions[tkvar.get()][1:]
    if img_path is None:
        img_path = 'default.png'
    img = Image.open(img_path)

    zoom = .5

    #multiple image size by zoom
    pixels_x, pixels_y = tuple([int(zoom * x)  for x in img.size])

    img = ImageTk.PhotoImage(img.resize((pixels_x, pixels_y)))
    panel.configure(image=img)
    panel.image = img

    input_description.configure(text=f"{default_input_desc} Expected args: {', '.join(args)}")

    img_path = backend.all_functions[tkvar.get()][1]

# define a callback with write permission to tkvar
tkvar.trace('w', on_change_dropdown)

default_input_desc = "Enter comma separated inputs (i.e. 5, 20)."
input_description = tk.Label(mainframe, text=default_input_desc)
input_description.grid(row=3,column=1)

e1 = tk.Entry(mainframe)
e1.grid(row=4,column=1) # TODO: make this have a label that describes what input arguments are expected

res = tk.Label(mainframe, text="", font=("Monospace", 16), fg='blue')
res.grid(row=6,column=1)

def on_click_compute():
    # TODO: make function call asynchronous and have a buffering animation while computation is happening with an option to cancel the function
    # TODO: put all this parsing in the backend

    function = backend.all_functions[tkvar.get()][0]
    user_in = [foo.strip() for foo in e1.get().split(',')]
    if tkvar.get() in backend.functions_with_int_parameters:
        try:
            args = [int(i) for i in user_in]
        except:
            res.config(text=f"Expected integer inputs, please try again", fg='red')
            return
        if len(args) != backend.functions_with_int_parameters[tkvar.get()]:
            s = backend.build_error_string(backend.functions_with_int_parameters[tkvar.get()], len(args))
            res.config(text=s, fg='red')
            return
        t0 = time.time()
        result = function(*args)
        t1 = time.time()-t0
    else:
        t0 = time.time()
        if len(user_in) == 1:
            result = function(user_in[0])
        else:
            result = function(user_in)
        t1 = time.time()-t0
    s = backend.build_output_string(user_in, tkvar.get(), result, t1)
    res.config(text=s, fg='blue')

img_path = None
img = None

panel = tk.Label(mainframe, image = img)

panel.grid(row=7,column=1)

B = tk.Button(mainframe, text = "Compute", command = on_click_compute)
B.grid(row=5,column=1)
top.mainloop()



