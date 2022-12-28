""" Funktionen, die verschiedene geografische Berechnungen erledigen

"""

from GeoPackage.definitions import Pos2D


def get_point_from_pdb(point_a: Pos2D, bearing: float, distance: float) -> Pos2D:
    """
    Berechnet die Koordinaten eines sich ergebenden Punktes, aus dem Ursprungspunkt,
    dem Heading und dem Abstand
    :param point_a: Position als Pos2D
    :param bearing: Heading in Grad
    :param distance: Abstand in NM
    :return: Neuer Punkt als Pos2D
    """
    pass

def get_dist_between_points(point_a: Pos2D, point_b: Pos2D) -> float:
    """
    Bestimmt den Abstand zwischen zwei Punkten
    :param point_a: Punkt 1 als Pos2D
    :param point_b: Punkt 2 als Pos2D
    :return: Abstand in NM
    """
    pass

def normalize_coordinates(coords: str) -> float:
    """
    Macht aus diversen Koordinatenformaten eine Koordinate im Format d,dd
    :param coords: Koordinaten (z.B. N45°12'01")
    :return: Koordinaten in Dezimalschreibweise (z.B. 45,2)
    """
    pass

def convert_geo_to_canvas(coords: Pos2D) -> Pos2D:
    """
    Konvertiert geografische Koordinaten in das Koordinatensystem des Canvas
    :param coords: Geo-Koordinaten
    :return: x/y-Koordinaten im Canvas
    """
    pass