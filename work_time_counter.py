
'''
Main application for work time counter
'''
import tkinter as tk
from tkinter import ttk


class WorkTime(tk.Frame): 
    ''' The application screen and widgets '''
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        

        profile_name = tk.StringVar()
        profile_label = ttk.Label(self, text="Profile: ")
        
        # Profile entry widget with profile_name
        profile_entry = ttk.Entry(parent, textvariable=profile_name)
        profile_ok_button = ttk.Button(self, text="OK", command=self.on_change)
        profile_name_label = ttk.Label(self, textvariable=profile_name, 
                                font=("Consolas", 24), wraplength=600)

        profile_label.grid(row=0, column=0)
        profile_entry.grid(row=0, column=0)
        profile_ok_button.grid(row=0, column=3)
        profile_name_label.grid(row=1, column=0, columnspan=3)
        
        self.columnconfigure(1, weight=1)

    def on_change(self): 
        if self.profile_name.get().strip():
            self.profile_name.set(self.name.get)
        else:
            # If no name is given, set empty
            self.profile_name.set("")

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