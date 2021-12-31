from flask import Flask
from serendipiart.config import Config


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    from serendipiart.api import routes

    app.register_blueprint(routes.art)

    return app
