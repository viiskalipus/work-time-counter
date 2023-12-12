"""   
Work Time Counter for keeping track on working time. 
"""
# Imported libraries 
import tkinter as tk 
from tkinter import ttk
import datetime
import time
import tkinter.scrolledtext as scrolledtext
from functools import partial

# WorkTime Frame
class WorkTime(tk.Frame):
    """Work Time counter main screen"""
    def __init__(self, window=None):
        super().__init__(window)
        self.window = window
        self.zero_time = ""
        # Stopwatch running
        self.is_running = False
        self.total_h = 0
        self.total_m = 0
        self.total_s = 0
        
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
        self.elapsed_time = tk.StringVar()
        self.elapsed_time_label = tk.Label(self, text="00:00:00", font=("Consolas", 24))
        
        # Current time
        self.current_time = tk.StringVar()
        self.current_time.set("Current time: " + 
                                datetime.datetime.now().strftime("%H:%M:%S"))
        current_time_label = ttk.Label(self, textvariable=self.current_time, 
                                font=("Consolas", 24), background="yellow")
               
        # Set task
        self.task_name = tk.StringVar()
        self.task_name.set("")
        task_label = ttk.Label(self, text="Task: ")
        task_entry = ttk.Entry(self, textvariable=self.task_name)
        
        # Log
        self.log_screen = scrolledtext.ScrolledText(self, height=8, width=100)
        log_label = ttk.Label(self, text="Log: ")
        
        # Buttons
        profile_ok_button = ttk.Button(self, text="OK", command=self.profile_on_change)
        task_ok_button = ttk.Button(self, text="OK", command=self.task_on_change)
        save_button = ttk.Button(self, text="Save", command=self.save_to_file)
        quit_button = ttk.Button(self, text="Quit", command=self.window.quit)
        self.counter_start_button = ttk.Button(self, text="Start", command=self.start_time)
        self.counter_pause_button = ttk.Button(self, text="Pause", command=self.pause_time)
        self.counter_reset_button = ttk.Button(self, text="Reset", command=self.reset_time)
        
        # Grid positions
        profile_label.grid(row=0, column=0, sticky="W")
        name_entry.grid(row=0, column=1, sticky="WE")
        profile_ok_button.grid(row=0, column=2, sticky="E")
        save_label.grid(row=1, column=0, columnspan=3)
        self.elapsed_time_label.grid(row=2, column=0, columnspan=2, rowspan=1, sticky="WSN")
        current_time_label.grid(row=3, column=0, columnspan=2, rowspan=1, sticky="WSN")
        task_label.grid(row=4, column=0, sticky="W")
        task_entry.grid(row=4, column=1, sticky="WE")
        task_ok_button.grid(row=4, column=2, sticky="E")
        self.log_screen.grid(row=6, column=1, sticky="ES")
        log_label.grid(row=5, column=0, sticky="W")
        save_button.grid(row=7, column=2, sticky="ES")
        quit_button.grid(row=8, column=2, sticky="ES")
        self.counter_start_button.grid(row=1, column=2, sticky="E")
        self.counter_pause_button.grid(row=2, column=2, sticky="E")
        self.counter_reset_button.grid(row=3, column=2, sticky="E")
        
        # Column/row configurations
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)
        
        # Sync with computer clock
        snooze = (1000000 - datetime.datetime.now().microsecond) / 1000000.
        if snooze > 0:
            time.sleep(snooze)
        self.clock()
        self.log_screen.insert("end", f"Date: [{datetime.date.today()}]\n")     

    # Clock to keep current time
    def clock(self): 
        self.current_time.set(datetime.datetime.now().strftime("%H:%M:%S"))
        self.after(1000, self.clock)
    
    # When savefile profile is changed
    def profile_on_change(self):
        self.profile_string.set(f"Saved to file \"{self.profile.get()}.txt\"")
        
        # TODO
        # - Add date to filename        

    # When time counter is started
    def start_time(self):
        # Update log
        self.log_screen.insert("end", f"[{self.current_time.get()}]\[{self.elapsed_time.get()}]: START > Task [{self.task_name.get()}] started\n")
        # Scroll to bottom after log is updated
        self.log_screen.yview(tk.END)

        # Check if can start
        if not self.is_running:
            self.elapsed_time_label.after(1000)
            self.update_time()
            self.is_running = True
            
        # TODO
        # - If pause True and start False, start the timer
        # - Disable start/continue button when time is not paused
        # - Enable start/continue button when time is paused

    # When time counter is paused
    def pause_time(self):
        # Update log
        self.log_screen.insert("end", f"[{self.current_time.get()}]\[{self.elapsed_time.get()}]: PAUSE > Task [{self.task_name.get()}] paused\n")
        # Scroll to bottom after log is updated
        self.log_screen.yview(tk.END)
        
        if self.is_running:
            self.elapsed_time_label.after_cancel(self.zero_time)
            self.is_running = False
        
        # TODO
        # If pause False but start True, pause the timer
            # Change button text to 'Reset'
        # If pause True and start False, reset the timer
            # Change button to 'Pause'
        
    # When time counter is reset
    def reset_time(self):
        # Update log
        self.log_screen.insert("end", f"[{self.current_time.get()}]\[{self.elapsed_time.get()}]: RESET > Task [{self.task_name.get()}] reset\n")
        # Scroll to bottom after log is updated
        self.log_screen.yview(tk.END)
        
        if self.is_running:
            self.counter_pause_button.after_cancel(self.zero_time)
            self.is_running == False
        self.total_h = 0
        self.total_m = 0
        self.total_s = 0
        self.elapsed_time_label.config(text="00:00:00")
    
    # Update time counter
    def update_time(self):
        self.total_s += 1
        if self.total_s == 60:
            self.total_m += 1
            self.total_s = 0
        if self.total_m == 60:
            self.total_h += 1
            self.total_m = 0
            
        total_h_str = f"{self.total_h}" if self.total_h > 9 else f"0{self.total_h}"
        total_m_str = f"{self.total_m}" if self.total_m > 9 else f"0{self.total_m}"
        total_s_str = f"{self.total_s}" if self.total_s > 9 else f"0{self.total_s}"
        
        self.elapsed_time_label.config(text=
                                    total_h_str + ":" +
                                    total_m_str + ":" + 
                                    total_s_str)
        
        self.elapsed_time.set(total_h_str + ":" +
                                total_m_str + ":" + 
                                total_s_str)
        
        self.zero_time = self.elapsed_time_label.after(1000, self.update_time)

    # Save log into a file
    def save_to_file(self):
        filename = f"{self.profile.get()}.txt"
        file = open(filename, "w")
        print(f"Saved to file {filename}: \n" + self.log_screen.get("1.0", tk.END))
        file.write(self.log_screen.get("1.0", tk.END))
        file.close()

        # When log updated, add to file
        # filename: "profile.txt"

        # TODO
        # - If application to be closed, stop timer and save to file before
        # - Save to "profile_DD_MM_YY.txt"

    # When current task is changed
    def task_on_change(self):
        # Update log
        "[{self.current_time.get()}]\[{self.elapsed_time.get()}]: RESET > Task {self.task_name.get()} reset\n"
        self.log_screen.insert("end", f"[{self.current_time.get()}]\[{self.elapsed_time.get()}]: TASK > New task [{self.task_name.get()}]\n")
        # Scroll to bottom after log is updated
        self.log_screen.yview(tk.END)

class WorkTimeApplication(tk.Tk): 
    """Work Time Counter Main Application"""
    def __init__(self, *args, **kwargs):
        # Tk object is the root window and does not need 'parent' as argument.
        super().__init__(*args, **kwargs)
        # Window title
        self.title("Work Time Counter")
        # Sets the size of the window in pixels, default 600x300
        self.geometry("600x380")
        # Sets resizability of the window, default False
        self.resizable(width=False, height=False)
        
        WorkTime(self).grid(sticky=(tk.E + tk.W + tk.N + tk.S))
        self.columnconfigure(0, weight=1)
        
# Checking if script is being run directly. 
if __name__ == '__main__':
    app = WorkTimeApplication() 
    app.mainloop()
