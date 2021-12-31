from flask import Blueprint, send_file
from serendipiart.artgen.voronoi_artist import VoronoiArtistFactory

art = Blueprint("art", __name__)


@art.route("/art/<seed>", methods=["GET"])
def generate_art(seed: str):
    factory = VoronoiArtistFactory()
    artist = factory.make(int(seed), img_width=10, img_height=10)
    img_bytes = artist.draw()
    return send_file(img_bytes, mimetype="image/png")
