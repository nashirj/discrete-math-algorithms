from tkinter import *

root = Tk()

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

text = Text(root, wrap=WORD, yscrollcommand=scrollbar.set)
text.pack()
s = ' '.join(['hi there i am joe']*1000)

# text.insert(1.0, END)
text.insert(END, s)
text.config(state=DISABLED)

scrollbar.config(command=text.yview)

mainloop()