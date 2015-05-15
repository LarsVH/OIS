import json
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from pld.config import Config
from walrus import Database

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.database_uri
db = SQLAlchemy(app)
db.metadata.schema = Config.schema_name
db.schema = Config.schema_name

from pld.models import *


database = None
ac = None


@app.before_first_request
def init_autocompletion():
    print "Initializing autocomplete data..."
    global ac
    global database
    database = Database(db=3)
    ac = database.autocomplete()
    for pl in ProgrammingLanguage.query.all():
        metadata = {
            'name':pl.name,
            'id':pl.id}
        ac.store(
            pl.name,
            data=metadata)


@app.route('/')
def hello_world():
    return "Serve static content"


@app.route('/api/languages/')
def get_languages():
    langs = ProgrammingLanguage.query.all()
    return json.dumps(map(lambda pl: pl.to_dict(), langs))


@app.route('/api/languages/<int:lang_id>')
def get_language(lang_id):
    lang = ProgrammingLanguage.query.filter(ProgrammingLanguage.id==lang_id).first()
    if lang:
        return json.dumps(lang.to_dict(extended=True))
    else:
        # TODO: Valid error message
        return "Error"


@app.route('/api/languages/predict/<str>')
def predict(str):
    return json.dumps(ac.search(str, limit=10))