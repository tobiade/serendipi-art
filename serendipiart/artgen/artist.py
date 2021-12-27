import numpy as np
import numpy.typing as npt
from dataclasses import dataclass
from scipy.spatial import Voronoi
from serendipiart.plot.plotter import Plotter
from serendipiart.plot.shape import Shape
from PIL import Image


@dataclass
class VoronoiArtistConfig:
    seed: int
    num_points: int = 200
    x_lim: int = 13
    y_lim: int = 16


class VoronoiArtist:
    X_BUFFER = 2.5
    Y_BUFFER = 2.5

    def __init__(self, config: VoronoiArtistConfig, plotter: Plotter) -> None:
        self.__config = config
        self.__plotter = plotter

    def __generate_points(self) -> npt.NDArray:
        x_bounds, y_bounds = self.__bounds()

        num_points = self.__config.num_points
        x = np.random.uniform(*x_bounds, size=num_points).reshape((num_points, 1))
        y = np.random.uniform(*y_bounds, size=num_points).reshape((num_points, 1))
        pts = np.hstack([x, y])
        return pts

    def __construct_voronoi(self, coords) -> npt.NDArray:
        vor = Voronoi(coords)
        vertices = vor.vertices  # type: ignore
        shape_indexes = vor.regions  # type: ignore

        shape_indexes = [s for s in shape_indexes if len(s) > 0 and -1 not in s]

        shapes: npt.NDArray = np.array(
            [vertices[s] for s in shape_indexes], dtype=object
        )
        return shapes

    def __bounds(self) -> tuple[npt.NDArray[np.int64], npt.NDArray[np.int64]]:
        x_bounds: npt.NDArray[np.int64] = np.array([0, self.__config.x_lim])
        y_bounds: npt.NDArray[np.int64] = np.array([0, self.__config.y_lim])
        return x_bounds, y_bounds

    def __create_voronoi_shapes(self, regions: npt.NDArray) -> list[Shape]:
        # close the region by appending first point in region to the end of its points e.g [[(1,2), (2,4)]] -> [[(1,2), (2,4), (1,2)]]
        closed_regions = [np.append(region, region[0:1], axis=0) for region in regions]
        # seed random number generator and use it to generate colours
        rng = np.random.default_rng(seed=self.__config.seed)
        shapes = [
            Shape(
                xcoords=closed_region[:, 0],
                ycoords=closed_region[:, 1],
                colour=(rng.random(), rng.random(), rng.random()),
            )
            for closed_region in closed_regions
        ]
        return shapes

    def draw(self):
        points = self.__generate_points()
        regions = self.__construct_voronoi(points)
        shapes = self.__create_voronoi_shapes(regions)

        x_bounds, y_bounds = self.__bounds()
        xlim = x_bounds + np.array([self.X_BUFFER, -self.X_BUFFER])
        ylim = y_bounds + np.array([self.Y_BUFFER, -self.Y_BUFFER])

        with self.__plotter.plot(
            (xlim[0], xlim[1]), (ylim[0], ylim[1]), shapes
        ) as img_bytes:
            im = Image.open(img_bytes)
            im.show()
