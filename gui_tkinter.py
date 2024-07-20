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

        # Title
        title_font = ('Arial', 20, 'bold')

        self.title_label = tk.Label(self, text="MatiShop", font=title_font)
        self.title_label["bg"] = "darkgrey"
        self.title_label.grid(row=0, column=0)  # View

        large_font = ('Verdana',20)

        self.entry_barcode_input = tk.Text(self, width=40, height=10, font=large_font)
        self.entry_barcode_input.grid(row=1, column=0, rowspan=2)  # View
        #self.entry_barcode_input["textvariable"] = self.contents
        self.entry_barcode_input["bg"] = "darkgrey"
        self.entry_barcode_input.bind('<Key-Return>', self.entry_changed_input)

        self.button_clear = tk.Button(self, width=20, height=5)
        self.button_clear["text"] = "Clear"
        self.button_clear["command"] = self.button_clear_event
        self.button_clear["bg"] = "darkgrey"
        self.button_clear.grid(row=1, column=3)  # View

        self.button_exit = tk.Button(self, width=20, height=5)
        self.button_exit["text"] = "Exit"
        self.button_exit["command"] = self.button_exit_event
        self.button_exit["bg"] = "darkgrey"
        self.button_exit.grid(row=1, column=4)  # View

        self.button_add = tk.Button(self, width=20, height=5)
        self.button_add["text"] = "Add"
        self.button_add["command"] = self.button_add_event
        self.button_add["bg"] = "darkgrey"
        self.button_add.grid(row=2, column=3)  # View

        self.text_itemname = tk.Text(self, width=10, height=1, font=large_font)
        self.text_itemname.grid(row=3, column=3)  # View
        self.text_itemname["bg"] = "darkgrey"

        self.text_itemcost = tk.Text(self, width=10, height=1, font=large_font)
        self.text_itemcost.grid(row=3, column=4)  # View
        self.text_itemcost["bg"] = "darkgrey"

        self.text_log = tk.Text(self, width=40, height=10, font=large_font)
        self.text_log["bg"] = "darkgrey"
        self.text_log.grid(row=2, column=0, rowspan=2)  # View

        self.all_cost_label = tk.Label(self, text="All cost:", font=title_font)
        self.all_cost_label["bg"] = "darkgrey"
        self.all_cost_label.grid(row=4, column=0)  # View

        self.all_cost_calculation_label = tk.Label(self, text="0 Ft", font=title_font)
        self.all_cost_calculation_label["bg"] = "darkgrey"
        self.all_cost_calculation_label.grid(row=4, column=1)  # View


    def button_add_event(self):
        self.print_log(f'Try to add...')
        lines = self.entry_barcode_input.get("0.0", tk.END)  # TODO: Check which line needed... or clear needed
        print(f'Lines: "{lines}"')
        import shop
        barcode = lines.strip()
        item_name = self.text_itemname.get("0.0", tk.END).strip()
        item_cost = self.text_itemcost.get("0.0", tk.END).strip()
        shop.add_item(barcode, item_name, item_cost)


    def button_exit_event(self):
        print('Exit button')
        self.quit()

    def button_clear_event(self):
        print('Clear button')
        import shop
        shop.clear_cost()
        self.all_cost_calculation_label["text"] = "0 Ft"
        self.text_log.delete("1.0", tk.END)

    def quit(self):
        self.master.destroy()
        exit(0)

    def update_all_cost(self):
        import shop
        all_cost_value = shop.get_all_cost()
        self.all_cost_calculation_label["text"] = all_cost_value


    def entry_changed_input(self, event):
        """ Called at newlines"""
        print(f'entry_changed_input: {event}')

        content = self.entry_barcode_input.get("0.0", tk.END)
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
            # Process the line
            import shop
            shop_result = shop.check_if_item_is_available(new_line)
            if shop_result:
                self.print_log(f'Successfully found: {new_line}')
                self.button_add["state"] = tk.DISABLED
                item_info = shop.get_item_info(new_line)
                shop.add_item_to_cost(item_info)
                self.print_log(f'{item_info["item"]}')
                self.print_log(f'{item_info["cost"]}')
                self.update_all_cost()
                self.text_itemname.delete("1.0", tk.END)
                self.text_itemname.insert(tk.END, item_info["item"])
                self.text_itemcost.delete("1.0", tk.END)
                self.text_itemcost.insert(tk.END, item_info["cost"])
                #self.text_itemname.configure(tk.DISABLED)
                #self.text_itemcost.configure(tk.DISABLED)
            else:
                self.print_log(f'{new_line} not found, you shall add it!')
                self.button_add["state"] = tk.NORMAL
                self.text_itemname.configure(tk.NORMAL)
                self.text_itemcost.configure(tk.NORMAL)
        self.entry_barcode_input.delete("0.0", tk.END)

    def print_log(self, message):
        print(f'[INFO] {message}')
        self.text_log.insert(tk.END, message + '\n')


def do_shop_init():
    try:
        import shop
        shop.load_offline_config()
    except:
        print('[ERROR] with loading shop data!')


def start_gui(config=None):
    global root
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    app = Application(master=root)
    # Not tkinter related
    do_shop_init()
    # end of tkinter related
    root.configure(bg="darkgrey")
    app.configure(bg="darkgrey")  # Colorize all sub widgets
    app.mainloop()


if __name__ == "__main__":
    start_gui()

