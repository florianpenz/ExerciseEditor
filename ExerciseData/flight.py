from dataclasses import dataclass

import GeoPackage.definitions
import GeoPackage.definitions as geo_def


@dataclass
class Flight:
    """ Diese Klasse speichert alle Informationen eines einzelnen Fluges:
            -) Elemente aus der Excel Datei (ADEP, C/S,...)
            -) Informationen die für die Darstellung benötigt werden
                (aktuelle Position,...)
    """
    # -------------------------------------------------------
    # Aircraft Properties für Darstellung
    # -------------------------------------------------------

    start_position_coordinates: geo_def.Position() = GeoPackage.definitions.dummy_position
    adep_coordinates: geo_def.Position() = GeoPackage.definitions.dummy_position
    best_route_coordinates = []
    ades_coordinates: geo_def.Position() = GeoPackage.definitions.dummy_position
    copn_coordinates: geo_def.Position() = GeoPackage.definitions.dummy_position

    # Aktuelle Position
    actual_position: geo_def.Position() = GeoPackage.definitions.dummy_position

    # FPL-Data
    ID: int = 0
    callsign: str = ""
    type: str = ""
    starttime: str = ""
    start_position: str = ""
    adep: str = ""
    best_route: str = ""
    icao_route: str = ""
    ades: str = ""
    afl: str = ""
    cfl: str = ""
    rfl: str = ""
    ssr_allocated: str = ""
    ssr_equipment: str = ""
    frequency: str = ""
    field18switches: str = ""
    pilot_remarks: str = ""
    flight_rule: str = ""
    flight_type: str = ""
    brnav: bool = True
    prnav: bool = False
    eight33: bool = False
    uhf: bool = False
    rvsm: bool = True
    target_speed: str = ""
    formation_data: str = ""
    sectors: str = ""
    frqSectors: str = ""
    disregardFpl: bool = False
    color: str = ""
    user_defined_script: str = ""  # TODO: Eigene Klasse für Scripts bauen
    pel: str = ""
    copn: str = ""
    firn: str = ""
    speed: str = ""
    starting_outside_fir: bool = True
    cof: bool = False
    registr = ""
    ation: str = ""
    cpdlc: bool = False
    ofl: str = ""
    nat_track: str = ""
    oceanic_restriction: str = ""
