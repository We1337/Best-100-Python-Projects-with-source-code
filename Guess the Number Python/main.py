#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import tkinter as tk

import sv_ttk


class CenteredWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # set window title
        self.title("Centered Window")
        
        # set window size
        self.geometry("300x200")
        
        # center window on screen
        self.center_window()

        # random number
        self.number = random.randint(0, 10)
        
    def center_window(self):
        # get screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        # calculate coordinates of top-left corner to center window
        x = (screen_width - self.winfo_reqwidth()) // 2
        y = (screen_height - self.winfo_reqheight()) // 2
        
        # set window position
        self.geometry("+{}+{}".format(x, y))
        
    def random_number(self):
        # return random number
        return random.randint(1, 10)

    def get_input(self, user_input):
        # check two number
        if int(user_input) == self.number:
            label = tk.Label(self, text=user_input)
            label.pack()
        else:
            label = tk.Label(self, text=user_input)            
            label.pack()
    
# create and run application
root = CenteredWindow()

# create Labe1 widget for instructions
label = tk.Label(root, text="Enter your number:", height="2")
label.pack()

# create Entry widget for user input
user_input = tk.Entry(root)
user_input.pack()

# create Button widget to submit form
button = tk.Button(root, text="Submit", command=lambda: root.get_input(user_input.get()))
button.pack()

sv_ttk.set_theme("dark")
root.mainloop()