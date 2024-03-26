import tkinter as tk
from tkinter import ttk

import os

from exceptions import UnsupportedOperatingSystemError


class App():
    def start(self) -> None:
        root = tk.Tk()
        start_page = StartPage(root)
        
        root.title('Text scanner')
        root.minsize(600, 400)

        root.mainloop()

class StartPage(ttk.Frame):
    def __init__(self, master: tk.Misc | None = None) -> None:
        super().__init__(master)

        button = ttk.Button(self.master, text='Открыть изображение', command=self.open_explorer)
        button.place(relwidth=0.5, relheight=0.15, relx=0.25, rely=0.4)

    def open_explorer(self):
        """Открыть системный проводник"""
        os_name = os.name

        if os_name == 'nt':
            os.system('explorer')
        elif os_name == 'posix':
            if 'Apple' in os.uname().sysname:
                os.system('open')
            else:
                os.system('xdg-open')
        else:
            raise UnsupportedOperatingSystemError(os_name)


class ImagePage():
    pass
