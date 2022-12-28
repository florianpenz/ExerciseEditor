class Pos2D:
    """ Klasse, die verwendet wird und zweidimensionale Koordinaten zu speichern
        z.B. als geographische Koordinaten eines Fluges
    """

    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.x = x  # longitutde
        self.y = y  # latitude

    def __repr__(self) -> str:
        return f'Position: {self.x} - {self.y}'


class Position:
    """ Speichert von einem Punkt sowohl die geografischen Koordinaten als auch
        die Koordinaten auf dem Canvas, damit man diese für einen Punkt nur
        einmal berechnen muss und danach immer zur Verfügung hat
    """

    def __init__(self) -> None:
        self.position_name: str = ""  # z.B. LOAG
        self.position_geo = Pos2D()  # Geografische Koordinaten
        self.position_canvas = Pos2D()  # Koordinaten im Canvas

    def clear(self) -> None:
        self.position_canvas.x = 0
        self.position_canvas.y = 0
        self.position_geo.x = 0
        self.position_geo.y = 0
        self.position_name = ""


dummy_position = Position()
dummy_position.position_name = ""
dummy_position.position_geo = Pos2D()
dummy_position.position_canvas = Pos2D()
