from ExerciseData import flight


class Exercise:
    """ Diese Klasse speichert ein Simulator-Beispiel.
        Einerseits grundlegende Einstellungen, wie Beispielname
        als auch die eigentlichen Flüge in Form einer Liste mit
        Flight-Objekten
    """

    def __init__(self) -> None:
        # Speichert die Flüge in Form von clsFlight-Objekten
        self.flights: list = [flight]
        self.filename: str = ""
        self.exercise_name: str = ""
        self.num_of_flights: int = 0
        self.exercise_loaded: bool = False
        self.exercise_saved: bool = True

    def new_exercise(self) -> None:
        pass

    def load_exercise(self) -> None:
        pass

    def save(self) -> None:
        pass

    def save_as(self) -> None:
        pass
