import os
from flask import Flask

from .views import main
from .extensions import db

def create_app(config_file='config'):
    app = Flask(__name__)
    app.config.from_object(config_file)
    
    db.init_app(app)
    
    app.register_blueprint(main)
    
    return app

