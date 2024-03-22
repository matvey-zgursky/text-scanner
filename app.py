import tkinter as tk
from tkinter import ttk


class App():
    def start(self):
        root = tk.Tk()
        start_page = StartPage(root)
        
        root.title('Text scanner')
        root.minsize(600, 400)

        root.mainloop()

class StartPage(ttk.Frame):
    def __init__(self, master: tk.Misc | None = None) -> None:
        super().__init__(master)

        button = ttk.Button(self.master, text='Открыть изображение')
        button.place(relwidth=0.5, relheight=0.15, relx=0.25, rely=0.4)

class ImagePage():
    pass
