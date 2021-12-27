from dataclasses import dataclass
from typing import Tuple


@dataclass
class Shape:
    xcoords: list[float]
    ycoords: list[float]
    colour: Tuple[float, float, float]
