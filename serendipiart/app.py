from serendipiart.artgen.voronoi_artist import VoronoiArtistFactory
from serendipiart.plot.plotter import Plotter
from PIL import Image

# For local testing
def run():
    factory = VoronoiArtistFactory()
    artist = factory.make(100, 10, 10)
    with artist.draw() as img_bytes:
        im = Image.open(img_bytes)
        im.show()
