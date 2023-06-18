-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 09, 2022 at 10:49 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `game_info`
--

-- --------------------------------------------------------

--
-- Table structure for table `colr`
--

CREATE TABLE `colr` (
  `colr_id` int(11) NOT NULL,
  `colr` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `colr`
--

INSERT INTO `colr` (`colr_id`, `colr`) VALUES
(1, 'red.png'),
(2, 'blue.png');

-- --------------------------------------------------------

--
-- Table structure for table `coords`
--

CREATE TABLE `coords` (
  `coords_id` int(11) NOT NULL,
  `x` int(11) DEFAULT NULL,
  `y` int(11) DEFAULT NULL,
  `map` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `coords`
--

INSERT INTO `coords` (`coords_id`, `x`, `y`, `map`) VALUES
(1, 100, 200, 'map1'),
(2, 100, 202, 'map1'),
(3, 100, 300, 'map1'),
(4, 195, 200, 'map1'),
(5, 130, 115, 'map1'),
(6, 195, 60, 'map1'),
(7, 500, 70, 'map1'),
(8, 140, 85, 'map1'),
(9, 390, 170, 'map1'),
(10, 325, 95, 'map1'),
(11, 180, 100, 'map2'),
(12, 105, 130, 'map1');

-- --------------------------------------------------------

--
-- Table structure for table `player`
--

CREATE TABLE `player` (
  `idPlayer` int(11) NOT NULL,
  `player_name` varchar(45) NOT NULL,
  `player_password` varchar(45) NOT NULL,
  `coords_coords_id` int(11) DEFAULT NULL,
  `colr_colr_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `player`
--

INSERT INTO `player` (`idPlayer`, `player_name`, `player_password`, `coords_coords_id`, `colr_colr_id`) VALUES
(14, 'simen123', 'simenerkul', 1, 1),
(15, 'simen123', 'simenerkul', 2, 1),
(19, 'joon', 'jegerkul', 3, 1),
(20, 'simen', '123', 12, 1),
(21, 'simen', '1233', 1, 1),
(22, 'simenerkul', '123', 1, 1),
(23, 'simen123', '123312', 1, 1),
(34, 'simen', '1234', 10, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `colr`
--
ALTER TABLE `colr`
  ADD PRIMARY KEY (`colr_id`);

--
-- Indexes for table `coords`
--
ALTER TABLE `coords`
  ADD PRIMARY KEY (`coords_id`);

--
-- Indexes for table `player`
--
ALTER TABLE `player`
  ADD PRIMARY KEY (`idPlayer`),
  ADD KEY `fk_player_coords1` (`coords_coords_id`),
  ADD KEY `fk_player_colr1` (`colr_colr_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `colr`
--
ALTER TABLE `colr`
  MODIFY `colr_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `coords`
--
ALTER TABLE `coords`
  MODIFY `coords_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `player`
--
ALTER TABLE `player`
  MODIFY `idPlayer` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `player`
--
ALTER TABLE `player`
  ADD CONSTRAINT `fk_player_colr1` FOREIGN KEY (`colr_colr_id`) REFERENCES `colr` (`colr_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_player_coords1` FOREIGN KEY (`coords_coords_id`) REFERENCES `coords` (`coords_id`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
