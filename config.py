import os

SQLALCHEMY_TRACK_MODIFICATIONS = True

uri = os.getenv("DATABASE_URL")
LOCAL = uri is None
if LOCAL: # app de test
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(basedir, "app.db")}'
else: # vraie app
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    SQLALCHEMY_DATABASE_URI = uri
