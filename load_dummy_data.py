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





# Towns
regensburg_d = add_town("Regensburg", "Bayern", "Germany", 93001)
weinfelden_ch = add_town("Weinfelden", "Thurgau", "Switzerland", 8570)
strasbourg_f = add_town("Strasbourg", "Alsace-Lorraine", "France", 67482)
philadelphia_usa = add_town("Philadelphia", "Pennsylvania", "USA", 19100)
pittsburgh_usa = add_town("Pittsburgh", "Pennsylvania", 15100)
frederiksberg_dk = add_town("Frederiksberg", "Seeland" ,"Denmark", 0)
rotterdam_nl = add_town("Rotterdam","Zuid-Holland" ,"Netherlands", 3000)
boston_usa = add_town("Boston", "Massachusetts", 0200)


# Persons
dritchie = add_person("Dennis", "Ritchie")
dritchie.sex = 'male'
dritchie.nationality = 'American'

bjarne = add_person("Bjarne", "Stroustrup")
bjarne.sex = 'male'
bjarne.nationality = 'American or Swedish'

fbauer = add_person("Friedrich L.", "Bauer")
fbauer.sex = 'male'
fbauer.nationality = "German"
fbauer.birthday = datetime(1924, 6, 10)
fbauer.birthplace = regensburg_d

hbottenbruch = add_person("Herman", "Bottenbruch")
hbottenbruch.sex = 'male'
hbottenbruch.nationality = "German"
hbottenbruch.birthday = datetime(1928, 9, 14)

hrutishauser = add_person("Heinz", "Rutishauser")
hrutishauser.sex = 'male'
hrutishauser.nationality = "Swiss"
hrutishauser.birthday = datetime(1918, 1, 90)
hrutishauser.birthplace = weinfelden_ch
hrutishauser.deathday = datetime(1970, 11, 10)

ksamelson = add_person("Klaus", "Samelson")
ksamelson.sex = 'male'
ksamelson.nationality = "German"
ksamelson.birthplace = strasbourg_f
ksamelson.birthday = datetime(1918,12,21)
ksamelson.deathday = datetime(1980,5,25)

jbackus = add_person("John", "Backus")
jbackus.sex = 'male'
jbackus.nationality = "American"
jbackus.birthplace = philadelphia_usa
jbackus.birthday = datetime(1924,12,3)
jbackus.deathday = datetime(2007,3,17)

chkatz = add_person("Charles", "Katz")
chkatz.sex = 'male'
chkatz.nationality = "American"
chkatz.birthday = datetime(1927) # month/year unknown
chkatz.birthplace = philadelphia_usa

aperlis = add_person("Alan", "Perlis")
aperlis.sex = 'male'
aperlis.nationality = "American"
aperlis.birthday = datetime(1922,4,1)
aperlis.birthplace = pittsburgh_usa
aperlis.deathday = datetime(1990,2,7)

pnaur = add_person("Peter", "Naur")
pnaur.sex = 'male'
pnaur.nationality = "Danish"
pnaur.birthplace = frederiksberg_dk
pnaur.birthday = datetime(1928,10,25)

avanwijngaarden = add_person("Adriaan", "Van Wijngaarden")
avanwijngaarden.sex = 'male'
avanwijngaarden.nationality = "Dutch"
avanwijngaarden.birthday = datetime(1916,11,2)
avanwijngaarden.birthplace = rotterdam_nl
avanwijngaarden.deathday = datetime(1987,2,7)

# John McCarthey Family
jmccarthey = add_person("John", "McCarthy")
jmccarthey.sex = 'male'
jmccarthey.nationality = "American"
jmccarthey.birthday = datetime(1927,9,4)
jmccarthey.birthplace = boston_usa
jmccarthey.deathday = datetime(2011,10,24)

johnpatrick = add_person("John", "Patrick")
johnpatrick.sex = 'male'
idaglattmccarthy = add_person("Ida G.", "McCarthy")
idaglattmccarthy.sex = 'female'

add_ancestor(johnpatrick,jmccarthey)
add_ancestor(idaglattmccarthy, jmccarthey)
#---


