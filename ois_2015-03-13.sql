# ************************************************************
# Sequel Pro SQL dump
# Version 4096
#
# http://www.sequelpro.com/
# http://code.google.com/p/sequel-pro/
#
# Host: 127.0.0.1 (MySQL 5.6.16)
# Database: ois
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table Address
# ------------------------------------------------------------

DROP TABLE IF EXISTS `Address`;

CREATE TABLE `Address` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `person_id` int(11) DEFAULT NULL,
  `town_id` int(11) DEFAULT NULL,
  `street` varchar(256) DEFAULT NULL,
  `number` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `person_id` (`person_id`),
  KEY `town_id` (`town_id`),
  CONSTRAINT `address_ibfk_1` FOREIGN KEY (`person_id`) REFERENCES `Person` (`id`),
  CONSTRAINT `address_ibfk_2` FOREIGN KEY (`town_id`) REFERENCES `Town` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table Ancestor
# ------------------------------------------------------------

DROP TABLE IF EXISTS `Ancestor`;

CREATE TABLE `Ancestor` (
  `Parent` int(11) DEFAULT NULL,
  `Child` int(11) DEFAULT NULL,
  KEY `Parent` (`Parent`),
  KEY `Child` (`Child`),
  CONSTRAINT `ancestor_ibfk_1` FOREIGN KEY (`Parent`) REFERENCES `Person` (`id`),
  CONSTRAINT `ancestor_ibfk_2` FOREIGN KEY (`Child`) REFERENCES `Person` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `Ancestor` WRITE;
/*!40000 ALTER TABLE `Ancestor` DISABLE KEYS */;

INSERT INTO `Ancestor` (`Parent`, `Child`)
VALUES
	(13,12),
	(14,12),
	(18,17),
	(19,18),
	(20,19),
	(24,23),
	(25,23),
	(24,26),
	(25,26);

/*!40000 ALTER TABLE `Ancestor` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table Award
# ------------------------------------------------------------

DROP TABLE IF EXISTS `Award`;

CREATE TABLE `Award` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(256) DEFAULT NULL,
  `person_id` int(11) DEFAULT NULL,
  `year` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `person_id` (`person_id`),
  CONSTRAINT `award_ibfk_1` FOREIGN KEY (`person_id`) REFERENCES `Person` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `Award` WRITE;
/*!40000 ALTER TABLE `Award` DISABLE KEYS */;

INSERT INTO `Award` (`id`, `name`, `person_id`, `year`)
VALUES
	(1,'Iron Cross 2nd Class',3,1944),
	(2,'Bundesverdienstkreuz 1st Class',3,1982),
	(3,'IEEE Computer Pioneer Award',3,1988),
	(4,'National Medal of Science',7,1975),
	(5,'ACM Turing Award',7,1977),
	(6,'ACM Turing Award',9,1966),
	(7,'Computer Pioneer Award',9,1985),
	(8,'ACM Turing Award',10,2005),
	(9,'IEEE Computer Pioneer Award',11,1986),
	(10,'ACM Turing Award',12,1971),
	(11,'IEEE Computer Pioneer Award',12,1985),
	(12,'ACM Turing Award',15,1984);

/*!40000 ALTER TABLE `Award` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table DesignedByInstitution
# ------------------------------------------------------------

DROP TABLE IF EXISTS `DesignedByInstitution`;

CREATE TABLE `DesignedByInstitution` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pl_id` int(11) DEFAULT NULL,
  `institution_id` int(11) DEFAULT NULL,
  `version` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `pl_id` (`pl_id`),
  KEY `institution_id` (`institution_id`),
  CONSTRAINT `designedbyinstitution_ibfk_1` FOREIGN KEY (`pl_id`) REFERENCES `ProgrammingLanguage` (`id`),
  CONSTRAINT `designedbyinstitution_ibfk_2` FOREIGN KEY (`institution_id`) REFERENCES `Institution` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `DesignedByInstitution` WRITE;
/*!40000 ALTER TABLE `DesignedByInstitution` DISABLE KEYS */;

INSERT INTO `DesignedByInstitution` (`id`, `pl_id`, `institution_id`, `version`)
VALUES
	(1,6,26,2),
	(2,7,19,1),
	(3,7,19,2),
	(4,7,25,2),
	(5,7,19,4),
	(6,7,25,4),
	(7,11,28,1),
	(8,11,29,1),
	(9,12,28,1),
	(10,12,30,1),
	(11,13,31,10),
	(12,13,31,11),
	(13,13,31,12),
	(14,13,31,13),
	(15,13,31,14),
	(16,13,31,50),
	(17,13,31,60),
	(18,13,31,70),
	(19,13,32,80),
	(20,13,32,90),
	(21,13,32,100),
	(22,14,34,2),
	(23,14,34,3),
	(24,15,35,1);

/*!40000 ALTER TABLE `DesignedByInstitution` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table DesignedByPerson
# ------------------------------------------------------------

DROP TABLE IF EXISTS `DesignedByPerson`;

CREATE TABLE `DesignedByPerson` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pl_id` int(11) DEFAULT NULL,
  `person_id` int(11) DEFAULT NULL,
  `version` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `pl_id` (`pl_id`),
  KEY `person_id` (`person_id`),
  CONSTRAINT `designedbyperson_ibfk_1` FOREIGN KEY (`pl_id`) REFERENCES `ProgrammingLanguage` (`id`),
  CONSTRAINT `designedbyperson_ibfk_2` FOREIGN KEY (`person_id`) REFERENCES `Person` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `DesignedByPerson` WRITE;
/*!40000 ALTER TABLE `DesignedByPerson` DISABLE KEYS */;

INSERT INTO `DesignedByPerson` (`id`, `pl_id`, `person_id`, `version`)
VALUES
	(1,1,3,60),
	(2,1,4,60),
	(3,1,5,60),
	(4,1,6,60),
	(5,1,7,60),
	(6,1,8,60),
	(7,1,9,60),
	(8,1,10,60),
	(9,1,11,60),
	(10,1,12,60),
	(11,2,1,1),
	(12,3,2,1),
	(13,4,23,1),
	(14,5,15,1),
	(15,6,16,1),
	(16,6,16,2),
	(17,8,17,1),
	(18,9,15,1),
	(19,10,15,1),
	(20,13,21,10),
	(21,13,21,11),
	(22,13,21,12),
	(23,13,21,13),
	(24,13,21,14),
	(25,13,21,50),
	(26,13,21,60),
	(27,13,21,70),
	(28,14,22,2),
	(29,14,22,3);

/*!40000 ALTER TABLE `DesignedByPerson` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table EmailAddress
# ------------------------------------------------------------

DROP TABLE IF EXISTS `EmailAddress`;

CREATE TABLE `EmailAddress` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `person_id` int(11) DEFAULT NULL,
  `emailaddress` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `person_id` (`person_id`),
  CONSTRAINT `emailaddress_ibfk_1` FOREIGN KEY (`person_id`) REFERENCES `Person` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table Employment
# ------------------------------------------------------------

DROP TABLE IF EXISTS `Employment`;

CREATE TABLE `Employment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `institution_id` int(11) DEFAULT NULL,
  `person_id` int(11) DEFAULT NULL,
  `year` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `institution_id` (`institution_id`),
  KEY `person_id` (`person_id`),
  CONSTRAINT `employment_ibfk_1` FOREIGN KEY (`institution_id`) REFERENCES `Institution` (`id`),
  CONSTRAINT `employment_ibfk_2` FOREIGN KEY (`person_id`) REFERENCES `Person` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `Employment` WRITE;
/*!40000 ALTER TABLE `Employment` DISABLE KEYS */;

INSERT INTO `Employment` (`id`, `institution_id`, `person_id`, `year`)
VALUES
	(1,2,3,1963),
	(2,2,3,1972),
	(3,23,7,1950),
	(4,9,9,1956),
	(5,10,9,1971),
	(6,36,10,1959),
	(7,12,11,1947),
	(8,15,12,1962),
	(9,15,15,1963),
	(10,16,15,1968),
	(11,24,15,1976),
	(12,26,16,1989),
	(13,27,16,1996),
	(14,20,17,1962),
	(15,21,17,1965),
	(16,31,21,1984),
	(17,33,21,2011);

/*!40000 ALTER TABLE `Employment` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table FollowsParadigm
# ------------------------------------------------------------

DROP TABLE IF EXISTS `FollowsParadigm`;

CREATE TABLE `FollowsParadigm` (
  `pl_id` int(11) DEFAULT NULL,
  `pa_id` int(11) DEFAULT NULL,
  KEY `pl_id` (`pl_id`),
  KEY `pa_id` (`pa_id`),
  CONSTRAINT `followsparadigm_ibfk_1` FOREIGN KEY (`pl_id`) REFERENCES `ProgrammingLanguage` (`id`),
  CONSTRAINT `followsparadigm_ibfk_2` FOREIGN KEY (`pa_id`) REFERENCES `Paradigm` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `FollowsParadigm` WRITE;
/*!40000 ALTER TABLE `FollowsParadigm` DISABLE KEYS */;

INSERT INTO `FollowsParadigm` (`pl_id`, `pa_id`)
VALUES
	(1,3),
	(1,4),
	(1,5),
	(2,4),
	(3,4),
	(3,1),
	(4,3),
	(4,4),
	(4,1),
	(5,4),
	(5,5),
	(8,4),
	(8,5),
	(8,3),
	(8,2),
	(10,4),
	(10,5),
	(10,6),
	(11,4),
	(11,5),
	(11,6),
	(12,4),
	(12,5),
	(12,6),
	(12,3),
	(14,1),
	(14,4),
	(14,2),
	(14,7),
	(15,1),
	(15,2),
	(15,8);

/*!40000 ALTER TABLE `FollowsParadigm` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table Graduation
# ------------------------------------------------------------

DROP TABLE IF EXISTS `Graduation`;

CREATE TABLE `Graduation` (
  `person_id` int(11) NOT NULL,
  `institution_id` int(11) NOT NULL,
  `year` int(11) DEFAULT NULL,
  PRIMARY KEY (`person_id`,`institution_id`),
  KEY `institution_id` (`institution_id`),
  CONSTRAINT `graduation_ibfk_1` FOREIGN KEY (`person_id`) REFERENCES `Person` (`id`),
  CONSTRAINT `graduation_ibfk_2` FOREIGN KEY (`institution_id`) REFERENCES `Institution` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `Graduation` WRITE;
/*!40000 ALTER TABLE `Graduation` DISABLE KEYS */;

INSERT INTO `Graduation` (`person_id`, `institution_id`, `year`)
VALUES
	(3,3,1950),
	(4,1,1957),
	(6,3,1950),
	(7,4,1949),
	(8,5,1950),
	(8,6,1953),
	(9,7,1943),
	(9,8,1949),
	(11,11,1939),
	(12,13,1948),
	(12,14,1951),
	(15,16,1959),
	(15,17,1959),
	(15,18,1963),
	(17,20,1935),
	(21,7,1983),
	(21,22,1977);

/*!40000 ALTER TABLE `Graduation` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table HasTypingDiscipline
# ------------------------------------------------------------

DROP TABLE IF EXISTS `HasTypingDiscipline`;

CREATE TABLE `HasTypingDiscipline` (
  `pl_id` int(11) DEFAULT NULL,
  `td_id` int(11) DEFAULT NULL,
  KEY `pl_id` (`pl_id`),
  KEY `td_id` (`td_id`),
  CONSTRAINT `hastypingdiscipline_ibfk_1` FOREIGN KEY (`pl_id`) REFERENCES `ProgrammingLanguage` (`id`),
  CONSTRAINT `hastypingdiscipline_ibfk_2` FOREIGN KEY (`td_id`) REFERENCES `TypingDiscipline` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `HasTypingDiscipline` WRITE;
/*!40000 ALTER TABLE `HasTypingDiscipline` DISABLE KEYS */;

INSERT INTO `HasTypingDiscipline` (`pl_id`, `td_id`)
VALUES
	(2,4),
	(2,2),
	(3,4),
	(3,2),
	(4,3),
	(4,4),
	(5,4),
	(5,2),
	(5,6),
	(9,2),
	(9,4),
	(11,2),
	(11,4),
	(12,2),
	(12,4),
	(12,6),
	(13,4),
	(13,2),
	(13,6),
	(13,7),
	(13,8),
	(14,1),
	(14,5),
	(14,2),
	(15,4),
	(15,2),
	(15,9);

/*!40000 ALTER TABLE `HasTypingDiscipline` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table Implementation
# ------------------------------------------------------------

DROP TABLE IF EXISTS `Implementation`;

CREATE TABLE `Implementation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(256) DEFAULT NULL,
  `pl_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `pl_id` (`pl_id`),
  CONSTRAINT `implementation_ibfk_1` FOREIGN KEY (`pl_id`) REFERENCES `ProgrammingLanguage` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `Implementation` WRITE;
/*!40000 ALTER TABLE `Implementation` DISABLE KEYS */;

INSERT INTO `Implementation` (`id`, `name`, `pl_id`)
VALUES
	(1,'HPPascal',5),
	(2,'FreePascal',5),
	(3,'IBMSystem370',5),
	(4,'Pascal-P',7),
	(5,'OpenJDK',13);

/*!40000 ALTER TABLE `Implementation` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table ImplementationVersionDesignedBy
# ------------------------------------------------------------

DROP TABLE IF EXISTS `ImplementationVersionDesignedBy`;

CREATE TABLE `ImplementationVersionDesignedBy` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `implementation_id` int(11) DEFAULT NULL,
  `person_id` int(11) DEFAULT NULL,
  `version` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `implementation_id` (`implementation_id`),
  KEY `person_id` (`person_id`),
  CONSTRAINT `implementationversiondesignedby_ibfk_1` FOREIGN KEY (`implementation_id`) REFERENCES `Implementation` (`id`),
  CONSTRAINT `implementationversiondesignedby_ibfk_2` FOREIGN KEY (`person_id`) REFERENCES `Person` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table ImplementationVersionDesignedByInst
# ------------------------------------------------------------

DROP TABLE IF EXISTS `ImplementationVersionDesignedByInst`;

CREATE TABLE `ImplementationVersionDesignedByInst` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `implementation_id` int(11) DEFAULT NULL,
  `institution_id` int(11) DEFAULT NULL,
  `version` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `implementation_id` (`implementation_id`),
  KEY `institution_id` (`institution_id`),
  CONSTRAINT `implementationversiondesignedbyinst_ibfk_1` FOREIGN KEY (`implementation_id`) REFERENCES `Implementation` (`id`),
  CONSTRAINT `implementationversiondesignedbyinst_ibfk_2` FOREIGN KEY (`institution_id`) REFERENCES `Institution` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `ImplementationVersionDesignedByInst` WRITE;
/*!40000 ALTER TABLE `ImplementationVersionDesignedByInst` DISABLE KEYS */;

INSERT INTO `ImplementationVersionDesignedByInst` (`id`, `implementation_id`, `institution_id`, `version`)
VALUES
	(1,3,23,1),
	(2,4,19,1),
	(3,4,19,2),
	(4,4,25,2),
	(5,4,19,4),
	(6,4,25,4),
	(7,5,31,60),
	(8,5,31,70),
	(9,5,32,80);

/*!40000 ALTER TABLE `ImplementationVersionDesignedByInst` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table Influence
# ------------------------------------------------------------

DROP TABLE IF EXISTS `Influence`;

CREATE TABLE `Influence` (
  `HasInfluenced` int(11) DEFAULT NULL,
  `InfluencedBy` int(11) DEFAULT NULL,
  KEY `HasInfluenced` (`HasInfluenced`),
  KEY `InfluencedBy` (`InfluencedBy`),
  CONSTRAINT `influence_ibfk_1` FOREIGN KEY (`HasInfluenced`) REFERENCES `ProgrammingLanguage` (`id`),
  CONSTRAINT `influence_ibfk_2` FOREIGN KEY (`InfluencedBy`) REFERENCES `ProgrammingLanguage` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `Influence` WRITE;
/*!40000 ALTER TABLE `Influence` DISABLE KEYS */;

INSERT INTO `Influence` (`HasInfluenced`, `InfluencedBy`)
VALUES
	(1,2),
	(2,3),
	(3,4),
	(1,5),
	(1,8),
	(5,9),
	(1,10),
	(5,10),
	(9,10),
	(1,11),
	(5,11),
	(10,11),
	(1,12),
	(5,12),
	(10,12),
	(11,12),
	(12,13),
	(3,13),
	(7,13),
	(1,14),
	(3,14),
	(13,14),
	(12,14),
	(2,14),
	(14,15);

/*!40000 ALTER TABLE `Influence` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table Institution
# ------------------------------------------------------------

DROP TABLE IF EXISTS `Institution`;

CREATE TABLE `Institution` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(256) DEFAULT NULL,
  `type` enum('academic','commercial','public') DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `Institution` WRITE;
/*!40000 ALTER TABLE `Institution` DISABLE KEYS */;

INSERT INTO `Institution` (`id`, `name`, `type`)
VALUES
	(1,'Technische Hochschule Darmstadt','academic'),
	(2,'Technische Universitat Munchen','academic'),
	(3,'Ludwig-Maximilians-Universitat','academic'),
	(4,'Columbia University','academic'),
	(5,'Temple University Philadelphia','academic'),
	(6,'University of Pennsylvania','academic'),
	(7,'Carnegie Mellon University Pennsylvania','academic'),
	(8,'MIT','academic'),
	(9,'Carnegie Institute of Technology','academic'),
	(10,'Yale University','academic'),
	(11,'Delft University of Technology','academic'),
	(12,'University of Amsterdam','academic'),
	(13,'California Institute of Technology','academic'),
	(14,'Princeton University New Jersey','academic'),
	(15,'Stanford University','academic'),
	(16,'ETH Zurich','academic'),
	(17,'Universite Laval Canada','academic'),
	(18,'University of California Berkeley','academic'),
	(19,'University of California San Diego','academic'),
	(20,'University of Cambridge','academic'),
	(21,'University of Oxford','academic'),
	(22,'Calgary University','academic'),
	(23,'IBM','commercial'),
	(24,'Xerox Palo Alto Research Center','commercial'),
	(25,'SofTech Inc','commercial'),
	(26,'Borland Software Company','commercial'),
	(27,'Microsoft','commercial'),
	(28,'DEC Systems Research Center SRC','commercial'),
	(29,'Acorn Research Center','commercial'),
	(30,'Olivetti','commercial'),
	(31,'Sun Microsystems','commercial'),
	(32,'Oracle Corporation','commercial'),
	(33,'Google','commercial'),
	(34,'Python Software Foundation','commercial'),
	(35,'Apple Inc.','commercial'),
	(36,'Regnecentralen Denmark','public');

/*!40000 ALTER TABLE `Institution` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table Paradigm
# ------------------------------------------------------------

DROP TABLE IF EXISTS `Paradigm`;

CREATE TABLE `Paradigm` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `Paradigm` WRITE;
/*!40000 ALTER TABLE `Paradigm` DISABLE KEYS */;

INSERT INTO `Paradigm` (`id`, `name`)
VALUES
	(1,'object-oriented'),
	(2,'functional'),
	(3,'procedural'),
	(4,'imperative'),
	(5,'structured'),
	(6,'modular'),
	(7,'reflective'),
	(8,'block structured');

/*!40000 ALTER TABLE `Paradigm` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table Person
# ------------------------------------------------------------

DROP TABLE IF EXISTS `Person`;

CREATE TABLE `Person` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `birthday` date DEFAULT NULL,
  `firstname` varchar(256) DEFAULT NULL,
  `lastname` varchar(256) DEFAULT NULL,
  `nationality` varchar(256) DEFAULT NULL,
  `deathday` date DEFAULT NULL,
  `sex` enum('male','female') DEFAULT NULL,
  `birthplace_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `birthplace_id` (`birthplace_id`),
  CONSTRAINT `person_ibfk_1` FOREIGN KEY (`birthplace_id`) REFERENCES `Town` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `Person` WRITE;
/*!40000 ALTER TABLE `Person` DISABLE KEYS */;

INSERT INTO `Person` (`id`, `birthday`, `firstname`, `lastname`, `nationality`, `deathday`, `sex`, `birthplace_id`)
VALUES
	(1,NULL,'Dennis','Ritchie','American',NULL,'male',NULL),
	(2,NULL,'Bjarne','Stroustrup','American or Swedish',NULL,'male',NULL),
	(3,'1924-06-10','Friedrich L.','Bauer','German',NULL,'male',1),
	(4,'1928-09-14','Herman','Bottenbruch','German',NULL,'male',NULL),
	(5,'1918-01-09','Heinz','Rutishauser','Swiss','1970-11-10','male',2),
	(6,'1918-12-21','Klaus','Samelson','German','1980-05-25','male',3),
	(7,'1924-12-03','John','Backus','American','2007-03-17','male',4),
	(8,'1927-01-01','Charles','Katz','American',NULL,'male',4),
	(9,'1922-04-01','Alan','Perlis','American','1990-02-07','male',5),
	(10,'1928-10-25','Peter','Naur','Danish',NULL,'male',6),
	(11,'1916-11-02','Adriaan','Van Wijngaarden','Dutch','1987-02-07','male',7),
	(12,'1927-09-04','John','McCarthy','American','2011-10-24','male',8),
	(13,NULL,'John','Patrick',NULL,NULL,'male',NULL),
	(14,NULL,'Ida G.','McCarthy',NULL,NULL,'female',NULL),
	(15,'1934-02-15','Niklaus','Wirth','Swiss',NULL,'male',9),
	(16,'1960-12-01','Anders','Hejlsberg','Danish',NULL,'male',10),
	(17,'1916-11-16','Christopher S.','Strachey','British','1975-05-18','male',11),
	(18,'1817-07-24','Richard','Strachey','British',NULL,'male',NULL),
	(19,NULL,'Edward','Strachey','British',NULL,'male',NULL),
	(20,'1737-05-23','Sir Henry','Strachey 1st Baronet','British','1810-01-03','male',NULL),
	(21,'1955-05-19','James','Gosling','Canadian',NULL,'male',NULL),
	(22,'1956-01-31','Guido','van Rossum','Dutch',NULL,'male',13),
	(23,'1928-03-23','Jean E.','Sammet','American',NULL,'female',14),
	(24,NULL,'Harry','Sammet','American',NULL,'male',NULL),
	(25,NULL,'Ruth','Sammet','American',NULL,'female',NULL),
	(26,NULL,'Helen','Sammet','American',NULL,'female',NULL);

/*!40000 ALTER TABLE `Person` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table PhoneNumber
# ------------------------------------------------------------

DROP TABLE IF EXISTS `PhoneNumber`;

CREATE TABLE `PhoneNumber` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `person_id` int(11) DEFAULT NULL,
  `number` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `person_id` (`person_id`),
  CONSTRAINT `phonenumber_ibfk_1` FOREIGN KEY (`person_id`) REFERENCES `Person` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table ProgrammingLanguage
# ------------------------------------------------------------

DROP TABLE IF EXISTS `ProgrammingLanguage`;

CREATE TABLE `ProgrammingLanguage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(256) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `dialect_of` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `dialect_of` (`dialect_of`),
  CONSTRAINT `programminglanguage_ibfk_1` FOREIGN KEY (`dialect_of`) REFERENCES `ProgrammingLanguage` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `ProgrammingLanguage` WRITE;
/*!40000 ALTER TABLE `ProgrammingLanguage` DISABLE KEYS */;

INSERT INTO `ProgrammingLanguage` (`id`, `name`, `date`, `dialect_of`)
VALUES
	(1,'ALGOL','1958-01-01',NULL),
	(2,'C','1970-01-01',NULL),
	(3,'C++','1979-01-01',NULL),
	(4,'Cobol','1959-01-01',NULL),
	(5,'Pascal','1970-01-01',NULL),
	(6,'Turbo Pascal','1983-01-01',5),
	(7,'UCSD Pascal','1978-01-01',5),
	(8,'CPL','1963-01-01',NULL),
	(9,'Modula','1975-01-01',NULL),
	(10,'Modula-2','1978-01-01',NULL),
	(11,'Modula-2+','1980-01-01',NULL),
	(12,'Modula-3','1980-01-01',NULL),
	(13,'Java','1995-01-01',NULL),
	(14,'Python','1991-01-01',NULL),
	(15,'Swift','2014-09-09',NULL);

/*!40000 ALTER TABLE `ProgrammingLanguage` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table Town
# ------------------------------------------------------------

DROP TABLE IF EXISTS `Town`;

CREATE TABLE `Town` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(256) DEFAULT NULL,
  `postal_code` varchar(256) DEFAULT NULL,
  `country` varchar(256) DEFAULT NULL,
  `state` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `Town` WRITE;
/*!40000 ALTER TABLE `Town` DISABLE KEYS */;

INSERT INTO `Town` (`id`, `name`, `postal_code`, `country`, `state`)
VALUES
	(1,'Regensburg','93001','Germany','Bayern'),
	(2,'Weinfelden','8570','Switzerland','Thurgau'),
	(3,'Strasbourg','67482','France','Alsace-Lorraine'),
	(4,'Philadelphia','19100','USA','Pennsylvania'),
	(5,'Pittsburgh','15100','USA','Pennsylvania'),
	(6,'Frederiksberg','0','Denmark','Seeland'),
	(7,'Rotterdam','3000','Netherlands','Zuid-Holland'),
	(8,'Boston','128','USA','Massachusetts'),
	(9,'Winterthur','8400','Switzerland','Zurich'),
	(10,'Kobenhavn','1000','Denmark','Hovedstaden'),
	(11,'Hampstead','16','UK','London'),
	(12,'Calgary','T1Y','Canada','Alberta'),
	(13,'Haarlem','2000','The Netherlands','Noord-Holland'),
	(14,'New York City','10000','USA','New York');

/*!40000 ALTER TABLE `Town` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table TypingDiscipline
# ------------------------------------------------------------

DROP TABLE IF EXISTS `TypingDiscipline`;

CREATE TABLE `TypingDiscipline` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `TypingDiscipline` WRITE;
/*!40000 ALTER TABLE `TypingDiscipline` DISABLE KEYS */;

INSERT INTO `TypingDiscipline` (`id`, `name`)
VALUES
	(1,'duck'),
	(2,'strong'),
	(3,'weak'),
	(4,'static'),
	(5,'dynamic'),
	(6,'safe'),
	(7,'nominative'),
	(8,'manifest'),
	(9,'inferred');

/*!40000 ALTER TABLE `TypingDiscipline` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
