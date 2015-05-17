import json
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from pld.config import Config
from Queue import Queue
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


@app.route('/api/languages/<int:lang_id>/<int:depth>')
def get_language_graph(lang_id, depth):
    lang = ProgrammingLanguage.query.filter(ProgrammingLanguage.id==lang_id).first()
    if not lang:
        # TODO: Valid error message
        return "Error"
    if not depth >= 1:
        return "Depth must be >= 1"
    ids = set()
    languages = []
    queue = Queue()
    queue.put((depth, lang))
    while not queue.empty():
        d, l = queue.get()
        if d < 0:
            continue
        if l.id in ids:
            continue
        languages.append(l)
        ids.add(l.id)
        for lang in l.influenced_by:
            queue.put((d-1, lang))
    return json.dumps(map(lambda pl: pl.to_dict(), languages))


@app.route('/api/languages/predict/<str>')
def predict(str):
    return json.dumps(ac.search(str, limit=10))


@app.route('/api/designer/all')
def get_designers():
    l1 = map(lambda p: p.to_dict(), Person.query.all())
    l2 = map(lambda p: p.to_dict(), Institution.query.all())
    return json.dumps(l1+l2)


@app.route('/api/designer/person/<int:id>')
def get_person(id):
    def helper(dbp):
        pl = ProgrammingLanguage.query.filter(ProgrammingLanguage.id == dbp.pl_id).first()
        return pl.to_dict()
    person = Person.query.filter(Person.id == id).first()
    if not person:
        # TODO: Valid error message
        return "Error"
    langs = map(helper, person.has_designed)
    return json.dumps(langs)


@app.route('/api/designer/institution/<int:id>')
def get_institution(id):
    def helper(dbp):
        pl = ProgrammingLanguage.query.filter(ProgrammingLanguage.id == dbp.pl_id).first()
        return pl.to_dict()
    institution = Institution.query.filter(Institution.id == id).first()
    if not institution:
        # TODO: Valid error message
        return "Error"
    langs = map(helper, institution.has_designed)
    return json.dumps(langs)