
CREATE TABLE ProgrammingLanguage
(
	programmingLanguageId INT AUTO_INCREMENT NOT NULL,
	name VARCHAR(16383) NOT NULL,
	`day` INT,
	dialectOfProgrammingLanguageId INT,
	`month` INT,
	yearNr INT,
	CONSTRAINT ProgrammingLanguage_PK PRIMARY KEY(programmingLanguageId)
);

CREATE TABLE ProgrammingLanguageInfluencedProgrammingLanguage
(
	programmingLanguageId1 INT NOT NULL,
	programmingLanguageId2 INT NOT NULL,
	CONSTRAINT ProgrammingLanguageInfluencedProgrammingLanguage_PK PRIMARY KEY(programmingLanguageId2, programmingLanguageId1)
);

CREATE TABLE Person
(
	personId INT AUTO_INCREMENT NOT NULL,
	bornOnDateDay INT NOT NULL,
	bornOnDateMonth INT NOT NULL,
	bornOnDateYearNr INT NOT NULL,
	firstname VARCHAR(16383) NOT NULL,
	lastname VARCHAR(16383) NOT NULL,
	countryName VARCHAR(16383),
	diedOnDateDay INT,
	diedOnDateMonth INT,
	diedOnDateYearNr INT,
	sexCode CHAR(63),
	townId INT,
	CONSTRAINT Person_PK PRIMARY KEY(personId)
);

CREATE TABLE ProgrammingLanguageHasVersionDesignedByPerson
(
	personId INT NOT NULL,
	programmingLanguageId INT NOT NULL,
	versionNr INT NOT NULL,
	CONSTRAINT ProgrammingLanguageHasVersionDesignedByPerson_PK PRIMARY KEY(programmingLanguageId, versionNr, personId)
);

CREATE TABLE PersonAncestorOfPerson
(
	personId1 INT NOT NULL,
	personId2 INT NOT NULL,
	CONSTRAINT PersonAncestorOfPerson_PK PRIMARY KEY(personId2, personId1)
);

CREATE TABLE Town
(
	townId INT AUTO_INCREMENT NOT NULL,
	name VARCHAR(16383) NOT NULL,
	postalCode CHAR(63),
	CONSTRAINT Town_PK PRIMARY KEY(townId),
	CONSTRAINT Town_UC UNIQUE(postalCode)
);

CREATE TABLE Institution
(
	institutionId INT AUTO_INCREMENT NOT NULL,
	name VARCHAR(16383) NOT NULL,
	typeCode CHAR(63) NOT NULL,
	CONSTRAINT Institution_PK PRIMARY KEY(institutionId)
);

CREATE TABLE PersonGraduatedFromInstitution
(
	institutionId INT NOT NULL,
	personId INT NOT NULL,
	yearNr INT NOT NULL,
	CONSTRAINT PersonGraduatedFromInstitution_PK PRIMARY KEY(personId, institutionId)
);

CREATE TABLE PersonInYearAwardedWithAward
(
	awardName VARCHAR(16383) NOT NULL,
	personId INT NOT NULL,
	yearNr INT NOT NULL,
	CONSTRAINT PersonInYearAwardedWithAward_PK PRIMARY KEY(awardName, yearNr, personId)
);

CREATE TABLE Paradigm
(
	paradigmId INT AUTO_INCREMENT NOT NULL,
	name VARCHAR(16383) NOT NULL,
	CONSTRAINT Paradigm_PK PRIMARY KEY(paradigmId)
);

CREATE TABLE ProgrammingLanguageFollowsParadigm
(
	paradigmId INT NOT NULL,
	programmingLanguageId INT NOT NULL,
	CONSTRAINT ProgrammingLanguageFollowsParadigm_PK PRIMARY KEY(paradigmId, programmingLanguageId)
);

CREATE TABLE TypingDiscipline
(
	typingDisciplineId INT AUTO_INCREMENT NOT NULL,
	name VARCHAR(16383) NOT NULL,
	CONSTRAINT TypingDiscipline_PK PRIMARY KEY(typingDisciplineId)
);

CREATE TABLE ProgrammingLanguageHasTypingDiscipline
(
	programmingLanguageId INT NOT NULL,
	typingDisciplineId INT NOT NULL,
	CONSTRAINT ProgrammingLanguageHasTypingDiscipline_PK PRIMARY KEY(programmingLanguageId, typingDisciplineId)
);

