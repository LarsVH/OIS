from app import app
from flask.ext.sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@%s/%s' % ('root', '', '127.0.0.1', 'ois')
db = SQLAlchemy(app)


def init_db():
    import models
    db.create_all()