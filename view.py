import tkinter as tk
from tkinter.ttk import Progressbar

import controller

import queue # for async stuff
import time

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

        # set the default option
        self.tkvar.set('------')

        self.popupMenu = tk.OptionMenu(self, self.tkvar, *controller.all_functions)
        tk.Label(self, text="Choose something to compute").grid(row = 1, column = 1)
        self.popupMenu.grid(row = 2, column =1)

        # define a callback with write permission to self.tkvar
        self.tkvar.trace('w', self.on_change_dropdown)

        self.default_input_desc = "Enter comma separated inputs (i.e. 5, 20)."
        self.input_description = tk.Label(self, text=self.default_input_desc)
        self.input_description.grid(row=3,column=1)

        self.e1 = tk.Entry(self)
        self.e1.grid(row=4,column=1)

        self.res = tk.Label(self, text="", wraplength=500, fg='blue')
        self.res.grid(row=7,column=1)

        self.img_path = None
        self.img = None
        self.img_zoom = .5

        self.panel = tk.Label(self, image = self.img)

        self.panel.grid(row=8,column=1)

        self.B = tk.Button(self, text = "Compute", command = self.on_click_compute)
        self.B.grid(row=5,column=1)

        self.prog_bar = Progressbar(
            self, orient="horizontal",
            length=200, mode="indeterminate"
        )
        self.prog_bar.grid(row=6, column=1)
        self.prog_bar.grid_forget()

    # on change dropdown value
    def on_change_dropdown(self, *args):
        self.img_path, args = controller.all_functions[self.tkvar.get()][1:3] # [1:3] slices elements at indices 1 and 2
        if self.img_path is None:
            self.img_path = controller.default_doc
        self.img = Image.open(self.img_path)

        #multiple image size by zoom
        pixels_x, pixels_y = tuple([int(self.img_zoom * x)  for x in self.img.size])

        self.img = ImageTk.PhotoImage(self.img.resize((pixels_x, pixels_y)))
        self.panel.configure(image=self.img)
        self.panel.image = self.img

        self.input_description.configure(text=f"{self.default_input_desc} Expected args: {', '.join(args)}")

        self.img_path = controller.all_functions[self.tkvar.get()][1]

        self.res.grid_forget()

    def on_click_compute(self):
        self.res.grid_forget()
        self.prog_bar.grid(row=6, column=1)
        self.B.config(text="Computing")
        self.B.config(state=tk.DISABLED)
        self.prog_bar.start()
        self.queue = queue.Queue()
        
        # TODO: instead of a progress bar, make a buffering animation
        # while computation is happening with an option to cancel the function
        unformatted_input = self.e1.get()
        self.function_name = self.tkvar.get()
        
        try:
            self.user_in, args, function = controller.parse_input(self.function_name, unformatted_input)
        except TypeError:
            self.res.config(text=f"Expected integer inputs, please try again", fg='red')
            return
        except ValueError:
            args = unformatted_input.split(',')
            s = controller.build_error_string(controller.functions_with_int_parameters[self.tkvar.get()], len(args))
            self.res.config(text=s, fg='red')
            return
        
        t0 = time.time()
        if self.function_name in controller.functions_with_int_parameters:
            # result = function(*args)
            controller.ThreadedTask(self.queue, function, [*args], t0).start()
        else:
            if self.function_name in controller.functions_with_list_parameters:
                # result = function(user_in)
                controller.ThreadedTask(self.queue, function, [self.user_in], t0).start()
            else:
                # result = function(user_in[0])
                controller.ThreadedTask(self.queue, function, [self.user_in[0]], t0).start()

        self.master.after(100, self.process_queue)

        # TODO: wrap res in a scrollbar
        # s = controller.build_output_string(user_in, function_name, result, t)
        # self.res.config(text=s, fg='blue')

    def process_queue(self):
        try:
            result, t = self.queue.get(0)
            self.res.grid(row=7,column=1)
            s = controller.build_output_string(self.user_in, self.function_name, result, t)
            self.res.config(text=s)
            self.prog_bar.stop()
            self.prog_bar.grid_forget()
            self.B.config(state=tk.NORMAL)
            self.B.config(text="Compute")
        except queue.Empty:
            self.master.after(100, self.process_queue)

if __name__ == '__main__':
    # Create top level GUI
    top = tk.Tk()
    top.geometry('{}x{}+0+0'.format(*top.maxsize()))
    top.option_add( "*font", "Monospace 16" )

    MainApplication(top)
    top.mainloop()
