from datetime import datetime
from db import db
from models import *


# Helper functions
def add(obj):
    db.session.add(obj)
    db.session.flush()


def add_institution(name, type):
    inst = Institution(name, type)
    add(inst)
    return inst


def add_language(name, date, dialect_of=None):
    if dialect_of:
        dialect_of = dialect_of.id

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
        add(association)
    else:
        association = DesignedByInstitution(version=version)
        association.designer = designer
        lang.institutions.append(association)
        add(association)


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
    add(association)


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
            person_id=designer.id)
        add(association)
    else:
        association = ImplementationVersionDesignedByInst(
            version=version, implementation_id=implementation.id,
            institution_id=designer.id)
        add(association)