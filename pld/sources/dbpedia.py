import time
from SPARQLWrapper import SPARQLWrapper, JSON
from pld.models import *


sparql = SPARQLWrapper("http://dbpedia.org/sparql")
preamble = """PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>
PREFIX dbpprop: <http://dbpedia.org/property/>
PREFIX dbres: <http://dbpedia.org/resource/>
"""
_lang_map = {}
_para_map = {}
_type_map = {}


def create_limiter(func, limit):
    create_limiter.last = int(time.time())
    create_limiter.hits = 0

    def wrapped():
        current = int(time.time())
        if (current - create_limiter.last) > 1:
            create_limiter.last = current
            create_limiter.hits = 0
        if create_limiter.hits > limit:
            time.sleep(1)
            return wrapped()
        create_limiter.hits += 1
        return func()
    return wrapped


sparql.query = create_limiter(sparql.query, 25)


def _perform_query(q):
    sparql.setQuery(preamble+q)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results["results"]["bindings"]


def _get_langauges():
    query = """SELECT ?y WHERE {
 ?y rdf:type dbpedia-owl:ProgrammingLanguage.
 FILTER (EXISTS {?y dbpprop:paradigm ?x})
 }
"""
    raw = _perform_query(query)
    results = map(lambda e: e['y']['value'], raw)
    return results


def _get_influences(uri, obj):
    query = """SELECT ?y WHERE {
 <%s> dbpedia-owl:influencedBy ?y.
 }
""" % uri
    raw = _perform_query(query)
    uris = map(lambda e: e['y']['value'].encode('utf-8'), raw)
    objs = map(_lang_map.get, uris)
    objs = filter(lambda e: True if e else False, objs)
    # TODO: misschien moet dit een merge zijn
    obj.influenced_by = objs


def _get_label(uri):
    raw = _perform_query("""SELECT ?label WHERE{
    <%s> rdfs:label ?label.
    FILTER(LANG(?label) = "" || LANGMATCHES(LANG(?label), "en"))}"""%uri)
    if len(raw) == 0:
        print "No label found for %s" % uri
        return uri
        #raise Exception("_get_label: Error with %s"%uri)
    name = raw[0]['label']['value']
    return name.encode('utf-8')


def _get_paradigms(uri):
    raw = _perform_query("""SELECT ?label WHERE{
    <%s> dbpprop:paradigm ?para.
    ?para rdfs:label ?label.
    FILTER(LANG(?label) = "" || LANGMATCHES(LANG(?label), "en"))}"""%uri)
    paradigms = []
    for para in raw:
        name = para['label']['value'].encode('utf-8')
        if name in _para_map:
            obj = _para_map[name]
        else:
            obj = Paradigm(name)
            _para_map[name] = obj
        paradigms.append(obj)
    return paradigms


def _get_disciplines(uri):
    raw = _perform_query("""SELECT ?label WHERE{
    <%s> dbpprop:typing ?para.
    ?para rdfs:label ?label.
    FILTER(LANG(?label) = "" || LANGMATCHES(LANG(?label), "en"))}"""%uri)
    disciplines = []
    for type in raw:
        name = type['label']['value'].encode('utf-8')
        if name in _type_map:
            obj = _type_map[name]
        else:
            obj = TypingDiscipline(name)
            _type_map[name] = obj
        disciplines.append(obj)
    return disciplines


def _get_language_object(uri):
    obj = ProgrammingLanguage(_get_label(uri))
    obj.paradigms = _get_paradigms(uri)
    obj.disciplines = _get_disciplines(uri)
    _lang_map[uri] = obj
    return obj


def import_source():
    from pld.app import db
    langs = _get_langauges()
    #langs = ["http://dbpedia.org/resource/Python_(programming_language)"]
    lang_objects = map(_get_language_object, langs)
    #print _lang_map
    #print _para_map
    for uri, obj in _lang_map.iteritems():
        _get_influences(uri, obj)
    for obj in lang_objects:
        db.session.add(obj)
    db.session.commit()


from pld.db import create_tables, drop_tables
drop_tables()
create_tables()
import_source()
