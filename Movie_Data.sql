-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Aug 03, 2018 at 12:21 PM
-- Server version: 5.7.23-0ubuntu0.16.04.1
-- PHP Version: 7.0.30-0ubuntu0.16.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Movie_Data`
--

-- --------------------------------------------------------

--
-- Table structure for table `Movie_Details`
--

CREATE TABLE `Movie_Details` (
  `id` varchar(11) NOT NULL,
  `title` text NOT NULL,
  `released_year` int(4) NOT NULL,
  `rating` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Movie_Details`
--

INSERT INTO `Movie_Details` (`id`, `title`, `released_year`, `rating`) VALUES
('tt0068646', 'The Godfather', 1972, 9.2),
('tt1375666', 'Inception', 2010, 8.8),
('tt2357129', 'Jobs', 2013, 6.1),
('tt5758778', 'Skyscraper', 2018, 6.2);

-- --------------------------------------------------------

--
-- Table structure for table `Movie_Genres`
--

CREATE TABLE `Movie_Genres` (
  `id` varchar(11) NOT NULL,
  `genre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Movie_Genres`
--

INSERT INTO `Movie_Genres` (`id`, `genre`) VALUES
('tt0068646', 'Crime'),
('tt0068646', ' Drama'),
('tt1375666', 'Action'),
('tt1375666', ' Adventure'),
('tt1375666', ' Sci-Fi'),
('tt2357129', 'Action'),
('tt5758778', 'Action'),
('tt5758778', ' Crime'),
('tt5758778', ' Drama');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Movie_Details`
--
ALTER TABLE `Movie_Details`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Movie_Genres`
--
ALTER TABLE `Movie_Genres`
  ADD KEY `id` (`id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Movie_Genres`
--
ALTER TABLE `Movie_Genres`
  ADD CONSTRAINT `Movie_Genres_ibfk_1` FOREIGN KEY (`id`) REFERENCES `Movie_Details` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
