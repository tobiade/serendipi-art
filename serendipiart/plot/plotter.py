from typing import Tuple
from serendipiart.plot.shape import Shape
import matplotlib.pyplot as plt
import io


class Plotter:
    def __init__(self, width: int, height: int) -> None:
        self.__width = width
        self.__height = height
        self.__dpi = 300
        pass

    def plot(
        self, xlim: Tuple[int, int], ylim: Tuple[int, int], shapes: list[Shape]
    ) -> io.BytesIO:
        _, ax = plt.subplots(figsize=(self.__width, self.__height), dpi=self.__dpi)
        plt.grid(False)
        plt.axis("off")
        ax.set_aspect("equal")
        ax.set_xlim(*xlim)
        ax.set_ylim(*ylim)

        [
            ax.fill(shape.xcoords, shape.ycoords, facecolor=shape.colour, alpha=0.9)
            for shape in shapes
        ]
        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)
        return buf
