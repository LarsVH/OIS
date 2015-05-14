from pld.app import db
from pld.config import Config

schema_name = Config.schema_name

# http://stackoverflow.com/a/5652169/2787432
Influence = db.Table(
    'Influence', db.Model.metadata,
    db.Column('HasInfluenced', db.Integer, db.ForeignKey('ProgrammingLanguage.id')),
    db.Column('InfluencedBy', db.Integer, db.ForeignKey('ProgrammingLanguage.id')))
Ancestor = db.Table(
    'Ancestor', db.Model.metadata,
    db.Column('Parent', db.Integer, db.ForeignKey('Person.id')),
    db.Column('Child', db.Integer, db.ForeignKey('Person.id')))
FollowsParadigm = db.Table(
    'FollowsParadigm', db.Model.metadata,
    db.Column('pl_id', db.Integer, db.ForeignKey('ProgrammingLanguage.id')),
    db.Column('pa_id', db.Integer, db.ForeignKey('Paradigm.id')))
HasTypingDiscipline = db.Table(
    'HasTypingDiscipline', db.Model.metadata,
    db.Column('pl_id', db.Integer, db.ForeignKey('ProgrammingLanguage.id')),
    db.Column('td_id', db.Integer, db.ForeignKey('TypingDiscipline.id')))


class Institution(db.Model):
    __tablename__ = "Institution"
    __schema__ = schema_name

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    type = db.Column(db.Enum('academic', 'commercial', 'public', name='institution_type'))

    def __init__(self, name, type):
        self.name = name
        self.type = type


class ProgrammingLanguage(db.Model):
    __tablename__ = "ProgrammingLanguage"
    __schema__ = schema_name

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    date = db.Column(db.Date)

    dialect_of = db.Column(db.Integer, db.ForeignKey('ProgrammingLanguage.id'))
    has_dialect = db.relationship("ProgrammingLanguage")

    influenced_by = db.relation("ProgrammingLanguage", secondary=Influence,
                                primaryjoin=Influence.c.InfluencedBy == id,
                                secondaryjoin=Influence.c.HasInfluenced == id,
                                backref="has_influenced")

    designers = db.relationship("DesignedByPerson",
                                backref="programming_language")
    institutions = db.relationship("DesignedByInstitution",
                                   backref="programming_language")

    paradigms = db.relationship("Paradigm", secondary=FollowsParadigm)
    disciplines = db.relationship("TypingDiscipline", secondary=HasTypingDiscipline)

    def __init__(self, name, date, dialect_of=None):
        self.name = name
        self.date = date

        if dialect_of:
            self.dialect_of = dialect_of

    def to_dict(self):
        d = dict()
        d['id'] = self.id
        d['name'] = self.name
        d['influences'] = map(lambda pl: pl.id, self.influenced_by)
        d['influenced'] = map(lambda pl: pl.id, self.has_influenced)
        return d


class Person(db.Model):
    __tablename__ = "Person"
    __schema__ = schema_name

    id = db.Column(db.Integer, primary_key=True)
    birthday = db.Column(db.Date)
    firstname = db.Column(db.String(256))
    lastname = db.Column(db.String(256))
    nationality = db.Column(db.String(256))
    deathday = db.Column(db.Date)
    #sex = db.Column(db.Enum('male', 'female', name='sex'))
    sex = db.Column(db.String(6))

    birthplace_id = db.Column(db.Integer, db.ForeignKey('Town.id'))
    birthplace = db.relationship("Town")

    # TODO: constraints op deze relatie
    parents = db.relation("Person", secondary=Ancestor,
                          primaryjoin=Ancestor.c.Child == id,
                          secondaryjoin=Ancestor.c.Parent == id,
                          backref="children")

    graduations = db.relationship("Graduation")

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


class DesignedByPerson(db.Model):
    __tablename__ = 'DesignedByPerson'
    __schema__ = schema_name

    id = db.Column(db.Integer, primary_key=True)
    pl_id = db.Column(
        db.Integer, db.ForeignKey('ProgrammingLanguage.id'))
    person_id = db.Column(
        db.Integer, db.ForeignKey('Person.id'))
    version = db.Column(db.Integer)
    designer = db.relationship("Person", backref="has_designed")


class DesignedByInstitution(db.Model):
    __tablename__ = 'DesignedByInstitution'
    __schema__ = schema_name

    id = db.Column(db.Integer, primary_key=True)
    pl_id = db.Column(
        db.Integer, db.ForeignKey('ProgrammingLanguage.id'))
    institution_id = db.Column(
        db.Integer, db.ForeignKey('Institution.id'))
    version = db.Column(db.Integer)
    designer = db.relationship("Institution", backref="has_designed")


