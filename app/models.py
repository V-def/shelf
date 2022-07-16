from flask_sqlalchemy import SQLAlchemy

import logging as lg

from .views import app

db = SQLAlchemy(app)

class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    def __init__(self, title, description):
        self.title = title
        self.description = description

db.create_all()

def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(Content("Livre exemple 1", "Ce livre est un exemple"))
    db.session.commit()
    lg.warning('Database initialized!')
