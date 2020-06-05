# gui
import tkinter as tk
from tkinter.ttk import Progressbar

# backend computation
import controller

# for async stuff
import time
import multiprocessing as mp
import queue
import sys

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

        tk.Label(self, text="Choose something to compute").grid(row = 1, column = 1)
        
        self.popupMenu = tk.OptionMenu(self, self.tkvar, *controller.all_functions)
        self.popupMenu.grid(row = 2, column =1)

        # define a callback with write permission to self.tkvar
        self.tkvar.trace('w', self.on_change_dropdown)

        self.default_input_desc = "Enter comma separated inputs (i.e. 5, 20)."
        self.input_description = tk.Label(self, text=self.default_input_desc)
        self.input_description.grid(row=3,column=1)

        self.e1 = tk.Entry(self)
        self.e1.grid(row=4,column=1)

        self.compute_B = tk.Button(self, text = "Compute", command = self.on_click_compute)
        self.compute_B.grid(row=5,column=1)

        self.cancel_B = tk.Button(self, text = "Stop computation", command = self.on_click_cancel)
        self.cancel_B.grid(row=6,column=1)
        self.cancel_B.grid_forget()

        self.prog_bar = Progressbar(
            self, orient="horizontal",
            length=200, mode="indeterminate"
        )
        self.prog_bar.grid(row=7, column=1)
        self.prog_bar.grid_forget() # only show progress bar during computation

        self.res = tk.Label(self, text="", wraplength=500, fg='blue')
        self.res.grid(row=8,column=1)

        self.img_path = None
        self.img = None
        self.img_zoom = .5

        self.panel = tk.Label(self, image = self.img)

        self.panel.grid(row=9,column=1)

        mp.set_start_method('spawn')
        self.queue = mp.Queue()
        self.py_version_gte_3_7 = sys.version[0] == 3 and sys.version[1] >= 7

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

    def reset_gui(self):
        self.prog_bar.stop()
        self.prog_bar.grid_forget()
        self.compute_B.config(state=tk.NORMAL)
        self.compute_B.config(text="Compute")
        self.cancel_B.grid_forget()

    def on_click_cancel(self):
        self.queue.put(("interrupt",0))
        self.res.config(text="Computation cancelled", fg='red')
        self.reset_gui()

    def on_click_compute(self):
        if self.tkvar.get() == '------':
            return
        self.res.grid_forget()
        self.prog_bar.grid(row=7, column=1)
        self.prog_bar.start()
        self.compute_B.config(text="Computing")
        self.compute_B.config(state=tk.DISABLED)
        self.cancel_B.grid(row=6, column=1)
        
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
            if self.function_name == 'solve LHCCRR':
                s = '''For a kth degree LHCCRR, need k base cases.\nSeparate coefficients and base cases with a semicolon, i.e. "2,3;3,4"'''
            else:
                args = unformatted_input.split(',')
                s = controller.build_error_string(controller.functions_with_int_parameters[self.tkvar.get()], len(args))
            self.res.config(text=s, fg='red')
            self.res.grid(row=8,column=1)
            self.reset_gui()
            return
        
        if self.function_name in controller.functions_with_int_parameters:
            args = [*args]
        else:
            if self.function_name == 'solve LHCCRR':
                args = [self.user_in[0], self.user_in[1]]
            elif self.function_name in controller.functions_with_list_parameters:
                args = [self.user_in]
            else:
                args = [self.user_in[0]]

        self.process = mp.Process(target=controller.run, args=(self.queue, function, args, time.time()))
        self.process.start()

        self.master.after(100, self.process_queue)

    def process_queue(self):
        try:
            result, t = self.queue.get(0)
            self.res.grid(row=8,column=1)
            if not result:
                if self.function_name == 'solve LHCCRR':
                    s = '''No implementation for complex roots of LHCCRR\nNo implementation for higher order solutions with repeated roots'''
                else:
                    s = "This should not happen :o"
            elif result == "interrupt":
                self.process.terminate()
                time.sleep(0.1)
                if self.py_version_gte_3_7:
                    self.process.close()
                s = "Computation cancelled"
            else:
                s = controller.build_output_string(self.user_in, self.function_name, result, t)
            self.res.config(text=s, fg='blue')
            self.prog_bar.stop()
            self.prog_bar.grid_forget()
            self.compute_B.config(state=tk.NORMAL)
            self.compute_B.config(text="Compute")
            self.cancel_B.grid_forget()
        except queue.Empty: # this comes from queue module, not from multiprocessing
            self.master.after(100, self.process_queue)

if __name__ == '__main__':
    # Create top level GUI
    top = tk.Tk()
    top.geometry('{}x{}+0+0'.format(*top.maxsize()))
    top.option_add( "*font", "Monospace 16" )

    MainApplication(top)
    top.mainloop()
