import os
from models import *
from db import db, init_db
from datetime import datetime


# Helper functions
def add(obj):
    db.session.add(obj)


def add_designer(lang, person, version):
    association = DesignedByPerson(version=version)
    association.designer = person
    lang.designers.append(association)


def add_typing(lang, discipline):
    lang.disciplines.append(discipline)


def add_paradigm(lang, paradigm):
    lang.paradigms.append(paradigm)

def add_influence(lang1, lang2):
    lang1.influenced_by.append(lang2)

# And code
try:
    os.remove("/tmp/test.db")
except:
    pass

init_db()

# Typing Disciplines
duck = TypingDiscipline("duck typing")
strong = TypingDiscipline("strong typing")
weak = TypingDiscipline("weak typing")
static = TypingDiscipline("static typing")
dynamic = TypingDiscipline("dynamic typing")
add(dynamic)
add(static)
add(weak)
add(strong)
add(duck)


# Paradigms
pass

# Persons
ritchie = Person("Dennis", "Ritchie")
ritchie.sex = 'male'
ritchie.nationality = 'American'
add(ritchie)

bjarne = Person("Bjarne", "Ietsmetsoep")
bjarne.sex = 'male'
bjarne.nationality = 'American or Swedish'
add(bjarne)


# Languages
C = ProgrammingLanguage("C", datetime(1970, 1, 1))
add_designer(C, ritchie, 1)
add_typing(C, static)
add_typing(C, strong)
add(C)

cpp = ProgrammingLanguage("C++", datetime(1979, 1, 1))
add_designer(cpp, bjarne, 1)
add_typing(cpp, static)
add_typing(cpp, strong)
add_influence(cpp, C)
add(cpp)


# Ready to commit? I hope you are
db.session.commit()