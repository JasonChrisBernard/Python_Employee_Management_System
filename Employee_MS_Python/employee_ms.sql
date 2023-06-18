-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 13, 2023 at 12:23 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `employee_ms`
--

-- --------------------------------------------------------

--
-- Table structure for table `employee_t`
--

CREATE TABLE `employee_t` (
  `id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `salary` decimal(10,2) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `department` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `employee_t`
--

INSERT INTO `employee_t` (`id`, `name`, `salary`, `address`, `department`, `email`) VALUES
(3, 'John Doe', 5000.00, '123 Main St', 'Sales', 'johndoe@gmail.com'),
(4, 'Jane Smith', 4500.00, '456 Elm St', 'HR', 'janesmith@gmail.com'),
(5, 'Robert Johnson', 6000.00, '789 Oak St', 'IT', 'robertjohnson@gmail.com'),
(6, 'Emily Wilson', 5500.00, ' 987 Pine St', 'Marketing', 'emilywilson@gmail.com'),
(7, 'Michael Brown', 4000.00, '654 Elm St', 'Finance', 'michaelbrown@gmail.com'),
(8, 'Alice Davis', 4800.00, '321 Oak St', 'Sales', 'alicedavis@gmail.com'),
(9, 'Jessica Wilson', 5100.00, '456 Oak St', 'Marketing', 'jessicawilson@gmail.com'),
(10, 'Sarah Johnson', 5100.00, '456 Oak St', 'Marketing', 'jessicawilson@gmail.com'),
(11, 'Andrew Tate', 1000000.00, '50 Romania St', 'Finance', 'andrewbrown@gmail.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `employee_t`
--
ALTER TABLE `employee_t`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `employee_t`
--
ALTER TABLE `employee_t`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
