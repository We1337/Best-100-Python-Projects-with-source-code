#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk
import sv_ttk

from ui.window import CenteredWindow

# create and run application
root = CenteredWindow()

# create Labe1 widget for instructions
label = tk.Label(root, text="Enter your number:", height="2")
label.pack()

# create Entry widget for user input
user_input = tk.Entry(root)
user_input.pack()

# create Button widget to submit form
button = tk.Button(root, text="Submit", command=lambda: root.get_user_input(user_input.get()))
button.pack()

sv_ttk.set_theme("dark")
root.mainloop()
