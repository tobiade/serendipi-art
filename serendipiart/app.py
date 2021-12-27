from serendipiart.artgen.artist import VoronoiArtistConfig, VoronoiArtist
from serendipiart.plot.plotter import Plotter


def run():
    config = VoronoiArtistConfig(seed=100)
    plotter = Plotter(10, 10)
    artist = VoronoiArtist(config, plotter)
    artist.draw()
