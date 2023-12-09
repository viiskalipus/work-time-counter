"""   
Work Time Counter for keeping track on working time. 
"""
import tkinter as tk 
from tkinter import ttk
import datetime
import time
import tkinter.scrolledtext as scrolledtext
from functools import partial



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
        self.time_elapsed.set("Elapsed time: ")
        time_counter_label = ttk.Label(self, textvariable=self.time_elapsed, 
                                font=("Consolas", 18), background="red")
        
        # Current time
        self.current_time = tk.StringVar()
        self.current_time.set("Current time: " + 
                                datetime.datetime.now().strftime("%H:%M:%S"))
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
        counter_start_button = ttk.Button(self, text="Start", 
                                          command=partial(start_time, 
                                                          log_screen, 
                                                          self.task_name, 
                                                          self.current_time,
                                                          self.time_elapsed))
        counter_pause_button = ttk.Button(self, text="Pause", command=self.pause_time)
        task_ok_button = ttk.Button(self, text="OK", 
                                    command=partial(task_on_change,
                                                    log_screen,
                                                    self.task_name,
                                                    self.current_time))
        save_button = ttk.Button(self, text="Save", command=partial(save_to_file, 
                                                                    self.profile,
                                                                    log_screen))
        
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
        save_button.grid(row=7, column=2, sticky="ES")
        
        # Column/row configurations
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)
        
        # Sync with computer clock
        snooze = (1000000 - datetime.datetime.now().microsecond) / 1000000.
        if snooze > 0:
            time.sleep(snooze)
        self.clock()
        
        log_screen.insert("end", f"Date: [{datetime.date.today()}]\n")
        
    def clock(self): 
        self.current_time.set(datetime.datetime.now().strftime("%H:%M:%S"))
        self.after(1000, self.clock)
    
    # When savefile profile is changed
    def profile_on_change(self):
        # strip() strips out the whitespace in the variable. 
        if self.profile.get().strip():
            self.profile_string.set(f"Saved to file \"{self.profile.get()}.txt\"")
        else:
            self.profile_string.set("Saved to file \"unnamed.txt\"")
        
        # TODO
        # - Add date to filename

    # When time counter is paused
    def pause_time(self):
        pass
    
        # f"[{elapsed}]\n"
        
        # TODO
        # If pause False but start True, pause the timer
            # Change button text to 'Reset'
        # If pause True and start False, reset the timer
            # Change button to 'Pause'
        
# Stop counting time
def stop_time():
    global is_running
    is_running = False
    
# Update time
def update_time(elapsed):
    if is_running:
        elapsed_time = time.time() - t_start
        elapsed.set("Elapsed time: " + str(elapsed_time))
        elapsed.after(50, update_time)

# Save log into a file
def save_to_file(name, text):
    filename = f"{name.get()}.txt"
    file = open(filename, "w")
    print(f"Saved to file {filename}: \n" + text.get("1.0", tk.END))
    file.write(text.get("1.0", tk.END))
    file.close()
        
    # When log updated, add to file
    # filename: "profile.txt"
    
    # TODO
    # - If application to be closed, stop timer and save to file before
    # - Save to "profile_DD_MM_YY.txt"

# When current task is changed
def task_on_change(destination, task, t):
    destination.insert('end', f'New task {task.get()} at [{t.get()}]\n')
        
# When time counter is started
def start_time(destination, task, t, elapsed):
    destination.insert("end", f"[{t.get()}]: Task {task.get()} started\n")
    
    global is_running
    global t_start
    if not is_running: 
        is_running = True
        t_start = time.time()
        update_time(elapsed)
    
    # TODO
    # - If pause True and start False, start the timer
    # - Disable start/continue button when time is not paused
    # - Enable start/continue button when time is paused
        
is_running = False

class WorkTimeApplication(tk.Tk): 
    """Work Time Counter Main Application"""
    def __init__(self, *args, **kwargs):
        # Tk object is the root window and does not need 'parent' as argument.
        super().__init__(*args, **kwargs)
        # Window title
        self.title("Work Time Counter")
        # Sets the size of the window in pixels, default 600x300
        self.geometry("600x350")
        # Sets resizability of the window, default False
        self.resizable(width=False, height=False)
        
        WorkTime(self).grid(sticky=(tk.E + tk.W + tk.N + tk.S))
        self.columnconfigure(0, weight=1)
        
# Checking if script is being run directly. 
if __name__ == '__main__':
    app = WorkTimeApplication() 
    app.mainloop()
