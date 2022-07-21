from datetime import datetime
import logging as lg

from .extensions import db

db.create_all()

def init_db():
    db.drop_all()
    db.create_all()
    db.session.commit()
    lg.warning('Database initialized!')

