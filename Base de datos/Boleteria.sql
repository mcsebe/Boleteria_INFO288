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


-- Volcando estructura de base de datos para boleteria
CREATE DATABASE IF NOT EXISTS `boleteria` /*!40100 DEFAULT CHARACTER SET utf8mb3 */;
USE `boleteria`;

-- Volcando estructura para tabla boleteria.concierto
CREATE TABLE IF NOT EXISTS `concierto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) NOT NULL,
  `Precio` int(11) NOT NULL,
  `Fecha` datetime NOT NULL,
  `id_locacion` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_locacion` (`id_locacion`),
  CONSTRAINT `FK_concierto_locacion` FOREIGN KEY (`id_locacion`) REFERENCES `locacion` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla boleteria.concierto: ~1 rows (aproximadamente)
/*!40000 ALTER TABLE `concierto` DISABLE KEYS */;
INSERT INTO `concierto` (`id`, `Nombre`, `Precio`, `Fecha`, `id_locacion`) VALUES
	(1, 'adsdas', 1111, '2023-04-28 17:11:52', 1);
/*!40000 ALTER TABLE `concierto` ENABLE KEYS */;

-- Volcando estructura para tabla boleteria.locacion
CREATE TABLE IF NOT EXISTS `locacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) NOT NULL DEFAULT '0',
  `Ciudad` varchar(50) NOT NULL DEFAULT '0',
  `Region` varchar(50) NOT NULL DEFAULT '0',
  `Capacidad` int(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla boleteria.locacion: ~1 rows (aproximadamente)
/*!40000 ALTER TABLE `locacion` DISABLE KEYS */;
INSERT INTO `locacion` (`id`, `Nombre`, `Ciudad`, `Region`, `Capacidad`) VALUES
	(1, 'werwer', 'weew', 'werrwe', 100);
/*!40000 ALTER TABLE `locacion` ENABLE KEYS */;

-- Volcando estructura para tabla boleteria.reserva
CREATE TABLE IF NOT EXISTS `reserva` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Asiento` int(11) NOT NULL,
  `Nombre` varchar(50) NOT NULL DEFAULT '',
  `Rut` varchar(50) NOT NULL DEFAULT '',
  `Edad` int(11) NOT NULL,
  `Correo` varchar(50) NOT NULL DEFAULT '',
  `id_concierto` int(11) NOT NULL DEFAULT 0,
  `Finalizado` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_concierto` (`id_concierto`),
  CONSTRAINT `FK_reserva_concierto` FOREIGN KEY (`id_concierto`) REFERENCES `concierto` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla boleteria.reserva: ~2 rows (aproximadamente)
/*!40000 ALTER TABLE `reserva` DISABLE KEYS */;
INSERT INTO `reserva` (`id`, `Asiento`, `Nombre`, `Rut`, `Edad`, `Correo`, `id_concierto`, `Finalizado`) VALUES
	(1, 2, 'wfefew', '12332', 12, 'fwewfe', 1, 0),
	(2, 4, 'wfefew', '12332', 12, 'fwewfe', 1, 0);
/*!40000 ALTER TABLE `reserva` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
