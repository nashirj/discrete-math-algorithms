import tkinter as tk
import time

# controller logic for view
import backend

# display images/documentation about functions
from PIL import ImageTk, Image

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.grid(column=0,row=0, sticky=(tk.N,tk.W,tk.E,tk.S) )
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)
        self.pack(pady = 100, padx = 100)

        # Create a Tkinter variable
        self.tkvar = tk.StringVar(self.parent)

        self.tkvar.set('------') # set the default option

        self.popupMenu = tk.OptionMenu(self, self.tkvar, *backend.all_functions)
        tk.Label(self, text="Choose something to compute").grid(row = 1, column = 1)
        self.popupMenu.grid(row = 2, column =1)

        # define a callback with write permission to self.tkvar
        self.tkvar.trace('w', self.on_change_dropdown)

        self.default_input_desc = "Enter comma separated inputs (i.e. 5, 20)."
        self.input_description = tk.Label(self, text=self.default_input_desc)
        self.input_description.grid(row=3,column=1)

        self.e1 = tk.Entry(self)
        self.e1.grid(row=4,column=1) # TODO: make this have a label that describes what input arguments are expected

        self.res = tk.Label(self, text="", font=("Monospace", 16), fg='blue')
        self.res.grid(row=6,column=1)

        self.img_path = None
        self.img = None
        self.img_zoom = .5

        self.panel = tk.Label(self, image = self.img)

        self.panel.grid(row=7,column=1)

        self.B = tk.Button(self, text = "Compute", command = self.on_click_compute)
        self.B.grid(row=5,column=1)

    # on change dropdown value
    def on_change_dropdown(self, *args):
        self.img_path, args = backend.all_functions[self.tkvar.get()][1:]
        if self.img_path is None:
            self.img_path = 'default.png'
        self.img = Image.open(self.img_path)

        #multiple image size by zoom
        pixels_x, pixels_y = tuple([int(self.img_zoom * x)  for x in self.img.size])

        self.img = ImageTk.PhotoImage(self.img.resize((pixels_x, pixels_y)))
        self.panel.configure(image=self.img)
        self.panel.image = self.img

        self.input_description.configure(text=f"{self.default_input_desc} Expected args: {', '.join(args)}")

        self.img_path = backend.all_functions[self.tkvar.get()][1]

    def on_click_compute(self):
        # TODO: make function call asynchronous and have a buffering animation while computation is happening with an option to cancel the function
        # TODO: put all this parsing in the backend
        function = backend.all_functions[self.tkvar.get()][0]
        user_in = [arg.strip() for arg in self.e1.get().split(',')]
        if self.tkvar.get() in backend.functions_with_int_parameters:
            try:
                args = [int(i) for i in user_in]
            except:
                self.res.config(text=f"Expected integer inputs, please try again", fg='red')
                return
            if len(args) != backend.functions_with_int_parameters[self.tkvar.get()]:
                s = backend.build_error_string(backend.functions_with_int_parameters[self.tkvar.get()], len(args))
                self.res.config(text=s, fg='red')
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
        s = backend.build_output_string(user_in, self.tkvar.get(), result, t1)
        self.res.config(text=s, fg='blue')

if __name__ == '__main__':
    # Create top level GUI
    top = tk.Tk()
    top.attributes("-fullscreen", True)
    top.option_add( "*font", "Monospace 16" )

    MainApplication(top)
    top.mainloop()
