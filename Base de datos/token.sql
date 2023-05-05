-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.6.7-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para token
CREATE DATABASE IF NOT EXISTS `token` /*!40100 DEFAULT CHARACTER SET utf8mb3 */;
USE `token`;

-- Volcando estructura para tabla token.token
CREATE TABLE IF NOT EXISTS `token` (
  `Valor` varchar(50) NOT NULL DEFAULT 'hola',
  `Fecha` int(11) DEFAULT NULL,
  `Cola` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Valor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla token.token: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `token` DISABLE KEYS */;
INSERT INTO `token` (`Valor`, `Fecha`, `Cola`) VALUES
	('vs7ikthet8rjmpx2b3jm6k', 1683244335, 'weeknd');
/*!40000 ALTER TABLE `token` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
