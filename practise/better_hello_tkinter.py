"""   
A better Hello World for Tkinter
"""
# Avoid "star imports"
import tkinter as tk 
from tkinter import ttk

# Frame widget is typically used as a container for other widgets
# Any number inside Frame class, all widgets inside is treated 
# like a single widget
class HelloView(tk.Frame):
    """A friendly little module"""
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        # StringVar is part of a collection of variable types in Tkinter
        # that have special functionality, like automatic propagation of
        # changes to widgets or event triggers. 
        self.name = tk.StringVar()
        self.hello_string = tk.StringVar()
        self.hello_string.set("Hello World")
        name_label = ttk.Label(self, text="Name: ")
        name_entry = ttk.Entry(self, textvariable=self.name)
        
        ch_button = ttk.Button(self, text="Change", command=self.on_change)
        hello_label = ttk.Label(self, textvariable=self.hello_string, 
                                font=("Consolas", 64), wraplength=600)
        
        # Grid is a geometry manager, it allows to position widgets
        # on their parent object by rows and columns. Sticky argument 
        # takes cardinal direction N, S, E or W (tk.W or "W"). 
        name_label.grid(row=0, column=0, sticky=tk.W)
        name_entry.grid(row=0, column=1, sticky=(tk.W + tk.E))
        ch_button.grid(row=0, column=2, sticky=tk.E)
        hello_label.grid(row=1, column=0, columnspan=3)
        
        # Columncofigure tells that the column 1 (0, 1, 2,... etc.)
        # has more weight than others so it will expand horizontally
        # that column and other columns to their minimum widths. 
        self.columnconfigure(1, weight=1)
        
    def on_change(self):
        # strip() strips out the whitespace in the variable. 
        if self.name.get().strip():
            self.hello_string.set(f"Hello {self.name.get()}!")
        else:
            self.hello_string.set("Hello World")
                
# More than one subclass Tk may cause issues if wanting multiple 
# MyApplication objects. 
class MyApplication(tk.Tk): 
    """Hello World Main Application"""
    def __init__(self, *args, **kwargs):
        # Tk object is the root window and does not need 'parent' as argument.
        super().__init__(*args, **kwargs)
        # Window title
        self.title("Hello Tkinter")
        # Sets the size of the window in pixels
        self.geometry("800x600")
        # Sets resizability of the window
        self.resizable(width=False, height=False)
        
        HelloView(self).grid(sticky=(tk.E + tk.W + tk.N + tk.S))
        self.columnconfigure(0, weight=1)
        
# Checking if script is being run directly. 
# It's good to place this check into main execution 
# code to safely reuse classes and functions. 
if __name__ == '__main__':
    app = MyApplication()
    app.mainloop()
