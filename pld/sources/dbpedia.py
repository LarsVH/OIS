import re
import time
from datetime import datetime, date
from SPARQLWrapper import SPARQLWrapper, JSON
from pld.models import *


# TODO: str.format() instead of str % ...


sparql = SPARQLWrapper("http://dbpedia.org/sparql")
preamble = """
"""
_lang_map = {}
_para_map = {}
_type_map = {}
_pers_map = {}
_inst_map = {}
_place_map = {}


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


def _get_name_from_uri(uri):
    # Hacks
    last = uri.split("/")[-1].replace("_", " ")
    full = re.sub(" \(.+\)", "", last)
    parts = full.split(" ")
    return parts[0], " ".join(parts[1:])


def _get_place(uri):
    # TODO: states
    if uri in _place_map:
        return _place_map[uri]
    query = """SELECT * WHERE {{
    <{0}> rdfs:label ?name.
    FILTER(LANG(?name) = "" || LANGMATCHES(LANG(?name), "en"))
    OPTIONAL {{ <{0}> dbpedia-owl:country ?country }}
    OPTIONAL {{ <{0}> dbpedia-owl:postalCode ?pc }}
    }}""".format(uri)
    raw = _perform_query(query)[0]
    country_name = _get_label(raw['country']['value'])
    p = Town(raw['name']['value'].encode('utf-8'), "", country_name)
    _place_map[uri] = p
    return p


def _get_person(uri):
    if uri in _pers_map:
        return _pers_map[uri]
    query = """SELECT * WHERE {{
    OPTIONAL {{ <{0}> foaf:givenName ?gn }}
    OPTIONAL {{ <{0}> foaf:surname ?sn }}
    OPTIONAL {{ <{0}> dbpedia-owl:birthDate ?bd }}
    OPTIONAL {{ <{0}> dbpedia-owl:deathDate ?dd }}
    OPTIONAL {{ <{0}> dbpprop:nationality ?nat }}
    OPTIONAL {{ <{0}> dbpedia-owl:birthPlace ?bp }}}}""".format(uri)
    raw = _perform_query(query)[0]
    if 'gn' in raw and 'sn' in raw:
        gn = raw['gn']['value'].encode('utf-8')
        sn = raw['sn']['value'].encode('utf-8')
    else:
        gn, sn = _get_name_from_uri(uri)
    person = Person(gn, sn)
    if 'bd' in raw:
        date_str = raw['bd']['value']
        date = datetime.strptime(date_str, '%Y-%m-%d+%H:%M').date()
        person.birthday = date
    if 'dd' in raw:
        date_str = raw['dd']['value']
        date = datetime.strptime(date_str, '%Y-%m-%d+%H:%M').date()
        person.deathday = date
    if 'nat' in raw:
        person.nationality = raw['nat']['value']
    if 'bp' in raw:
        person.birthplace = _get_place(raw['bp']['value'])
    _pers_map[uri] = person
    return person


def _get_person_designers(uri):
    query = """SELECT ?x WHERE {
    {<%s> dbpedia-owl:designer ?x} UNION {<%s> dbpedia-owl:developer ?x}.
    ?x rdf:type schema:Person.}""" % (uri,uri)
    raw = _perform_query(query)
    persons = []
    for x in raw:
        x = x['x']
        if not x['type'] == 'uri':
            print uri
            print x
            raise Exception("Result not an uri  (get person designers)")
        persons.append(_get_person(x['value']))
    return persons


def _get_types(uri):
    query = """SELECT ?type WHERE {
    <%s> rdf:type ?d.
    ?d rdfs:label ?type.
    FILTER(LANG(?type) = "" || LANGMATCHES(LANG(?type), "en"))}""" % uri
    raw = _perform_query(query)
    s = set()
    for x in raw:
        s.add(x['type']['value'])
    return s


def _get_institution(uri):
    if uri in _inst_map:
        return _inst_map[uri]
    name = _get_label(uri)
    if name[0:7] == 'http://':
        name = name.split("/")[-1].replace("_", " ")
    types = _get_types(uri)
    if 'company' in types:
        type = InstitutionType.commercial
    elif 'educational institution' in types:
        type = InstitutionType.academic
    else:
        type = InstitutionType.unknown
    obj = Institution(name, type)
    _inst_map[uri] = obj
    return obj


def _get_institution_designers(uri):
    query = """SELECT ?x WHERE {
    {<%s> dbpedia-owl:designer ?x} UNION {<%s> dbpedia-owl:developer ?x}.
    ?x rdf:type schema:Organization.}""" % (uri,uri)
    raw = _perform_query(query)
    institutions = []
    for x in raw:
        x = x['x']
        if not x['type'] == 'uri':
            print uri
            print x
            print Exception("Result not an uri (get institution designers)")
        institutions.append(_get_institution(x['value']))
    return institutions


def _get_langauges():
    query = """SELECT ?y WHERE {
 ?y rdf:type dbpedia-owl:ProgrammingLanguage.
 FILTER (EXISTS {?y dbpprop:paradigm ?x})}"""
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

    designers = _get_person_designers(uri)
    institutions = _get_institution_designers(uri)
    for designer in designers:
        association = DesignedByPerson()
        association.designer = designer
        obj.designers.append(association)
        db.session.add(association)
    for institution in institutions:
        association = DesignedByInstitution()
        association.designer = institution
        obj.institutions.append(association)
        db.session.add(association)

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

if __name__ == '__main__':
    from pld.db import create_tables, drop_tables
    drop_tables()
    create_tables()
    import_source()