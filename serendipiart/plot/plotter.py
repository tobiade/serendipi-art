from typing import Tuple

from matplotlib.figure import Figure
from serendipiart.plot.shape import Shape
import io


class Plotter:
    def __init__(self, width: int, height: int) -> None:
        self.__width = width
        self.__height = height
        self.__dpi = 300
        pass

    def plot(
        self,
        xlim: Tuple[int, int],
        ylim: Tuple[int, int],
        title: str,
        shapes: list[Shape],
    ) -> io.BytesIO:
        figure = Figure(figsize=(self.__width, self.__height), dpi=self.__dpi)  # type: ignore
        ax = figure.subplots()
        ax.set_aspect("equal")
        ax.set_xlim(*xlim)
        ax.set_ylim(*ylim)
        ax.set_axis_off()

        [
            ax.fill(shape.xcoords, shape.ycoords, facecolor=shape.colour, alpha=0.9)
            for shape in shapes
        ]
        buf = io.BytesIO()
        figure.suptitle(
            title,
            fontsize=20,
            family="Futura",
        )
        figure.tight_layout()
        figure.savefig(buf, format="png", bbox_inches="tight", pad_inches=0.3)
        buf.seek(0)
        return buf