CREATE TABLE Implementation
(
	implementationId INT AUTO_INCREMENT NOT NULL,
	name VARCHAR(16383) NOT NULL,
	programmingLanguageId INT,
	CONSTRAINT Implementation_PK PRIMARY KEY(implementationId)
);

CREATE TABLE ProgrammingLanguageHasVersionDesignedByInstitution
(
	institutionId INT NOT NULL,
	programmingLanguageId INT NOT NULL,
	versionNr INT NOT NULL,
	CONSTRAINT ProgrammingLanguageHasVersionDesignedByInstitution_PK PRIMARY KEY(programmingLanguageId, versionNr, institutionId)
);

CREATE TABLE PersonWorksForInstitutionInYear
(
	institutionId INT NOT NULL,
	personId INT NOT NULL,
	yearNr INT NOT NULL,
	CONSTRAINT PersonWorksForInstitutionInYear_PK PRIMARY KEY(personId, institutionId, yearNr)
);

CREATE TABLE TownInStateOfCountry
(
	countryName VARCHAR(16383) NOT NULL,
	stateName VARCHAR(16383) NOT NULL,
	townId INT NOT NULL,
	CONSTRAINT TownInStateOfCountry_PK PRIMARY KEY(townId, stateName, countryName)
);

CREATE TABLE PhonenrOfPerson
(
	personId INT NOT NULL,
	phonenr VARCHAR(16383) NOT NULL,
	CONSTRAINT PhonenrOfPerson_PK PRIMARY KEY(personId, phonenr)
);

CREATE TABLE EmailaddressOfPerson
(
	emailaddress VARCHAR(16383) NOT NULL,
	personId INT NOT NULL,
	CONSTRAINT EmailaddressOfPerson_PK PRIMARY KEY(personId, emailaddress)
);

CREATE TABLE PersonHasGeographicalAddress
(
	personId INT NOT NULL,
	streetName INT NOT NULL,
	streetnrNr INT NOT NULL,
	townId INT NOT NULL,
	CONSTRAINT PersonHasGeographicalAddress_PK PRIMARY KEY(personId, streetName, streetnrNr, townId)
);

CREATE TABLE VersionOfImplementationDesignedByPerson
(
	implementationId INT NOT NULL,
	personId INT NOT NULL,
	versionNr INT NOT NULL,
	CONSTRAINT VersionOfImplementationDesignedByPerson_PK PRIMARY KEY(versionNr, implementationId, personId)
);

CREATE TABLE VersionOfImplementationDesignedByInstitution
(
	implementationId INT NOT NULL,
	institutionId INT NOT NULL,
	versionNr INT NOT NULL,
	CONSTRAINT VersionOfImplementationDesignedByInstitution_PK PRIMARY KEY(versionNr, implementationId, institutionId)
);

