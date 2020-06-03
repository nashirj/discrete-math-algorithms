from tkinter import *
import queue

class Loader(Label):
    def __init__(self, master, link, **kwargs):
        Label.__init__(self, text="")
        self.grid(row=1,column=2)
        self.sequence = ['-', '\\', '|', '/']
        self.load = False
        self.queue = queue.Queue()
        self.n=0
        self.link = link
        self.done = False
    def start(self):
        self.load = True
        self.done = False
        self.update_me()
    def end(self):
        self.load = False
        self.done = True
        self.queue.put((None,None))
    def set_text(self, text):
        self.title = text
        if self.done:
            self.config(text=self.title)
    def update_me(self):
        try:
            while 1 and not self.done:
                line, link = self.queue.get_nowait()
                self.load = (link and link == 'loader')
                self.config(text=f"{self.title}  {str(line)}")
                self.update_idletasks()
        except queue.Empty:
            pass
        if self.done:
            self.config(text="???")
            return
        else:
            self.after(100, self.update_me)
        if self.load:
            self.queue.put((self.sequence[self.n%len(self.sequence)], self.link))
            self.n += 1

if __name__ == '__main__':
    # testing application
    import time
    from py_modules import relations
    root = Tk()
    n = 4
    loader = Loader(root, "loader")
    text = f"Computing number of transitive relations on a {n} element set"
    loader.set_text(text)
    loader.pack()

    def load_it(n):
        loader.start()
        res = relations.count_transitive_relations(n)
        loader.set_text(f"There are {res} transitive relations for n = {n}")
        loader.end()
        time.sleep(2)

    import threading
    t = threading.Thread(target=load_it, args=[n])
    t.daemon = True
    t.start()
    t.join()

    root.mainloop()

    t.join()

    exit()
