from tkinter import *
from tkinter.ttk import *

# Only one of this object should be for every application
# This is the main exe thread
root = tk.Tk()

# Label() is passed to the master widget (root)
# Text to be displayed on the Label() widget
label = Label(root, text="Heippa Mirka ja Karpot!")
button = Button(root, text="Nappula")
entry = Entry(root, bd=5)

# Place label on the parent widget (root) 
# Pack is simplest of 3 *geometry managers*
label.pack()
button.pack()
entry.pack()

# Main event loop, processes keystrokes etc.
# Is ran until program is quit
# Usually last line of Tkinter program. 
# No line is read after this until program is closed. 
root.mainloop()