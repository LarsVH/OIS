import os
from models import *
from db import db, init_db
from datetime import datetime


# Helper functions
def add(obj):
    db.session.add(obj)


def add_institution(name, type):
    inst = Institution(name, type)
    add(inst)
    return inst


def add_language(name, date, dialect_of=None):
    lang = ProgrammingLanguage(name, date, dialect_of)
    add(lang)
    return lang


def add_person(firstname, lastname):
    person = Person(firstname, lastname)
    add(person)
    return person


def add_town(name, state, country, postal_code):
    town = Town(name, state, country)
    town.postal_code = postal_code
    add(town)
    return town


def add_designer(lang, designer, version):
    if type(designer) == Person:
        association = DesignedByPerson(version=version)
        association.designer = designer
        lang.designers.append(association)
    else:
        association = DesignedByInstitution(version=version)
        association.designer = designer
        lang.institutions.append(association)


def create_typing(name):
    t = TypingDiscipline(name)
    add(t)
    return t


def create_paradigm(name):
    p = Paradigm(name)
    add(p)
    return p


def add_typing(lang, discipline):
    lang.disciplines.append(discipline)


def add_paradigm(lang, paradigm):
    lang.paradigms.append(paradigm)


def add_influence(lang1, lang2):
    lang1.influenced_by.append(lang2)


def add_ancestor(parent, child):
    child.parents.append(parent)


def add_graduation(person, institution, year):
    association = Graduation(year=year)
    association.institution = institution
    person.graduations.append(association)


def add_award(person, name, year):
    a = Award(name, person.id, year)
    add(a)
    return a


def add_implementation(lang, name):
    imp = Implementation(name, lang.id)
    add(imp)
    return imp

def add_employment(person, institution, year):
    emp = Employment(institution.id, person.id, year)
    add(emp)
    return emp

def add_phonenumber(person, number):
    num = PhoneNumber(person.id, number)
    add(num)
    return num


def add_emailaddress(person, email):
    e = EmailAddress(person.id, email)
    add(e)
    return e

def add_address(person, town, street, number):
    a = Address(person.id, town.id, street, number)
    add(a)
    return a


def add_imp_designer(implementation, designer, version):
    if type(designer) == Person:
        association = ImplementationVersionDesignedBy(
            version=version, implementation_id=implementation.id,
            person_id=designers.id)
        add(association)
    else:
        association = ImplementationVersionDesignedByInst(
            version=version, implementation_id=implementation.id,
            institution_id=designers.id)
        add(association)


# And code
try:
    os.remove("/tmp/test.db")
except:
    pass

init_db()

# Typing Disciplines
duck = create_typing("duck")
strong = create_typing("strong")
weak = create_typing("weak")
static = create_typing("static")
dynamic = create_typing("dynamic")


# Paradigms
oop = create_paradigm("object-oriented")
fp = create_paradigm("functional")
proc = create_paradigm("procedural")
imp = create_paradigm("imperative")


# Persons
dritchie = add_person("Dennis", "Ritchie")
dritchie.sex = 'male'
dritchie.nationality = 'American'

bjarne = add_person("Bjarne", "Stroustrup")
bjarne.sex = 'male'
bjarne.nationality = 'American or Swedish'


# Languages
C = add_language("C", datetime(1970, 1, 1))
add_designer(C, dritchie, 1)
add_typing(C, static)
add_typing(C, strong)
add_paradigm(C, imp)

cpp = add_language("C++", datetime(1979, 1, 1))
add_designer(cpp, bjarne, 1)
add_typing(cpp, static)
add_typing(cpp, strong)
add_influence(cpp, C)
add_paradigm(cpp, imp)
add_paradigm(cpp, oop)


# Ready to commit? I hope you are
db.session.commit()


print "Data loaded"