SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `movie_data`
--

-- --------------------------------------------------------

--
-- Table structure for table `movie_details`
--

CREATE TABLE `movie_details` (
  `id` varchar(11) NOT NULL,
  `title` text NOT NULL,
  `released_year` int(4) NOT NULL,
  `rating` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `movie_details`
--

INSERT INTO `movie_details` (`id`, `title`, `released_year`, `rating`) VALUES
('tt0068646', 'The Godfather', 1972, 9.2),
('tt1375666', 'Inception', 2010, 8.8),
('tt2357129', 'Jobs', 2013, 6.1),
('tt5758778', 'Skyscraper', 2018, 6.2);

-- --------------------------------------------------------

--
-- Table structure for table `movie_genres`
--

CREATE TABLE `movie_genres` (
  `id` varchar(11) NOT NULL,
  `genre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `movie_genres`
--

INSERT INTO `movie_genres` (`id`, `genre`) VALUES
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
-- Indexes for table `movie_details`
--
ALTER TABLE `movie_details`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `movie_genres`
--
ALTER TABLE `movie_genres`
  ADD KEY `id` (`id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `movie_genres`
--
ALTER TABLE `movie_genres`
  ADD CONSTRAINT `movie_genres_ibfk_1` FOREIGN KEY (`id`) REFERENCES `movie_details` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
