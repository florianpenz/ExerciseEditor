import math
import tkinter as tk

import ttkbootstrap as tb

from ExerciseView.asd import ASD


class ExerciseEditor:
    def __init__(self) -> None:
        # Fenster erstellen
        self.main_root = tb.Window(themename='solar')

        self.main_root.title('Excercise Editor V1.00 - C PF')
        self.main_root.minsize(1600, 850)

        self.__createMainWindow()
        self.__createMainMenu()

        self.numberOfScreens = math.floor(self.main_root.maxsize()[0] / self.main_root.winfo_screenwidth())

        self.main_root.protocol("WM_DELETE_WINDOW", self.__on_window_close)

    def __createMainWindow(self) -> None:
        # Hauptfenster erstellen
        self.main_root.state('zoomed')

        tb.Label(self.main_root, text="Exercise Editor V1").pack()

        self.__ASD = ASD(self.main_root)
        self.__ASD.pack()

    def __createMainMenu(self) -> None:
        # Menü erstellen
        self.main_menu = tk.Menu(self.main_root)
        self.main_root.config(menu=self.main_menu)

        # FILE
        file_menu = tk.Menu(self.main_menu, tearoff=0)

        self.main_menu.add_cascade(label='File', menu=file_menu)

        file_menu.add_command(label='New...', command=self.__menu_new_file)
        file_menu.add_separator()
        file_menu.add_command(label='Open...', command=self.__menuOpenFile)
        file_menu.add_command(label='Save...', command=self.__menu_save_file)
        file_menu.add_command(label='Save as...', command=self.__menu_save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label='Close', command=self.__menuCloseMain)

        # VIEW
        view_menu = tk.Menu(self.main_menu, tearoff=0)

        self.main_menu.add_cascade(label='View', menu=view_menu)

        view_menu.add_command(label='Property Inspector')

        # EXERCISE
        exercise_menu = tk.Menu(self.main_menu, tearoff=0)

        self.main_menu.add_cascade(label='Exercise', menu=exercise_menu)

        exercise_menu.add_command(label='New empty flight')
        exercise_menu.add_command(label='New flight from template')
        exercise_menu.add_command(label='New background flights')
        exercise_menu.add_command(label='Delete all flights')
        exercise_menu.add_separator()
        exercise_menu.add_command(label='Weather settings')

    def __menuCloseMain(self):
        self.main_root.quit()

    def __menuOpenFile(self):
        """ Lädt ein Beispiel aus einer Excel-Datei
        """
        pass

    def __menu_save_file(self):
        pass

    def __menu_save_as_file(self):
        pass

    def __menu_new_file(self):
        pass

    def __on_window_close(self):
        self.main_root.destroy()

    def __main_on_key_press(self, event):
        pass


class Singleton:
    """
    TODO: Singleton muss einen Parameter weiter geben, damit der erste Buchstabe gleich im Fenster steht

    """

    def __init__(self, decorated):
        self._decorated = decorated

    def instance(self):
        """
        Returns the singleton instance. Upon its first call, it creates a
        new instance of the decorated class and calls its `__init__` method.
        On all subsequent calls, the already created instance is returned.

        """
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)


@Singleton
class clsSearchWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()

        # ToDo: Suchfenster muss in der Mitte des Bildschirms aufgehen
        self.geometry('+500+500')
        self.overrideredirect(True)

        self.__searchEntry = tk.Entry(self)
        self.__searchEntry.pack()

        self.__searchEntry.focus_set()

        self.__searchEntry.bind("<Return>", self.__startSearch)

    def __startSearch(self, event):
        self.destroy()
