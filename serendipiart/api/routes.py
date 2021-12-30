from flask import Blueprint, send_file
from serendipiart.artgen.voronoi_artist import VoronoiArtist, VoronoiArtistConfig
from serendipiart.plot.plotter import Plotter

art = Blueprint("art", __name__)


@art.route("/art/<seed>", methods=["POST"])
def generate_art(seed):
    config = VoronoiArtistConfig(seed=int(seed))
    plotter = Plotter(10, 10)
    artist = VoronoiArtist(config, plotter)
    img_bytes = artist.draw()
    return send_file(img_bytes, mimetype="image/png")
