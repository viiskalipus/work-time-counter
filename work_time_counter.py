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
    """Work Time counter main screen"""
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        # StringVar is part of a collection of variable types in Tkinter
        # that have special functionality, like automatic propagation of
        # changes to widgets or event triggers. 
        self.profile = tk.StringVar()
        self.profile.set("anonymous")
        self.profile_string = tk.StringVar()
        self.profile_string.set("Give savefile name")
        profile_label = ttk.Label(self, text="Profile: ")
        name_entry = ttk.Entry(self, textvariable=self.profile)
        
        profile_ok_button = ttk.Button(self, text="OK", command=self.profile_on_change)
        save_label = ttk.Label(self, textvariable=self.profile_string, 
                                font=("Consolas", 12), wraplength=600)
        
        self.time_elapsed = tk.StringVar()
        self.time_elapsed.set("Current time is " + 
                                datetime.datetime.now().strftime("%H:%M:%S"))
        
        self.current_time = tk.StringVar()
        self.current_time.set("Current time is " + 
                                datetime.datetime.now().strftime("%H:%M:%S"))
        time_counter_label = ttk.Label(self, textvariable=self.time_elapsed, 
                                font=("Consolas", 18), background="red")
        current_time_label = ttk.Label(self, textvariable=self.current_time, 
                                font=("Consolas", 18), background="green")
        
        counter_start_button = ttk.Button(self, text="Start", command=self.start_time)
        counter_pause_button = ttk.Button(self, text="Pause", command=self.pause_time)
        self.task_name = tk.StringVar()
        self.task_name.set("Enter task name")
        task_label = ttk.Label(self, text="Task: ")
        task_entry = ttk.Entry(self, textvariable=self.task_name)
        task_ok_button = ttk.Button(self, text="OK", command=self.task_on_change)
        
        log_box = ttk.Notebook(self, height=100, width=100)
        
        # Grid is a geometry manager, it allows to position widgets
        # on their parent object by rows and columns. Sticky argument 
        # takes cardinal direction N, S, E or W (tk.W or "W"). 
        profile_label.grid(row=0, column=0, sticky="W")
        name_entry.grid(row=0, column=1, sticky="WE")
        profile_ok_button.grid(row=0, column=2, sticky="E")
        save_label.grid(row=1, column=0, columnspan=3)
        time_counter_label.grid(row=2, column=0, columnspan=2, rowspan=1, sticky="WSN")
        current_time_label.grid(row=3, column=0, columnspan=2, rowspan=1, sticky="WSN")
        log_box.grid(row=5, column=0, columnspan=3, rowspan=1, sticky="WES")
        counter_start_button.grid(row=2, column=2, sticky="E")
        counter_pause_button.grid(row=3, column=2, sticky="E")
        task_label.grid(row=4, column=0, sticky="W")
        task_entry.grid(row=4, column=1, sticky="WE")
        task_ok_button.grid(row=4, column=2, sticky="E")
        
        # Columncofigure tells that the column 1 (0, 1, 2,... etc.)
        # has more weight than others so it will expand horizontally
        # that column and other columns to their minimum widths. 
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)
        
    # When savefile profile is changed
    def profile_on_change(self):
        # strip() strips out the whitespace in the variable. 
        if self.profile.get().strip():
            self.profile_string.set(f"Saved for name \"{self.profile.get()}\"")
        else:
            self.profile_string.set("Saved for name \"no_name\"")
                
    # When time counter is started
    def start_time(self):
        pass
    
    # When time counter is paused
    def pause_time(self):
        pass
    
    # When current task is changed
    def task_on_change(self):
        pass
    
class WorkTimeApplication(tk.Tk): 
    """Work Time Counter Main Application"""
    def __init__(self, *args, **kwargs):
        # Tk object is the root window and does not need 'parent' as argument.
        super().__init__(*args, **kwargs)
        # Window title
        self.title("Work Time Counter")
        # Sets the size of the window in pixels, default 600x300
        self.geometry("600x300")
        # Sets resizability of the window, default False
        self.resizable(width=False, height=False)
        
        WorkTime(self).grid(sticky=(tk.E + tk.W + tk.N + tk.S))
        self.columnconfigure(0, weight=1)
        
# Checking if script is being run directly. 
if __name__ == '__main__':
    app = WorkTimeApplication()
    app.mainloop()
