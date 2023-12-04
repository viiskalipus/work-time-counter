"""   
A better Hello World for Tkinter
"""
# Avoid "star imports"
import tkinter as tk 
from tkinter import ttk
import datetime

# Frame widget is typically used as a container for other widgets
# Any number inside Frame class, all widgets inside is treated 
# like a single widget
class WorkTime(tk.Frame):
    """A friendly little module"""
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        # StringVar is part of a collection of variable types in Tkinter
        # that have special functionality, like automatic propagation of
        # changes to widgets or event triggers. 
        self.profile = tk.StringVar()
        self.profile_string = tk.StringVar()
        self.profile_string.set("Give savefile name")
        profile_label = ttk.Label(self, text="Profile: ")
        name_entry = ttk.Entry(self, textvariable=self.profile)
        
        profile_ok_button = ttk.Button(self, text="OK", command=self.profile_on_change)
        save_label = ttk.Label(self, textvariable=self.profile_string, 
                                font=("Consolas", 12), wraplength=600)
        
        self.time_elapsed = datetime.date
        self.time_counter_label = ttk.Label(self, textvariable=self.time_elapsed)
        
        
        # Grid is a geometry manager, it allows to position widgets
        # on their parent object by rows and columns. Sticky argument 
        # takes cardinal direction N, S, E or W (tk.W or "W"). 
        profile_label.grid(row=0, column=0, sticky=tk.W)
        name_entry.grid(row=0, column=1, sticky=(tk.W + tk.E))
        profile_ok_button.grid(row=0, column=2, sticky=tk.E)
        save_label.grid(row=1, column=0, columnspan=3)
        time_counter_label.grid
        
        
        # Columncofigure tells that the column 1 (0, 1, 2,... etc.)
        # has more weight than others so it will expand horizontally
        # that column and other columns to their minimum widths. 
        self.columnconfigure(1, weight=1)
        
    def profile_on_change(self):
        # strip() strips out the whitespace in the variable. 
        if self.profile.get().strip():
            self.profile_string.set(f"Saved for name \"{self.profile.get()}\"")
        else:
            self.profile_string.set("Saved for name \"no_name\"")
                
# More than one subclass Tk may cause issues if wanting multiple 
# MyApplication objects. 
class WorkTimeApplication(tk.Tk): 
    """Work Time Counter Main Application"""
    def __init__(self, *args, **kwargs):
        # Tk object is the root window and does not need 'parent' as argument.
        super().__init__(*args, **kwargs)
        # Window title
        self.title("Work Time Counter")
        # Sets the size of the window in pixels
        self.geometry("600x300")
        # Sets resizability of the window
        self.resizable(width=False, height=False)
        
        WorkTime(self).grid(sticky=(tk.E + tk.W + tk.N + tk.S))
        self.columnconfigure(0, weight=1)
        
# Checking if script is being run directly. 
# It's good to place this check into main execution 
# code to safely reuse classes and functions. 
if __name__ == '__main__':
    app = WorkTimeApplication()
    app.mainloop()
