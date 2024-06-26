#!/usr/bin/python3

#https://docs.python.org/3.7/library/tkinter.html
import tkinter as tk
# For Font
from tkinter.font import *
from PIL import Image
from enum import Enum


root = None
app = None


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()


    def create_widgets(self):

        # Specials
        #global gui_variable_status
        #gui_variable_status = tk.StringVar(value='Status')

        # Title
        title_font = ('Arial', 20, 'bold')
        self.title_label = tk.Label(self, text="MatiShops", font=title_font)
        self.title_label.grid(row=0, column=0)  # View

        # What is this...
        large_font = ('Verdana',20)
        entry_var = tk.StringVar(value='EXAMPE_QR_CODE')
        #self.entry_qr = tk.Entry(self, width=40, textvariable=entry_var, font=large_font)
        self.entry_qr = tk.Text(self, width=40, height=10, font=large_font)
        self.entry_qr.grid(row=1, column=0, rowspan=2)  # View
        #self.entry_qr["textvariable"] = self.contents
        self.entry_qr.bind('<Key-Return>', self.entry_changed_input)

        self.button_2 = tk.Button(self, width=20, height=5)
        self.button_2["text"] = "Add"
        self.button_2["command"] = self.button_add_event
        self.button_2.grid(row=1, column=3)  # View

        self.button_3 = tk.Button(self, width=20, height=5)
        self.button_3["text"] = "Exit"
        self.button_3["command"] = self.button_exit_event
        self.button_3.grid(row=1, column=4)  # View


    def button_add_event(self):
        print('Add button')
        lines = self.entry_qr.get("0.0", tk.END)  # TODO: Check which line needed... or clear needed
        print(f'Lines: "{lines}"')
        self.add_item(lines)


    def button_exit_event(self):
        print('Exit button')
        self.quit()


    def quit(self):
        self.master.destroy()
        exit(0)


    def entry_changed_input(self, event):
        """ Called at newlines"""
        print(f'entry_changed_input: {event}')

        #content = self.entry_qr.get()  # entry
        content = self.entry_qr.get("0.0", tk.END)
        print(f'Content: {content}')
        if '\n' not in content:
            return
        lines = content.split('\n')
        lines = [item.strip() for item in lines]
        for new_line in lines:
            if len(new_line) == 0:
                continue
            # Item LETS GO
            print(f'Find new line: {new_line}')
            # TODO
        self.entry_qr.delete("0.0", tk.END)


def start_gui(config=None):
    global root

    root = tk.Tk()
    root.attributes('-fullscreen', True)
    app = Application(master=root)
    app.mainloop()


if __name__ == "__main__":
    start_gui()

