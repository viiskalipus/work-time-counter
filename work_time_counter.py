"""   
Work Time Counter for keeping track on working time. 
"""
import tkinter as tk 
from tkinter import ttk
import datetime
import tkinter.scrolledtext as scrolledtext

# WorkTime Frame
class WorkTime(tk.Frame):
    """Work Time counter main screen"""
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        # Set savename
        self.profile = tk.StringVar()
        self.profile.set("")
        self.profile_string = tk.StringVar()
        self.profile_string.set("Give savefile name")
        profile_label = ttk.Label(self, text="Profile: ")
        name_entry = ttk.Entry(self, textvariable=self.profile)
        save_label = ttk.Label(self, textvariable=self.profile_string, 
                                font=("Consolas", 12), wraplength=600)
        
        # Running time
        self.time_elapsed = tk.StringVar()
        self.time_elapsed.set("Current time is " + 
                                datetime.datetime.now().strftime("%H:%M:%S"))
        time_counter_label = ttk.Label(self, textvariable=self.time_elapsed, 
                                font=("Consolas", 18), background="red")
        # Current time
        self.current_time = tk.StringVar()
        self.current_time.set("Current time is " + 
                                datetime.datetime.now().strftime("%H:%M"))
        current_time_label = ttk.Label(self, textvariable=self.current_time, 
                                font=("Consolas", 18), background="green")
               
        # Set task
        self.task_name = tk.StringVar()
        self.task_name.set("")
        task_label = ttk.Label(self, text="Task: ")
        task_entry = ttk.Entry(self, textvariable=self.task_name)

        
        # Log
        log_screen = scrolledtext.ScrolledText(self, height=8, width=100)
        log_label = ttk.Label(self, text="Log: ")
        
        # Buttons
        profile_ok_button = ttk.Button(self, text="OK", command=self.profile_on_change)
        counter_start_button = ttk.Button(self, text="Start", command=self.start_time)
        counter_pause_button = ttk.Button(self, text="Pause", command=self.pause_time)
        task_ok_button = ttk.Button(self, text="OK", command=self.task_on_change)
        
        # Grid positions
        profile_label.grid(row=0, column=0, sticky="W")
        name_entry.grid(row=0, column=1, sticky="WE")
        profile_ok_button.grid(row=0, column=2, sticky="E")
        save_label.grid(row=1, column=0, columnspan=3)
        time_counter_label.grid(row=2, column=0, columnspan=2, rowspan=1, sticky="WSN")
        current_time_label.grid(row=3, column=0, columnspan=2, rowspan=1, sticky="WSN")
        counter_start_button.grid(row=2, column=2, sticky="E")
        counter_pause_button.grid(row=3, column=2, sticky="E")
        task_label.grid(row=4, column=0, sticky="W")
        task_entry.grid(row=4, column=1, sticky="WE")
        task_ok_button.grid(row=4, column=2, sticky="E")
        log_screen.grid(row=6, column=1, sticky="ES")
        log_label.grid(row=5, column=0, sticky="W")
        
        # Column/row configurations
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)
        
    # When savefile profile is changed
    def profile_on_change(self):
        # strip() strips out the whitespace in the variable. 
        if self.profile.get().strip():
            self.profile_string.set(f"Saved to file \"{self.profile.get()}\"")
        else:
            self.profile_string.set("Saved to file \"no_name\"")
                
    # When time counter is started
    def start_time(destination):
        destination.insert('end', 'Started')
        # Update log "Task {task_name} started at {current_time} for "
        # If pause True and start False, start the timer
            # 
    
    # When time counter is paused
    def pause_time(self):
        pass
        # If pause False but start True, pause the timer
            # Change button text to 'Reset'
        # If pause True and start False, reset the timer
            # Change button to 'Pause'
    
    # When current task is changed
    def task_on_change(self):
        pass
        # Update log f"Task changed to {task_name} at [HH:MM:SS]"
    
    # Update changes to log
    def update_log(self):
        pass
    
    # Write log into a file
    def write_file(self):
        pass
        # When log updated, add to file
        # If application to be closed, stop timer and save to file before
    


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
