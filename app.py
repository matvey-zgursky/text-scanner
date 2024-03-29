import tkinter as tk
from tkinter import ttk

from typing import Dict, Union
import os

from exceptions import UnsupportedOperatingSystemError


class StartPage(ttk.Frame):
    """
    Главная страница приложения, отображающая пользовательский интерфейс.

    Предоставляет кнопку для возможности открыть файловый менеджер.

    Attributes:
        master (tk.Misc): родительский виджет для этого фрейма.
        app (tk.Tk): экземпляр основного класса приложения для управления страницами.
    """
    def __init__(self, master: tk.Misc, app: tk.Tk) -> None:
        """Инициализировать главную страницу с кнопкой."""
        super().__init__(master)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)  

        button = ttk.Button(self, text='Открыть изображение',
                            command=lambda: app.show_frame(ImagePage))
        button.grid(row=0, column=0, sticky='nsew')

    def open_explorer(self) -> None:
        """
        Открывает файловый менеджер в зависимости от операционной системы.
        """
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

class ImagePage(ttk.Frame):
    """
    Страница приложения для работы с изображениями.

    В настоящий момент не содержит пользовательского интерфейса или функционала.

    Attributes:
        master (tk.Misc): родительский виджет для этого фрейма.
        app (App): экземпляр основного класса приложения для управления страницами.
    """
    def __init__(self, master: tk.Misc, app: tk.Tk) -> None:
        """Инициализировать страницу для работы с изображением."""
        super().__init__(master)
        pass

class App(tk.Tk):
    """
    Основной класс приложения, управляющий страницами и навигацией.

    Управляет переключением между различными страницами (фреймами) приложения.

    Methods:
        show_frame(page): поднимает указанную страницу на передний план.
        init_frames(): инициализирует и сохраняет все страницы приложения.
    """
    def __init__(self) -> None:
        """Инициализировать главное окно приложения."""
        super().__init__()
        self.title('Text scanner')
        self.minsize(600, 400)

        self.container = ttk.Frame(self)
        self.container.pack(expand=True)

        self.frames = self.init_frames()

        self.show_frame(StartPage)

    def show_frame(self, page: Union[StartPage, ImagePage]) -> None:
        """
        Поднять указанную страницу на передний план.

        Args:
            page (Union[StartPage, ImagePage]): страница (фрейм), который необходимо показать.
        """
        frame = self.frames[page]
        frame.tkraise()

    def init_frames(self) -> Dict[ttk.Frame, ttk.Frame]:
        """
        Инициализирует и сохраняет все страницы (фреймы) приложения.

        Returns:
            Dict[ttk.Frame, ttk.Frame]: словарь с экземплярами страниц (фреймов).
        """
        frames = {}
        for F in (StartPage, ImagePage):
            frame = F(self.container, self)
            frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        return frames
