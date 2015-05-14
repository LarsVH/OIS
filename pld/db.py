from pld.app import db


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