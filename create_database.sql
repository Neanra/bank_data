CREATE DATABASE `bank` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
CREATE TABLE `currency_rates` (
  `short_name` varchar(3) NOT NULL,
  `name` varchar(45) NOT NULL,
  `rate` decimal(20,8) unsigned NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`short_name`),
  UNIQUE KEY `short_name_UNIQUE` (`short_name`),
  UNIQUE KEY `name_UNIQUE` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
