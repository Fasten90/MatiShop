
#https://docs.python.org/3.7/library/tkinter.html
import tkinter as tk
# For Font
from tkinter.font import *
from PIL import Image
from enum import Enum

import main


# Config
app_global_config = None


class PrintMode(Enum):
    Print_Automatic = "Print_Automatic"
    Print_Manual = "Print_Manual"


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.app_config = app_global_config


    def create_widgets(self):

        # Specials
        #global gui_variable_status
        #gui_variable_status = tk.StringVar(value='Status')

        # Title
        title_font = ('Arial', 20, 'bold')
        self.title_label = tk.Label(self, text="QR Code label creator", font=title_font)
        self.title_label.grid(row=0, column=0)  # View

        #self.table_top_root.grid(row=0, column=0, sticky='W')

        # Label - Counter
        self.print_counter = tk.StringVar(value='0')
        self.print_counter_label = tk.Label(self, textvariable=self.print_counter,
                                        relief=tk.RAISED,
                                        font=title_font)
        self.print_counter_label.grid(row=1, column=1)

        #
        large_font = ('Verdana',20)
        entry_var = tk.StringVar(value='EXAMPE_QR_CODE')
        #self.entry_qr = tk.Entry(self, width=40, textvariable=entry_var, font=large_font)
        self.entry_qr = tk.Text(self, width=40, height=10, font=large_font)
        #self.entry_qr.pack(side="bottom")
        self.entry_qr.grid(row=1, column=0, rowspan=2)  # View
        #self.entry_qr["textvariable"] = self.contents
        self.entry_qr.bind('<Key-Return>', self.entry_changed_input)


        # TODO:
        #self.button_1 = tk.Button(self, width=20, height=5)
        #self.button_1["text"] = "Read"
        #self.button_1["command"] = self.button_1_event
        ##self.button_1.pack(side="bottom")
        #self.button_1.grid(row=2, column=0)  # View

        self.button_2 = tk.Button(self, width=20, height=5)
        self.button_2["text"] = "Generate"
        self.button_2["command"] = self.button_2_event
        #self.button_2.pack(side="bottom")
        self.button_2.grid(row=1, column=3)  # View

        self.button_3 = tk.Button(self, width=20, height=5)
        self.button_3["text"] = "Exit"
        self.button_3["command"] = self.button_3_event
        #self.button_2.pack(side="bottom")
        self.button_3.grid(row=1, column=4)  # View

        self.button_4 = tk.Button(self, width=20, height=5)
        self.button_4["text"] = "Print"
        self.button_4["command"] = self.button_4_event
        #self.button_2.pack(side="bottom")
        self.button_4.grid(row=2, column=3)  # View

        self.print_mode = tk.StringVar()
        print_mode_font = ('Verdana', 25)
        self.print_mode_radiobutton_1 = tk.Radiobutton(self, text="Automatic", variable=self.print_mode, value=PrintMode.Print_Automatic,
                        command=self.print_mode_select,
                        font=print_mode_font)
        self.print_mode_radiobutton_1.grid(row=1, column=2, sticky="W")  # View
        # normal.grid(column=1,row=2,rowspan=3, sticky="W")

        self.print_mode_radiobutton_2 = tk.Radiobutton(self, text="Manual", variable=self.print_mode, value=PrintMode.Print_Manual,
                        command=self.print_mode_select,
                        font=print_mode_font)
        self.print_mode_radiobutton_2.grid(row=2, column=2, sticky="W")  # View

        self.update_image(destroy_required=False)


    def update_image(self, destroy_required=False):
        if destroy_required:
            self.button_qr_image.destroy()
        #
        #img = Image.open(global_config['ImagePath'])
        #self.qr_image = tk.PhotoImage(self, img)  # TODO: Does not work
        #self.qr_image = tk.PhotoImage(img)
        #
        # TODO: Move, due used more times?
        self.qr_image = tk.PhotoImage(file=app_global_config['ImagePath'])
        self.button_qr_image = tk.Button(self, image=self.qr_image)
        #
        #self.button_qr_image = tk.Button(self, image=img)
        #self.button_qr_image["image"] = self.qr_image
        self.button_qr_image["text"] = ""
        self.button_qr_image["command"] = self.button_qr_image_event
        #self.button_qr_image.pack(side="bottom")
        self.button_qr_image.grid(row=3, column=0, rowspan=2, columnspan=3)  # View

        #self.qr_image.grid(row=4, column=0)


    def generate_qr(self, qr_code):
        print(f"Text: {qr_code}")
        #print(app_global_config['ProductConfig'])
        main.calculate_info_and_generate_image(qr_code)
        # Refresh image
        self.update_image(destroy_required=True)


    def print_qr(self):
        #Counter
        actual_counter = int(self.print_counter.get())
        self.print_counter.set(str(actual_counter+1))
        # Real print
        main.page_print()


    def button_2_event(self):
        print('Generate button')
        lines = self.entry_qr.get("0.0", tk.END)  # TODO: Check which line needed... or clear needed
        #original_qr_code = lines.split('\n')[-1:]  # TODO: Bugfix list element
        original_qr_code = lines
        print(f'QR: "{original_qr_code}"')
        self.generate_qr(original_qr_code)


    def button_3_event(self):
        print('Exit button')
        self.quit()


    def button_4_event(self):
        print('Print button')
        self.print_qr()


    def print_mode_select(self):
        print('print_mode_select')
        print_mode = self.print_mode.get()
        print(f'print_mode value: {print_mode}')


    def quit(self):
        self.master.destroy()
        exit(0)


    def button_qr_image_event(self):
        # TODO: Create a functionality
        print('Click event on the image')


    def entry_changed_input(self, event):
        """ Called at newlines"""
        print(f'entry_changed_input: {event}')

        mode = self.print_mode.get()
        if mode == 'PrintMode.Print_Automatic':
            print('Automatic mode')
            #content = self.entry_qr.get()  # entry
            content = self.entry_qr.get("0.0", tk.END)
            print(content)
            if '\n' not in content:
                return
            lines = content.split('\n')
            lines = [item.strip() for item in lines]
            for new_line in lines:
                if len(new_line) == 0:
                    continue
                # Item LETS GO
                print(f'Find new line: {new_line}')
                # Generate
                self.generate_qr(new_line)
                # Print
                self.print_qr()
            self.entry_qr.delete("0.0", tk.END)
        else:
            print('Manual mode, multiline print is disabled')



root = None
app = None


def start_gui(config=None):
    global root
    global app
    global app_global_config

    main.global_read_config()
    app_global_config = main.global_config

    root = tk.Tk()
    root.attributes('-fullscreen', True)
    app = Application(master=root)
    app.mainloop()

# Original solution (default called)
#root = tk.Tk()
#root.attributes('-fullscreen', True)
#app = Application(master=root)
#app.mainloop()


if __name__ == "__main__":
    import main
    main.main()

