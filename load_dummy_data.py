import os
from models import *
from db import db, init_db
from datetime import datetime


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
pittsburgh_usa = add_town("Pittsburgh", "Pennsylvania", "USA", 15100)
frederiksberg_dk = add_town("Frederiksberg", "Seeland" ,"Denmark", 0)
rotterdam_nl = add_town("Rotterdam","Zuid-Holland" ,"Netherlands", 3000)
boston_usa = add_town("Boston", "Massachusetts", "USA", 0200)
winterthur_ch = add_town("Winterthur", "Zurich", "Switzerland", 8400)
kobenhavn_dk = add_town("Kobenhavn", "Hovedstaden", "Denmark", 1000)
hampstead_uk = add_town("Hampstead", "London", "UK", 020) # Postal code incorrect
calgary_ca = add_town("Calgary", "Alberta", "Canada", "T1Y")

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
hrutishauser.birthday = datetime(1918, 1, 9)
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
chkatz.birthday = datetime(1927, 1, 1) # month/year unknown
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

nwirth = add_person("Niklaus", "Wirth")
nwirth.sex = 'male'
nwirth.nationality = "Swiss"
nwirth.birthday = datetime(1934,2,15)
nwirth.birthplace = winterthur_ch

ahejlsberg = add_person("Anders", "Hejlsberg")
ahejlsberg.sex = 'male'
ahejlsberg.nationality = "Danish"
ahejlsberg.birthday = datetime(1960,12,1)
ahejlsberg.birthplace = kobenhavn_dk

# Christopher Strachey Family
chstrachey = add_person("Christopher S.", "Strachey")
chstrachey.sex = 'male'
chstrachey.nationality = "British"
chstrachey.birthday = datetime(1916,11,16)
chstrachey.birthplace = hampstead_uk
chstrachey.deathday = datetime(1975,5,18)

richardstrachey = add_person("Richard", "Strachey")
richardstrachey.sex = 'male'
richardstrachey.nationality = "British"
richardstrachey.birthday = datetime(1817,7,24)

edwardstrachey = add_person("Edward", "Strachey")
edwardstrachey.sex = 'male'
edwardstrachey.nationality = "British"

sirhenrystrachey = add_person("Sir Henry", "Strachey 1st Baronet")
sirhenrystrachey.sex = 'male'
sirhenrystrachey.nationality = "British"
sirhenrystrachey.birthday = datetime(1737,5,23)
sirhenrystrachey.deathday = datetime(1810,1,3)

add_ancestor(richardstrachey, chstrachey)
add_ancestor(edwardstrachey, richardstrachey)
add_ancestor(sirhenrystrachey, edwardstrachey)
#--

jgosling = add_person("James", "Gosling")
jgosling.sex = 'male'
jgosling.nationality = "Canadian"
jgosling.birthday = datetime(1955,5,19)
jgosling.birtplace = calgary_ca

# Institutions
#-----------------------------------------------------------------------------
# Academic
thdarmstadt = add_institution("Technische Hochschule Darmstadt", 'academic')
tumunchen = add_institution("Technische Universitat Munchen", 'academic')
lmumunchen = add_institution("Ludwig-Maximilians-Universitat", 'academic')
coluniversity = add_institution("Columbia University", 'academic')
templeuniversityphil = add_institution("Temple University Philadelphia", 'academic')
upennsylvania = add_institution("University of Pennsylvania", 'academic')
carnegiemellon = add_institution("Carnegie Mellon University Pennsylvania", 'academic')
mit = add_institution("MIT", 'academic')
carnit = add_institution("Carnegie Institute of Technology", 'academic')
yale = add_institution("Yale University", 'academic')
tudelft = add_institution("Delft University of Technology", 'academic')
uamsterdam = add_institution("University of Amsterdam", 'academic')
caltech = add_institution("California Institute of Technology", 'academic')
princentonu = add_institution("Princeton University New Jersey", 'academic')
stanford = add_institution("Stanford University", 'academic')
eth = add_institution("ETH Zurich", 'academic')
lavalcandada = add_institution("Universite Laval Canada", 'academic')
calberkely = add_institution("University of California Berkeley", 'academic')
caldiego = add_institution("University of California San Diego", 'academic')
cambridge = add_institution("University of Cambridge", 'academic')
oxford = add_institution("University of Oxford", 'academic')
calgaryu = add_institution("Calgary University", 'academic')

