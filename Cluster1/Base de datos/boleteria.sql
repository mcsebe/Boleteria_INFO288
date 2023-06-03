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
  `Cola` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_locacion` (`id_locacion`),
  CONSTRAINT `FK_concierto_locacion` FOREIGN KEY (`id_locacion`) REFERENCES `locacion` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla boleteria.concierto: ~6 rows (aproximadamente)
/*!40000 ALTER TABLE `concierto` DISABLE KEYS */;
INSERT INTO `concierto` (`id`, `Nombre`, `Precio`, `Fecha`, `id_locacion`, `Cola`) VALUES
	(1, 'Metallica', 40000, '2023-11-20 17:00:00', 1, 'metallica'),
	(2, 'The Weeknd', 40000, '2023-12-01 18:30:00', 1, 'weeknd'),
	(3, 'Siames', 15000, '2023-06-28 18:00:00', 2, 'otros'),
	(4, 'Molotov', 20000, '2023-08-20 19:00:00', 2, 'otros'),
	(5, 'Movimiento Original', 12000, '2023-08-04 20:00:00', 3, 'otros'),
	(6, 'Chyste-MC', 12000, '2023-07-17 19:00:00', 3, 'otros');
/*!40000 ALTER TABLE `concierto` ENABLE KEYS */;

-- Volcando estructura para tabla boleteria.locacion
CREATE TABLE IF NOT EXISTS `locacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) NOT NULL DEFAULT '0',
  `Ciudad` varchar(50) NOT NULL DEFAULT '0',
  `Region` varchar(50) NOT NULL DEFAULT '0',
  `Capacidad` int(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla boleteria.locacion: ~3 rows (aproximadamente)
/*!40000 ALTER TABLE `locacion` DISABLE KEYS */;
INSERT INTO `locacion` (`id`, `Nombre`, `Ciudad`, `Region`, `Capacidad`) VALUES
	(1, 'Estadio Bicentenario', 'Santiago', 'Metropolitana', 1000),
	(2, 'Estadio Monumental', 'Santiago', 'Metropolitana', 1000),
	(3, 'Parque Saval', 'Valdivia', 'Los Ríos', 500);
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
  `TiempoSelec` datetime DEFAULT NULL,
  `TiempoPago` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_concierto` (`id_concierto`),
  CONSTRAINT `FK_reserva_concierto` FOREIGN KEY (`id_concierto`) REFERENCES `concierto` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla boleteria.reserva: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `reserva` DISABLE KEYS */;
/*!40000 ALTER TABLE `reserva` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
