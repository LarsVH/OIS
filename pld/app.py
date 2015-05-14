import json
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from pld.config import Config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.database_uri
db = SQLAlchemy(app)
db.metadata.schema = Config.schema_name
db.schema = Config.schema_name

from pld.models import *


@app.route('/')
def hello_world():
    return "Serve static content"


@app.route('/api/languages/')
def get_languages():
    langs = ProgrammingLanguage.query.all()
    return json.dumps(map(lambda pl: pl.to_dict(), langs))


@app.route('/api/languages/<int:lang_id>')
def get_language(lang_id):
    return "Information on a language in JSON"