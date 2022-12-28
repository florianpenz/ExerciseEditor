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

        self.create_oval(100 - 4, 100 - 4, 100 + 4, 100 + 4, outline="white", fill='')

    def display_map(self):
        pass

    def display_tsa(self):
        pass

    def display_aircraft(self):
        pass