# Commercial
#-----------------------------------------------------------------------------
ibm = add_institution("IBM", 'commercial')
xerox_parc = add_institution("Xerox Palo Alto Research Center", 'commercial')
softech = add_institution("SofTech Inc", 'commercial')
borlandsoft = add_institution("Borland Software Company", 'commercial')
microsoft = add_institution("Microsoft", 'commercial')
decresearch = add_institution("DEC Systems Research Center SRC", 'commercial')
acornresearch = add_institution("Acorn Research Center", 'commercial')
olivetti = add_institution("Olivetti", 'commercial')
sunms = add_institution("Sun Microsystems", 'commercial')
oracle = add_institution("Oracle Corporation", 'commercial')
google = add_institution("Google", "commercial")


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

add_graduation(nwirth, eth, 1959)
add_graduation(nwirth, lavalcandada, 1959)
add_graduation(nwirth, calberkely, 1963)

add_graduation(chstrachey, cambridge, 1935)

add_graduation(jgosling, calgaryu, 1977)
add_graduation(jgosling, carnegiemellon, 1983)

# Employments
add_employment(fbauer,tumunchen, 1963)
add_employment(fbauer, tumunchen, 1972)

add_employment(jbackus, ibm, 1950)

add_employment(aperlis, carnit, 1956)
add_employment(aperlis, yale, 1971)

add_employment(pnaur, regnecentralendk, 1959)

add_employment(avanwijngaarden, uamsterdam, 1947)

add_employment(jmccarthey, stanford, 1962)

add_employment(nwirth, stanford, 1963)
add_employment(nwirth, eth, 1968)
add_employment(nwirth, xerox_parc, 1976)

add_employment(ahejlsberg, borlandsoft, 1989)
add_employment(ahejlsberg, microsoft, 1996)

add_employment(chstrachey, cambridge, 1962)
add_employment(chstrachey, oxford, 1965)

add_employment(jgosling, sunms, 1984)
add_employment(jgosling, google, 2011)

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

add_award(nwirth, "ACM Turing Award", 1984)


# Languages
###########################################
# Typing Disciplines
duck = create_typing("duck")
strong = create_typing("strong")
weak = create_typing("weak")
static = create_typing("static")
dynamic = create_typing("dynamic")
safe = create_typing("safe")
nominative = create_typing("nominative")
manifest = create_typing("manifest")


# Paradigms
oop = create_paradigm("object-oriented")
fp = create_paradigm("functional")
proc = create_paradigm("procedural")
imp = create_paradigm("imperative")
struct = create_paradigm("structured")
modular = create_paradigm("modular")


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
add_typing(pascal, static)
add_typing(pascal, strong)
add_typing(pascal, safe)
add_paradigm(pascal, imp)
add_paradigm(pascal, struct)


add_designer(pascal, nwirth, 1)

## implementations
hppascal = add_implementation(pascal, "HPPascal")
freepascal = add_implementation(pascal, "FreePascal")
ibmsys370 = add_implementation(pascal, "IBMSystem370")
add_imp_designer(ibmsys370, ibm, 1)

## dialects
turbopascal = add_language("Turbo Pascal", datetime(1983,1,1), dialect_of=pascal)
add_designer(turbopascal, ahejlsberg, 1)
add_designer(turbopascal, ahejlsberg, 2)
add_designer(turbopascal, borlandsoft, 2)