# Merged with TownInStateOfCountry
class Town(db.Model):
    __tablename__ = "Town"
    __schema__ = schema_name

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    postal_code = db.Column(db.String(256))
    country = db.Column(db.String(256))
    state = db.Column(db.String(256))

    def __init__(self, name, state, country):
        self.name = name
        self.state = state
        self.country = country


class Graduation(db.Model):
    __tablename__ = 'Graduation'
    __schema__ = schema_name

    person_id = db.Column(
        db.Integer, db.ForeignKey('Person.id'), primary_key=True)
    institution_id = db.Column(
        db.Integer, db.ForeignKey('Institution.id'), primary_key=True)
    year = db.Column(db.Integer)
    institution = db.relationship("Institution")


# TODO: relationship met Person toevoegen
class Award(db.Model):
    __tablename__ = "Award"
    __schema__ = schema_name

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    person_id = db.Column(db.Integer, db.ForeignKey("Person.id"))
    year = db.Column(db.Integer)

    def __init__(self, name, person, year):
        self.name = name
        self.person_id = person
        self.year = year


class Paradigm(db.Model):
    __tablename__ = "Paradigm"
    __schema__ = schema_name

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))

    def __init__(self, name):
        self.name = name


class TypingDiscipline(db.Model):
    __tablename__ = "TypingDiscipline"
    __schema__ = schema_name

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))

    def __init__(self, name):
        self.name = name


# TODO: relationship met ProgrammingLanguage toevoegen?
class Implementation(db.Model):
    __tablename__ = "Implementation"
    __schema__ = schema_name

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    pl_id = db.Column(db.Integer, db.ForeignKey("ProgrammingLanguage.id"))

    def __init__(self, name, pl_id):
        self.name = name
        self.pl_id = pl_id


# TODO: relationship met Person/Institution toevoegen?
class Employment(db.Model):
    __tablename__ = "Employment"
    __schema__ = schema_name

    id = db.Column(db.Integer, primary_key=True)
    institution_id = db.Column(db.Integer, db.ForeignKey("Institution.id"))
    person_id = db.Column(db.Integer, db.ForeignKey("Person.id"))
    year = db.Column(db.Integer)

    def __init__(self, institution_id, person_id, year):
        self.institution_id = institution_id
        self.person_id = person_id
        self.year = year


# TODO: Relationship met Person toevoegen?
class PhoneNumber(db.Model):
    __tablename__ = "PhoneNumber"
    __schema__ = schema_name

    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey("Person.id"))
    number = db.Column(db.String(256))

    def __init__(self, person_id, number):
        self.person_id = person_id
        self.number = number


# TODO: Relationship met Person toevoegen?
class EmailAddress(db.Model):
    __tablename__ = "EmailAddress"
    __schema__ = schema_name

    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey("Person.id"))
    emailaddress = db.Column(db.String(256))

    def __init__(self, person_id, emailaddress):
        self.person_id = person_id
        self.emailaddress = emailaddress


# TODO: Relationship met Person toevoegen?
class Address(db.Model):
    __tablename__ = "Address"
    __schema__ = schema_name

    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey("Person.id"))
    town_id = db.Column(db.Integer, db.ForeignKey("Town.id"))
    street = db.Column(db.String(256))
    number = db.Column(db.String(256)) # String want PO boxes etc

    def __init__(self, person_id, town_id, street, number):
        self.person_id = person_id
        self.town_id = town_id
        self.street = street
        self.number = number


# TODO: Relationship met Implementation/Person toevoegen?
class ImplementationVersionDesignedBy(db.Model):
    __tablename__ = "ImplementationVersionDesignedBy"
    __schema__ = schema_name

    id = db.Column(db.Integer, primary_key=True)
    implementation_id = db.Column(db.Integer, db.ForeignKey("Implementation.id"))
    person_id = db.Column(db.Integer, db.ForeignKey("Person.id"))
    version = db.Column(db.Integer)


# TODO: Relationship met Implementation/Institution toevoegen?
class ImplementationVersionDesignedByInst(db.Model):
    __tablename__ = "ImplementationVersionDesignedByInst"
    __schema__ = schema_name

    id = db.Column(db.Integer, primary_key=True)
    implementation_id = db.Column(db.Integer, db.ForeignKey("Implementation.id"))
    institution_id = db.Column(db.Integer, db.ForeignKey("Institution.id"))
    version = db.Column(db.Integer)