ALTER TABLE ProgrammingLanguage ADD CONSTRAINT ProgrammingLanguage_FK FOREIGN KEY (dialectOfProgrammingLanguageId) REFERENCES ProgrammingLanguage (programmingLanguageId) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE ProgrammingLanguageInfluencedProgrammingLanguage ADD CONSTRAINT ProgrammingLanguageInfluencedProgrammingLanguage_FK1 FOREIGN KEY (programmingLanguageId2) REFERENCES ProgrammingLanguage (programmingLanguageId) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE ProgrammingLanguageInfluencedProgrammingLanguage ADD CONSTRAINT ProgrammingLanguageInfluencedProgrammingLanguage_FK2 FOREIGN KEY (programmingLanguageId1) REFERENCES ProgrammingLanguage (programmingLanguageId) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE Person ADD CONSTRAINT Person_FK FOREIGN KEY (townId) REFERENCES Town (townId) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE ProgrammingLanguageHasVersionDesignedByPerson ADD CONSTRAINT ProgrammingLanguageHasVersionDesignedByPerson_FK1 FOREIGN KEY (programmingLanguageId) REFERENCES ProgrammingLanguage (programmingLanguageId) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE ProgrammingLanguageHasVersionDesignedByPerson ADD CONSTRAINT ProgrammingLanguageHasVersionDesignedByPerson_FK2 FOREIGN KEY (personId) REFERENCES Person (personId) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE PersonAncestorOfPerson ADD CONSTRAINT PersonAncestorOfPerson_FK1 FOREIGN KEY (personId2) REFERENCES Person (personId) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE PersonAncestorOfPerson ADD CONSTRAINT PersonAncestorOfPerson_FK2 FOREIGN KEY (personId1) REFERENCES Person (personId) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE PersonGraduatedFromInstitution ADD CONSTRAINT PersonGraduatedFromInstitution_FK1 FOREIGN KEY (personId) REFERENCES Person (personId) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE PersonGraduatedFromInstitution ADD CONSTRAINT PersonGraduatedFromInstitution_FK2 FOREIGN KEY (institutionId) REFERENCES Institution (institutionId) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE PersonInYearAwardedWithAward ADD CONSTRAINT PersonInYearAwardedWithAward_FK FOREIGN KEY (personId) REFERENCES Person (personId) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE ProgrammingLanguageFollowsParadigm ADD CONSTRAINT ProgrammingLanguageFollowsParadigm_FK1 FOREIGN KEY (paradigmId) REFERENCES Paradigm (paradigmId) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE ProgrammingLanguageFollowsParadigm ADD CONSTRAINT ProgrammingLanguageFollowsParadigm_FK2 FOREIGN KEY (programmingLanguageId) REFERENCES ProgrammingLanguage (programmingLanguageId) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE ProgrammingLanguageHasTypingDiscipline ADD CONSTRAINT ProgrammingLanguageHasTypingDiscipline_FK1 FOREIGN KEY (programmingLanguageId) REFERENCES ProgrammingLanguage (programmingLanguageId) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE ProgrammingLanguageHasTypingDiscipline ADD CONSTRAINT ProgrammingLanguageHasTypingDiscipline_FK2 FOREIGN KEY (typingDisciplineId) REFERENCES TypingDiscipline (typingDisciplineId) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE Implementation ADD CONSTRAINT Implementation_FK FOREIGN KEY (programmingLanguageId) REFERENCES ProgrammingLanguage (programmingLanguageId) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE ProgrammingLanguageHasVersionDesignedByInstitution ADD CONSTRAINT ProgrammingLanguageHasVersionDesignedByInstitution_FK1 FOREIGN KEY (programmingLanguageId) REFERENCES ProgrammingLanguage (programmingLanguageId) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE ProgrammingLanguageHasVersionDesignedByInstitution ADD CONSTRAINT ProgrammingLanguageHasVersionDesignedByInstitution_FK2 FOREIGN KEY (institutionId) REFERENCES Institution (institutionId) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE PersonWorksForInstitutionInYear ADD CONSTRAINT PersonWorksForInstitutionInYear_FK1 FOREIGN KEY (personId) REFERENCES Person (personId) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE PersonWorksForInstitutionInYear ADD CONSTRAINT PersonWorksForInstitutionInYear_FK2 FOREIGN KEY (institutionId) REFERENCES Institution (institutionId) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE TownInStateOfCountry ADD CONSTRAINT TownInStateOfCountry_FK FOREIGN KEY (townId) REFERENCES Town (townId) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE PhonenrOfPerson ADD CONSTRAINT PhonenrOfPerson_FK FOREIGN KEY (personId) REFERENCES Person (personId) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE EmailaddressOfPerson ADD CONSTRAINT EmailaddressOfPerson_FK FOREIGN KEY (personId) REFERENCES Person (personId) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE PersonHasGeographicalAddress ADD CONSTRAINT PersonHasGeographicalAddress_FK1 FOREIGN KEY (personId) REFERENCES Person (personId) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE PersonHasGeographicalAddress ADD CONSTRAINT PersonHasGeographicalAddress_FK2 FOREIGN KEY (townId) REFERENCES Town (townId) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE VersionOfImplementationDesignedByPerson ADD CONSTRAINT VersionOfImplementationDesignedByPerson_FK1 FOREIGN KEY (implementationId) REFERENCES Implementation (implementationId) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE VersionOfImplementationDesignedByPerson ADD CONSTRAINT VersionOfImplementationDesignedByPerson_FK2 FOREIGN KEY (personId) REFERENCES Person (personId) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE VersionOfImplementationDesignedByInstitution ADD CONSTRAINT VersionOfImplementationDesignedByInstitution_FK1 FOREIGN KEY (implementationId) REFERENCES Implementation (implementationId) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE VersionOfImplementationDesignedByInstitution ADD CONSTRAINT VersionOfImplementationDesignedByInstitution_FK2 FOREIGN KEY (institutionId) REFERENCES Institution (institutionId) ON DELETE RESTRICT ON UPDATE RESTRICT;
