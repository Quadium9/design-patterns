-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Wersja serwera:               10.6.4-MariaDB - mariadb.org binary distribution
-- Serwer OS:                    Win64
-- HeidiSQL Wersja:              11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Zrzut struktury bazy danych note
CREATE DATABASE IF NOT EXISTS `note` /*!40100 DEFAULT CHARACTER SET utf8mb3 COLLATE utf8mb3_polish_ci */;
USE `note`;

-- Zrzut struktury tabela note.note
CREATE TABLE IF NOT EXISTS `note` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) COLLATE utf8mb3_polish_ci NOT NULL,
  `create_date` date NOT NULL,
  `planned_date` date DEFAULT NULL,
  `description` tinytext COLLATE utf8mb3_polish_ci DEFAULT NULL,
  `active` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `FK_note_user` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_polish_ci;

-- Zrzucanie danych dla tabeli note.note: ~1 rows (około)
/*!40000 ALTER TABLE `note` DISABLE KEYS */;
INSERT INTO `note` (`id`, `title`, `create_date`, `planned_date`, `description`, `active`, `user_id`) VALUES
	(1, 'Ważne', '2022-07-14', '2022-07-18', 'Ważna czynność do wykonania w dniu jutrzejszym ze względu na ważne rzeczy, których nie można pominąć ze względu na to, że są ważne.', 1, 2),
	(2, 'Lista zakupów na wtorek', '2022-07-14', '2022-07-14', 'Masło,\r\nSzynka,\r\nPomidor,\r\nOgórek ,\r\nFasolka,\r\nPiwo,\r\nOlej roślinny,', 1, 2),
	(3, 'Zaliczenie projektu na studia', '2022-07-14', '2022-07-22', 'Projekt zaliczeniowy z projektu od wykładowcy', 1, 2),
	(4, 'TEST 6', '2022-07-14', '2022-07-14', 'Test 6 today note', 0, 2);
/*!40000 ALTER TABLE `note` ENABLE KEYS */;

-- Zrzut struktury tabela note.user
CREATE TABLE IF NOT EXISTS `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) COLLATE utf8mb3_polish_ci NOT NULL,
  `password` varchar(256) COLLATE utf8mb3_polish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_polish_ci;

-- Zrzucanie danych dla tabeli note.user: ~1 rows (około)
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` (`id`, `username`, `password`) VALUES
	(2, 'user123', '$2b$12$.yED8VkOmSv6KE5ji/miZePpprzPMyt0DaUS0TkmK/FaNVgImpk..'),
	(3, 'user321', '$2b$12$6FL9Ly44AOdtU7Ua0Fb8e.rdQ0cw10aHtk2nWYzmMwegPGGtWzitm');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
