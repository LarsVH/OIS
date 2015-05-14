from pld.app import app
from flask.ext.sqlalchemy import SQLAlchemy


# TODO: Config file
db_backend = 'mysql'
db = None
schema_name = None


if db_backend == 'virtuoso':
    # TODO: SFW wachtwoord voor deliverable
    app.config['SQLALCHEMY_DATABASE_URI'] = 'virtuoso://dba:ditishetwachtwoordkut@VOS'
    db = SQLAlchemy(app)
    schema_name = 'pld.pld'
elif db_backend == 'mysql':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@%s/%s' % ('root', '', '127.0.0.1', 'ois')
    db = SQLAlchemy(app)
elif db_backend == 'sqlite':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    db = SQLAlchemy(app)
else:
    raise Exception("Incorrect database backend")


db.metadata.schema = schema_name
db.schema = schema_name


def create_tables():
    import pld.models
    db.create_all()


def drop_tables():
    import pld.models
    db.drop_all()


def clear_tables():
    import pld.models
    con = db.engine.connect()
    trans = con.begin()
    tables = db.metadata.sorted_tables
    tables.reverse()
    try:
        # TODO: test for virtuoso/sqlite
        con.execute("SET foreign_key_checks = 0;")
        for table in tables:
            con.execute(table.delete())
        con.execute("SET foreign_key_checks = 1;")
    except Exception:
        trans.rollback()
    finally:
        trans.close()
        con.close()