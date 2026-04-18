/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19-11.8.6-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: myWebAppDB
-- ------------------------------------------------------
-- Server version	11.8.6-MariaDB-5 from Debian

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*M!100616 SET @OLD_NOTE_VERBOSITY=@@NOTE_VERBOSITY, NOTE_VERBOSITY=0 */;

--
-- Table structure for table `progress`
--

DROP TABLE IF EXISTS `progress`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `progress` (
  `progressID` int(11) NOT NULL AUTO_INCREMENT,
  `userID` int(11) NOT NULL,
  `taskID` varchar(45) NOT NULL,
  PRIMARY KEY (`progressID`),
  KEY `userID` (`userID`),
  CONSTRAINT `progress_ibfk_1` FOREIGN KEY (`userID`) REFERENCES `users` (`userID`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `progress`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `progress` WRITE;
/*!40000 ALTER TABLE `progress` DISABLE KEYS */;
INSERT INTO `progress` VALUES
(1,2,'B1'),
(2,4,'B1'),
(3,2,'I1'),
(4,3,'B1'),
(5,2,'A1'),
(6,2,'B2'),
(7,2,'I2'),
(8,2,'A2'),
(9,2,'B3'),
(10,2,'I3'),
(11,2,'A3'),
(12,2,'B4'),
(13,2,'I4'),
(14,2,'A4'),
(15,2,'B5'),
(16,2,'I5'),
(17,2,'A5');
/*!40000 ALTER TABLE `progress` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `scores`
--

DROP TABLE IF EXISTS `scores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `scores` (
  `scoreID` int(11) NOT NULL AUTO_INCREMENT,
  `userID` int(11) NOT NULL,
  `score` int(11) DEFAULT 0,
  PRIMARY KEY (`scoreID`),
  KEY `userID` (`userID`),
  CONSTRAINT `scores_ibfk_1` FOREIGN KEY (`userID`) REFERENCES `users` (`userID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scores`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `scores` WRITE;
/*!40000 ALTER TABLE `scores` DISABLE KEYS */;
INSERT INTO `scores` VALUES
(1,1,0),
(2,2,1500),
(3,3,100),
(4,4,100);
/*!40000 ALTER TABLE `scores` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `userID` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(15) NOT NULL,
  `email` varchar(80) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`userID`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES
(1,'Tester1','tester1@test.com','scrypt:32768:8:1$sez7vQYmlfwRvErt$d64345f8d8be9e76bb661a3edafcad2cdade823d07d5b7aeae16c0f2e1ac2eeb58a60436e86505b0fff1d8c05b49f66e26683ed64663188b2f138e289ef7e96b'),
(2,'Tester2','tester2@test.com','scrypt:32768:8:1$yMc2TFCUI3W3PEid$2d743901ebc49cc49ed6de170b15f7cc154acfa35a312cbbfbd800f9b956e008634088d6e38af46ae1677cba07fb39d5e79a8d4edcf18842dd50688b63d4f05e'),
(3,'Tester3','tester3@test.com','scrypt:32768:8:1$N0aegvvplYtnft5t$6ad7f0961c1779c79587c784a5388646993ce97e637eb2cdf9b7b03bae0f963ad268fbfc7e7dd7058c6cf8dcdccde6e2ad93f951ff13ca683113e1cd423abd0b'),
(4,'Tester4','tester4@test.com','scrypt:32768:8:1$7JNN96AU9o7Rsf1i$d2dda55dd994319e6d525feb3462f855c85c256279dce881c0d1221b173118f82e0c677ded0ab2a7ac64b8d4848d8464117a3464a99d0846d75af65eae0dd18f');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `usersB3`
--

DROP TABLE IF EXISTS `usersB3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `usersB3` (
  `userID` int(11) NOT NULL DEFAULT 0,
  `email` varchar(80) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` varchar(80) NOT NULL,
  `book` varchar(80) DEFAULT NULL,
  `flag` varchar(27) DEFAULT NULL,
  `roleID` varchar(8) DEFAULT 'noadmin'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usersB3`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `usersB3` WRITE;
/*!40000 ALTER TABLE `usersB3` DISABLE KEYS */;
INSERT INTO `usersB3` VALUES
(1,'lilynorm@mymail.com','bunnies2006','customer','Warrior Cats',NULL,'noadmin'),
(2,'reynarivers@mymail.com','ilovebooks','customer',NULL,NULL,'noadmin'),
(3,'jillbloom@mymail.com','ratatouille','customer',NULL,NULL,'noadmin'),
(4,'timmarsh@booknook.com','13061986','Sales Executive','The Hobbit',NULL,'admin'),
(5,'amybrookes@booknook.com','cookies1234','HR Director','To Kill a Mockingbird','injection_sq67l','admin'),
(6,'peterheel@booknook.com','f3984hfwer39','CEO','The Very Hungry Caterpillar',NULL,'admin');
/*!40000 ALTER TABLE `usersB3` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `usersI1`
--

DROP TABLE IF EXISTS `usersI1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `usersI1` (
  `userID` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(80) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` varchar(80) NOT NULL,
  `book` varchar(80) DEFAULT NULL,
  `flag` varchar(27) DEFAULT NULL,
  `roleID` varchar(8) DEFAULT 'noadmin',
  PRIMARY KEY (`userID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usersI1`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `usersI1` WRITE;
/*!40000 ALTER TABLE `usersI1` DISABLE KEYS */;
INSERT INTO `usersI1` VALUES
(1,'lilynorm@mymail.com','bunnies2006','customer','Warrior Cats',NULL,'noadmin'),
(2,'reynarivers@mymail.com','ilovebooks','customer',NULL,NULL,'noadmin'),
(3,'jillbloom@mymail.com','ratatouille','customer',NULL,NULL,'noadmin'),
(4,'timmarsh@booknook.com','13061986','Sales Executive','The Hobbit',NULL,'admin'),
(5,'amybrookes@booknook.com','cookies1234','HR Director','To Kill a Mockingbird','broken_access_control_8af38','admin'),
(6,'peterheel@booknook.com','f3984hfwer39','CEO','The Very Hungry Caterpillar',NULL,'admin');
/*!40000 ALTER TABLE `usersI1` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `usersI4`
--

DROP TABLE IF EXISTS `usersI4`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `usersI4` (
  `userID` int(11) NOT NULL DEFAULT 0,
  `email` varchar(80) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` varchar(80) NOT NULL,
  `book` varchar(80) DEFAULT NULL,
  `flag` varchar(27) DEFAULT NULL,
  `roleID` varchar(8) DEFAULT 'noadmin'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usersI4`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `usersI4` WRITE;
/*!40000 ALTER TABLE `usersI4` DISABLE KEYS */;
INSERT INTO `usersI4` VALUES
(1,'lilynorm@mymail.com','bunnies2006','customer','Warrior Cats',NULL,'noadmin'),
(2,'reynarivers@mymail.com','ilovebooks','customer',NULL,NULL,'noadmin'),
(3,'jillbloom@mymail.com','ratatouille','customer',NULL,NULL,'noadmin'),
(4,'timmarsh@booknook.com','13061986','Sales Executive','The Hobbit',NULL,'admin'),
(5,'amybrookes@booknook.com','cookies1234','HR Director','To Kill a Mockingbird',NULL,'admin'),
(6,'peterheel@booknook.com','f3984hfwer39','CEO','The Very Hungry Caterpillar',NULL,'admin'),
(0,'peterrabbit@mymail.com','bumblebee','customer',NULL,'insecure_design_d30nw','noadmin');
/*!40000 ALTER TABLE `usersI4` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*M!100616 SET NOTE_VERBOSITY=@OLD_NOTE_VERBOSITY */;

-- Dump completed on 2026-04-18 14:10:46