# Institutions
#-----------------------------------------------------------------------------
# Academic
thdarmstadt = add_institution("Technische Hochschule Darmstadt", 'academic')
tumunchen = add_institution("Technische Universitat Munchen", 'academic')
lmumunchen = add_institution("Ludwig-Maximilians-Universitat", 'academic')
coluniversity = add_institution("Columbia University", 'academic')
templeuniversityphil = add_institution("Temple University Philadelphia", 'academic')
upennsylvania = add_institution("University of Pennsylvania", 'academic')
carnegiemellon = add_institution("Carnegie Mellon University Pennsylvania")
mit = add_institution("MIT", 'academic')
carnit = add_institution("Carnegie Institute of Technology", 'academic')
yale = add_institution("Yale University", 'academic')
tudelft = add_institution("Delft University of Technology", 'academic')
uamsterdam = add_institution("University of Amsterdam", 'academic')
caltech = add_institution("California Institute of Technology", 'academic')
princentonu = add_institution("Princeton University New Jersey", 'academic')
stanford = add_institution("Stanford University", 'academic')


# Commercial
#-----------------------------------------------------------------------------
ibm = add_institution("IBM", 'commercial')

# Public
#-----------------------------------------------------------------------------
regnecentralendk = add_institution("Regnecentralen Denmark", 'public')

# Graduations
add_graduation(hbottenbruch, thdarmstadt, 1957)

add_graduation(fbauer, lmumunchen, 1950)

add_graduation(ksamelson, lmumunchen, 1950) # year estimated

add_graduation(jbackus, coluniversity, 1949)

add_graduation(chkatz, templeuniversityphil, 1950)
add_graduation(chkatz, upennsylvania, 1953)

add_graduation(aperlis, carnegiemellon, 1943)
add_graduation(aperlis, mit, 1949)

add_graduation(avanwijngaarden, tudelft, 1939)

add_graduation(jmccarthey, caltech, 1948)
add_graduation(jmccarthey, princentonu, 1951)


# Employments
add_employment(fbauer,tumunchen, 1963)
add_employment(fbauer, tumunchen, 1972)

add_employment(jbackus, ibm, 1950)

add_employment(aperlis, carnit, 1956)
add_employment(aperlis, yale, 1971)

add_employment(pnaur, regnecentralendk, 1959)

add_employment(avanwijngaarden, uamsterdam, 1947)

add_employment(jmccarthey, stanford, 1962)

# Awards
#---------------------------------------------------------
add_award(fbauer, "Iron Cross 2nd Class", 1944)
add_award(fbauer, "Bundesverdienstkreuz 1st Class", 1982)
add_award(fbauer, "IEEE Computer Pioneer Award", 1988)

add_award(jbackus, "National Medal of Science", 1975)
add_award(jbackus, "ACM Turing Award", 1977)

add_award(aperlis, "ACM Turing Award", 1966)
add_award(aperlis, "Computer Pioneer Award", 1985)

add_award(pnaur, "ACM Turing Award", 2005)

add_award(avanwijngaarden, "IEEE Computer Pioneer Award", 1986)

add_award(jmccarthey, "ACM Turing Award", 1971)
add_award(jmccarthey, "IEEE Computer Pioneer Award", 1985)


# Languages
###########################################
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
struct = create_paradigm("structured")




# C
C = add_language("C", datetime(1970, 1, 1))
add_designer(C, dritchie, 1)
add_typing(C, static)
add_typing(C, strong)
add_paradigm(C, imp)

# C++
cpp = add_language("C++", datetime(1979, 1, 1))
add_designer(cpp, bjarne, 1)
add_typing(cpp, static)
add_typing(cpp, strong)
add_influence(cpp, C)
add_paradigm(cpp, imp)
add_paradigm(cpp, oop)

# Algol
algol = add_language("ALGOL", datetime(1958, 1, 1))

add_designer(algol, fbauer, 60)
add_designer(algol, hbottenbruch, 60)
add_designer(algol, hrutishauser, 60)
add_designer(algol,ksamelson, 60)
add_designer(algol,jbackus, 60)
add_designer(algol, chkatz, 60)
add_designer(algol, aperlis, 60)
add_designer(algol, pnaur, 60)
add_designer(algol, avanwijngaarden, 60)
add_designer(algol, jmccarthey, 60)

add_paradigm(algol, proc)
add_paradigm(algol, imp)
add_paradigm(algol, struct)

add_influence(C, algol)



# Pascal
pascal = add_language("Pascal", datetime(1970,1,1))

add_influence(pascal, algol)

# CPL
cpl = add_language("CPL", datetime(1963,1,1))


add_influence(cpl, algol)

# Ready to commit? I hope you are
db.session.commit()


print "Data loaded"