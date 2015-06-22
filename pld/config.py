class Config(object):
    schema_name = None
    # schema_name = 'pld.pld'
    database_uri = 'mysql://%s:%s@%s/%s' % ('root', '', '127.0.0.1', 'ois')
    # database_uri = 'sqlite:////tmp/test.db'
    # database_uri = 'virtuoso://dba:dba@VOS'