ucsdpascal = add_language("UCSD Pascal", datetime(1978,1,1), dialect_of=pascal)
add_designer(ucsdpascal, caldiego, 1)
add_designer(ucsdpascal, caldiego, 2)
add_designer(ucsdpascal, softech, 2)
add_designer(ucsdpascal, caldiego, 4)
add_designer(ucsdpascal, softech, 4)

### implementation of ucsdpascal
pascalp = add_implementation(ucsdpascal, "Pascal-P")
add_imp_designer(pascalp, caldiego, 1 )
add_imp_designer(pascalp, caldiego, 2 )
add_imp_designer(pascalp, softech, 2)
add_imp_designer(pascalp, caldiego, 4 )
add_imp_designer(pascalp, softech, 4)

## influence
add_influence(pascal, algol)

# CPL
cpl = add_language("CPL", datetime(1963,1,1))
add_designer(cpl, chstrachey, 1)
add_paradigm(cpl, imp)
add_paradigm(cpl, struct)
add_paradigm(cpl, proc)
add_paradigm(cpl, fp)

add_influence(cpl, algol)

# Modula
modula = add_language("Modula", datetime(1975,1,1))
add_designer(modula, nwirth, 1)
add_typing(modula, strong)
add_influence(modula, pascal)

modula2 = add_language("Modula-2", datetime(1978,1,1))
add_designer(modula2, nwirth, 1)
add_typing(modula, strong)
add_typing(modula, static)
add_paradigm(modula2, imp)
add_paradigm(modula2, struct)
add_paradigm(modula2, modular)
add_influence(modula2, algol)
add_influence(modula2, pascal)
add_influence(modula2, modula)

modula25 = add_language("Modula-2+", datetime(1980,1,1))
add_designer(modula25, decresearch, 1)
add_designer(modula25, acornresearch, 1)
add_typing(modula25, strong)
add_typing(modula25, static)
add_paradigm(modula25, imp)
add_paradigm(modula25, struct)
add_paradigm(modula25, modular)
add_influence(modula25, algol)
add_influence(modula25, pascal)
add_influence(modula25, modula2)

modula3 = add_language("Modula-3", datetime(1980,1,1))
add_designer(modula3, decresearch, 1)
add_designer(modula3, olivetti, 1)
add_typing(modula3, strong)
add_typing(modula3, static)
add_typing(modula3, safe)
add_paradigm(modula3, imp)
add_paradigm(modula3, struct)
add_paradigm(modula3, modular)
add_paradigm(modula3, proc)
add_influence(modula3, algol)
add_influence(modula3, pascal)
add_influence(modula3, modula2)
add_influence(modula3, modula25)

# Java
java = add_language("Java", datetime(1995,1,1))
add_typing(java, static)
add_typing(java, strong)
add_typing(java, safe)
add_typing(java, nominative)
add_typing(java, manifest)

add_designer(java, jgosling, 10)
add_designer(java, jgosling, 11)
add_designer(java, jgosling, 12)
add_designer(java, jgosling, 13)
add_designer(java, jgosling, 14)
add_designer(java, jgosling, 50)
add_designer(java, jgosling, 60)
add_designer(java, jgosling, 70)

add_designer(java, sunms, 10)
add_designer(java, sunms, 11)
add_designer(java, sunms, 12)
add_designer(java, sunms, 13)
add_designer(java, sunms, 14)
add_designer(java, sunms, 50)
add_designer(java, sunms, 60)
add_designer(java, sunms, 70)

add_designer(java, oracle, 80)
add_designer(java, oracle, 90)
add_designer(java, oracle, 100)

openjdk = add_implementation(java, "OpenJDK")
add_imp_designer(openjdk, sunms, 60)
add_imp_designer(openjdk, sunms, 70)
add_imp_designer(openjdk, oracle, 80)

add_influence(java, modula3)
add_influence(java, cpp)
add_influence(java, ucsdpascal)


# Ready to commit? I hope you are
db.session.commit()


print "Data loaded"