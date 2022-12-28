from ExerciseView.exerciseeditor import ExerciseEditor

def checkresourcesavailable() -> bool:
    # TODO: Überprüfung einbauen
    return True


if __name__ == "__main__":
    """ Entrypoint des Programms
        Zuerst wird gecheckt, ob alle Resourcen vorhanden sind (z.B: Ordner mit Maps)
        und nur dann wird das Programm gestartet
        Fehlen Resourcen, wird eine Fehlermeldung ausgegeben und das Programm beendet
    """

    if checkresourcesavailable():
        # appMain ist die Hauptklasse, die das Fenster zeichnet - PF

        win = ExerciseEditor()
        win.main_root.mainloop()
    else:
        # TODO: Fehlermeldung ausgeben
        pass
