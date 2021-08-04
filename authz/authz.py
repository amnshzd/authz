from flask import Flask
from authz.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Load Configuration from environment variable
    return app