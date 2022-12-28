# Viewer Class
# Diese Klasse erstellt ein Canvas in dem Dinge gezeichnet werden können
# Genauer werden damit z.B. die Staatsgrenze, Sektorgrenzen, usw. gezeichnet
# Außerdem kann man mit der Mouse das Zentrum verschieben und zoomen
from tkinter import Canvas

from GeoPackage import definitions


class ASD(Canvas):
    """ Macht aus einem Standard-Canvas das ASD
        Ermöglicht:
            -) Darstellung von Maps --> Fertig
            -) Diverse Events (Radarmenu, ...)
            -) Darstellung von Flügen (Hinzufügen, Bearbeiten, Löschen)
            -) Berechnet, wo sich Flüge zu einer bestimmten Zeit befinden
            -) Anzeige von LAT/LONG
            -) QDM
            -) SEP
    """

    def __init__(self, main, **kwargs):
        # Canvas initialisieren
        super().__init__()

        self.main = main

        self.__pressed = False
        self.__oldX = 0
        self.__oldY = 0

        self.__latLong = self.create_text(50, 10, text='0', fill='white')
        self.__center = self.create_text(50, 100,
                                         text=f'45 - 17',
                                         fill='red')

        self.bind("<ButtonPress-1>", self.on_mouse_down)
        self.bind("<ButtonPress-2>", self.on_middle_mouse_down)
        self.bind("<ButtonPress-3>", self.on_right_click)
        self.bind("<ButtonRelease-2>", self.on_middle_mouse_up)
        self.bind("<MouseWheel>", self.on_zoom)
        self.bind("<Motion>", self.on_mouse_move)

        self.configure(background="black")
        self.create_oval(100 - 4, 100 - 4, 100 + 4, 100 + 4, outline="white", fill='')

    def on_mouse_move(self, event):
        if self.__pressed :
            # print(event.x - self.__oldX, event.y - self.__oldY)
            self.scan_dragto(event.x, event.y, gain=1)
            self.__oldX = event.x
            self.__oldY = event.y

        self.itemconfig(self.__center,
                        text=f'{self.canvasx(event.x)}/{self.canvasy(event.y)} \n {event.x}/{event.y}')

        self.itemconfig(self.__latLong, text=f'{self.canvasx(event.x)}-{self.canvasy(event.y)}')

    def on_mouse_down(self, event):
        pass

    def on_middle_mouse_down(self, event):
        self.__pressed = True
        self.scan_mark(event.x, event.y)

    def on_middle_mouse_up(self, event):
        self.__pressed = False

    def on_right_click(self, event):
        pass

    def on_zoom(self, event):
        # TODO: Zoom darf nicht auf Punkte, Airports und Flüge angewendet werden
        if (event.delta > 0):
            self.scale("all", event.x, event.y, 1.1, 1.1)
        elif (event.delta < 0):
            self.scale("all", event.x, event.y, 0.9, 0.9)

    def display_map(self):
        pass

    def display_tsa(self):
        pass

    def display_aircraft(self):
        pass
