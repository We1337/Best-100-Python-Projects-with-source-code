import tkinter as tk
from tkinter import messagebox
import sv_ttk

from ui.logic import Logic

class CenteredWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # set window title
        self.title("Centered Window")
        
        # set window size
        self.geometry("300x200")
        
        # center window on screen
        self.center_window()

        self.random_number = Logic.random_number(0, 10)
        
    def center_window(self):
        # get screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        # calculate coordinates of top-left corner to center window
        x = (screen_width - self.winfo_reqwidth()) // 2
        y = (screen_height - self.winfo_reqheight()) // 2
        
        # set window position
        self.geometry("+{}+{}".format(x, y))

    def result_window(self, user_input):
        tk.messagebox.showinfo("Correct number: " + str(self.random_number), "Your input: " + str(user_input))

    def get_user_input(self, user_input):
        # compare user input with random number
        if int(user_input) == self.random_number:
            self.result_window(user_input)
        else:
            self.result_window(user_input)