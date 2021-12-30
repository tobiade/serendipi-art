from serendipiart.artgen.voronoi_artist import VoronoiArtistConfig, VoronoiArtist
from serendipiart.plot.plotter import Plotter
from PIL import Image

# For local testing
def run():
    config = VoronoiArtistConfig(seed=100)
    plotter = Plotter(10, 10)
    artist = VoronoiArtist(config, plotter)
    with artist.draw() as img_bytes:
        im = Image.open(img_bytes)
        im.show()
