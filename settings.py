from flask import Flask
from config import app_config

build_version = "Build Version: 1.0.0 (A) Build Date:22 Dec 2023."

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(app_config['config'])

def get_app():
    from movie_recommendation_app import routes
    return app
