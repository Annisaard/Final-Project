-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.4.22-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for hasiltest
CREATE DATABASE IF NOT EXISTS `hasiltest` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `hasiltest`;

-- Dumping structure for table hasiltest.answer
CREATE TABLE IF NOT EXISTS `answer` (
  `IP` text DEFAULT '0',
  `Hasil` int(11) DEFAULT 0,
  `P0` int(11) DEFAULT NULL,
  `P1` int(11) DEFAULT NULL,
  `P2` int(11) DEFAULT NULL,
  `P3` int(11) DEFAULT NULL,
  `P4` int(11) DEFAULT NULL,
  `P5` int(11) DEFAULT NULL,
  `P6` int(11) DEFAULT NULL,
  `P7` int(11) DEFAULT NULL,
  `P8` int(11) DEFAULT NULL,
  `P9` int(11) DEFAULT NULL,
  `P10` int(11) DEFAULT NULL,
  `P11` int(11) DEFAULT NULL,
  `P12` int(11) DEFAULT NULL,
  `P13` int(11) DEFAULT NULL,
  `P14` int(11) DEFAULT NULL,
  `P15` int(11) DEFAULT NULL,
  `P16` int(11) DEFAULT NULL,
  `P17` int(11) DEFAULT NULL,
  `P18` int(11) DEFAULT NULL,
  `P19` int(11) DEFAULT NULL,
  `P20` int(11) DEFAULT NULL,
  `P21` int(11) DEFAULT NULL,
  `P22` int(11) DEFAULT NULL,
  `P23` int(11) DEFAULT NULL,
  `P24` int(11) DEFAULT NULL,
  `P25` int(11) DEFAULT NULL,
  `P26` int(11) DEFAULT NULL,
  `P27` int(11) DEFAULT NULL,
  `P28` int(11) DEFAULT NULL,
  `P29` int(11) DEFAULT NULL,
  `P30` int(11) DEFAULT NULL,
  `P31` int(11) DEFAULT NULL,
  `P32` int(11) DEFAULT NULL,
  `P33` int(11) DEFAULT NULL,
  `P34` int(11) DEFAULT NULL,
  `P35` int(11) DEFAULT NULL,
  `P36` int(11) DEFAULT NULL,
  `P37` int(11) DEFAULT NULL,
  `P38` int(11) DEFAULT NULL,
  `P39` int(11) DEFAULT NULL,
  `P40` int(11) DEFAULT NULL,
  `P41` int(11) DEFAULT NULL,
  `P42` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Dumping data for table hasiltest.answer: ~0 rows (approximately)
/*!40000 ALTER TABLE `answer` DISABLE KEYS */;
/*!40000 ALTER TABLE `answer` ENABLE KEYS */;

-- Dumping structure for table hasiltest.depresi
CREATE TABLE IF NOT EXISTS `depresi` (
  `IP` text DEFAULT NULL,
  `nama` text DEFAULT NULL,
  `Score_Depresi` varchar(50) DEFAULT NULL,
  `Score_Anxiety` varchar(50) DEFAULT NULL,
  `Score_Stress` varchar(50) DEFAULT NULL,
  `TK_Depresi` varchar(50) DEFAULT NULL,
  `TK_Anxiety` varchar(50) DEFAULT NULL,
  `TK_Stress` varchar(50) DEFAULT NULL,
  `Prediksi` varchar(50) DEFAULT NULL,
  `Penjelasan` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Dumping data for table hasiltest.depresi: ~92 rows (approximately)
/*!40000 ALTER TABLE `depresi` DISABLE KEYS */;
INSERT INTO `depresi` (`IP`, `nama`, `Score_Depresi`, `Score_Anxiety`, `Score_Stress`, `TK_Depresi`, `TK_Anxiety`, `TK_Stress`, `Prediksi`, `Penjelasan`) VALUES
	('172.70.147.184', 'Fadhil', '20', '7', '15', 'Sedang', 'normal', 'ringan', 'Jaga Kesehatan Mental dan Tidur yang Cukup', 'Kurang tidur memiliki efek negatif yang signifikan'),
	('172.70.147.184', 'Dandunk', '43', '14', '28', 'Sangat Parah', 'sedang', 'parah', 'Meditasi dan Terapi Musik ', 'Meditasi bekerja untuk mengalihkan pikiran kamu da'),
	('172.70.147.142', 'Ichwan nauval', '13', '4', '14', 'Ringan', 'normal', 'normal', 'Jaga Kesehatan Mental dan Olahraga', 'Dengan berolahraga teratur dapat mengurangi tingka'),
	('172.70.147.162', 'Diah Aisyah', '22', '7', '15', 'Parah', 'normal', 'ringan', 'Jaga Kesehatan Mental dan Meditasi', 'Meditasi bekerja untuk mengalihkan pikiran kamu da'),
	('172.70.147.162', 'Azis Fauzi', '18', '13', '18', 'Sedang', 'sedang', 'ringan', 'Meditasi dan Tidur yang cukup  ', 'Meditasi bekerja untuk mengalihkan pikiran kamu da'),
	('172.70.147.180', 'Dewi Swarni ', '12', '6', '10', 'Ringan', 'normal', 'normal', 'Jaga Kesehatan Mental dan Kegiatan yang menyenangk', 'Luangkan waktu kamu untuk kegiatan santai seperti '),
	('172.70.147.162', 'Dewi Swarni ', '12', '6', '10', 'Ringan', 'normal', 'normal', 'Jaga Kesehatan Mental dan Kegiatan yang menyenangk', 'Luangkan waktu kamu untuk kegiatan santai seperti '),
	('172.70.147.142', NULL, '14', '6', '10', 'Sedang', 'normal', 'normal', 'Jaga Kesehatan Mental dan Olahraga', 'Dengan berolahraga teratur dapat mengurangi tingka'),
	('172.70.147.162', NULL, '15', '6', '14', 'Sedang', 'normal', 'normal', 'Jaga Kesehatan Mental dan Olahraga', 'Dengan berolahraga teratur dapat mengurangi tingka'),
	('172.70.147.184', NULL, '8', '3', '8', 'Normal', 'normal', 'normal', 'Jaga Kesehatan Mental', 'Tetap jaga Kesehatan mental kamu dan hindari hal y'),
	('172.70.147.162', NULL, '17', '7', '18', 'Sedang', 'normal', 'ringan', 'Jaga Kesehatan Mental dan Tidur yang Cukup', 'Kurang tidur memiliki efek negatif yang signifikan'),
	('172.70.147.184', 'Rosanitasari Dyah ayu Nurfitria', '29', '6', '33', 'Sangat Parah', 'normal', 'sangat parah', 'Jaga Kesehatan Mental dan Yoga', 'Dengan memfokuskan pikiran kamu pada gerakan dan p'),
	('172.70.147.162', NULL, '26', '8', '25', 'Parah', 'ringan', 'sedang', 'Latihan pernapasan kamu dan Tetap Meditasi  ', 'Ketika kamu khawatir, kamu menjadi cemas dan berna'),
	('172.70.147.184', 'Fadhil', '23', '5', '19', 'Parah', 'normal', 'sedang', 'Jaga Kesehatan Mental dan Manajemen waktu dengan b', 'Manajemen waktu yang baik dapat mengurangi distres'),
	('172.70.147.180', 'Diaan', '39', '11', '18', 'Sangat Parah', 'sedang', 'ringan', 'Meditasi dan Terapi Musik ', 'Meditasi bekerja untuk mengalihkan pikiran kamu da'),
	('172.70.147.142', 'rifqi', '35', '11', '26', 'Sangat Parah', 'sedang', 'parah', 'Meditasi dan Terapi Musik ', 'Meditasi bekerja untuk mengalihkan pikiran kamu da'),
	('172.70.142.218', 'Muhamad Rifqi Firdaus', '12', '5', '19', 'Ringan', 'normal', 'sedang', 'Jaga Kesehatan Mental dan Olahraga', 'Dengan berolahraga teratur dapat mengurangi tingka'),
	('172.70.147.162', 'Rahmi', '34', '12', '29', 'Sangat Parah', 'sedang', 'parah', 'Meditasi dan Terapi Musik ', 'Meditasi bekerja untuk mengalihkan pikiran kamu da'),
	('172.70.147.184', 'M agung vafky ideal', '16', '4', '14', 'Sedang', 'normal', 'normal', 'Jaga Kesehatan Mental dan Olahraga', 'Dengan berolahraga teratur dapat mengurangi tingka'),
	('172.70.147.162', 'Daniel', '28', '7', '20', 'Sangat Parah', 'normal', 'sedang', 'Jaga Kesehatan Mental dan Manajemen waktu dengan b', 'Manajemen waktu yang baik dapat mengurangi distres'),
	('172.70.147.184', 'Dandunk Ariyon', '20', '7', '23', 'Sedang', 'normal', 'sedang', 'Jaga Kesehatan Mental dan Manajemen waktu dengan b', 'Manajemen waktu yang baik dapat mengurangi distres'),
	('172.70.147.180', 'Om', '29', '12', '23', 'Sangat Parah', 'sedang', 'sedang', 'Meditasi dan Manajemen waktu dengan baik ', 'Meditasi bekerja untuk mengalihkan pikiran kamu da'),
	('172.70.142.218', 'Om', '29', '12', '23', 'Sangat Parah', 'sedang', 'sedang', 'Meditasi dan Manajemen waktu dengan baik ', 'Meditasi bekerja untuk mengalihkan pikiran kamu da'),
	('172.70.188.46', 'nawval', '24', '7', '14', 'Parah', 'normal', 'normal', 'Jaga Kesehatan Mental dan Gaya Hidup sehat', 'Pola hidup yang sehat, Makan makanan yang sehat, k'),
	('172.70.143.9', 'Arin', '7', '5', '7', 'Normal', 'normal', 'normal', 'Jaga Kesehatan Mental', 'Tetap jaga Kesehatan mental kamu dan hindari hal y'),
	('172.70.147.142', 'Zerlinda', '12', '6', '19', 'Ringan', 'normal', 'sedang', 'Jaga Kesehatan Mental dan Olahraga', 'Dengan berolahraga teratur dapat mengurangi tingka'),
	('172.70.188.150', 'Vecghy James Pratama', '19', '6', '11', 'Sedang', 'normal', 'normal', 'Jaga Kesehatan Mental dan Olahraga', 'Dengan berolahraga teratur dapat mengurangi tingka'),
	('172.70.147.142', 'Nadn', '23', '4', '18', 'Parah', 'normal', 'ringan', 'Jaga Kesehatan Mental dan Meditasi', 'Meditasi bekerja untuk mengalihkan pikiran kamu da'),
	('172.70.147.180', 'ummilkhair', '9', '3', '9', 'Normal', 'normal', 'normal', 'Jaga Kesehatan Mental', 'Tetap jaga Kesehatan mental kamu dan hindari hal y'),
	('172.70.147.184', 'Tiara ', '14', '1', '5', 'Sedang', 'normal', 'normal', 'Jaga Kesehatan Mental dan Olahraga', 'Dengan berolahraga teratur dapat mengurangi tingka'),
	('172.70.147.184', NULL, '37', '11', '27', 'Sangat Parah', 'sedang', 'parah', 'Meditasi dan Terapi Musik ', 'Meditasi bekerja untuk mengalihkan pikiran kamu da'),
	('172.70.147.142', 'Nurul fajri', '20', '7', '20', 'Sedang', 'normal', 'sedang', 'Jaga Kesehatan Mental dan Manajemen waktu dengan b', 'Manajemen waktu yang baik dapat mengurangi distres'),
	('172.70.147.142', 'Syaza putri ', '5', '4', '14', 'Normal', 'normal', 'normal', 'Jaga Kesehatan Mental', 'Tetap jaga Kesehatan mental kamu dan hindari hal y'),
	('172.70.147.142', 'Winda', '25', '12', '16', 'Parah', 'sedang', 'ringan', 'Meditasi dan Tidur yang cukup  ', 'Meditasi bekerja untuk mengalihkan pikiran kamu da'),
	('172.70.142.72', 'Fadhil', '14', '4', '11', 'Sedang', 'normal', 'normal', 'Jaga Kesehatan Mental dan Olahraga', 'Dengan berolahraga teratur dapat mengurangi tingka'),
	('172.70.142.252', 'Dandy Akroman', '2', '0', '4', 'Normal', 'normal', 'normal', 'Jaga Kesehatan Mental', 'Tetap jaga Kesehatan mental kamu dan hindari hal y'),
	('172.70.147.162', 'Muhamad Rifqi Firdaus', '36', '8', '19', 'Sangat Parah', 'ringan', 'sedang', 'Latihan pernapasan kamu dan Art terapi ', 'Ketika kamu khawatir, kamu menjadi cemas dan berna'),
	('172.70.147.180', 'Zakia', '22', '12', '12', 'Parah', 'sedang', 'normal', 'Meditasi dan Menggunakan Aroma Terapi ', 'Meditasi bekerja untuk mengalihkan pikiran kamu da'),
	('172.70.147.142', 'Yoga Dwi Yansyah', '15', '4', '13', 'Sedang', 'normal', 'normal', 'Jaga Kesehatan Mental dan Olahraga', 'Dengan berolahraga teratur dapat mengurangi tingka'),
	('172.70.147.162', NULL, '46', '16', '32', 'Sangat Parah', 'parah', 'parah', 'Art Terapi dan Journaling  ', 'Art therapy memberikan ruang untuk mengekspresikan'),
	('172.70.147.162', NULL, '36', '4', '14', 'Sangat Parah', 'normal', 'normal', 'Jaga Kesehatan Mental dan Terapi Musik', 'Dengan mendengarkan musik klasik atau bernyanyi be'),
	('172.70.147.162', 'Nindia', '19', '12', '15', 'Sedang', 'sedang', 'ringan', 'Meditasi dan Tidur yang cukup  ', 'Meditasi bekerja untuk mengalihkan pikiran kamu da'),
	('172.70.147.180', NULL, '3', '2', '3', 'Normal', 'normal', 'normal', 'Jaga Kesehatan Mental', 'Tetap jaga Kesehatan mental kamu dan hindari hal y'),
	('172.70.147.184', NULL, '1', '0', '6', 'Normal', 'normal', 'normal', 'Jaga Kesehatan Mental', 'Tetap jaga Kesehatan mental kamu dan hindari hal y'),
	('172.70.147.184', 'Septia Cindy Angella', '14', '5', '11', 'Sedang', 'normal', 'normal', 'Jaga Kesehatan Mental dan Olahraga', 'Dengan berolahraga teratur dapat mengurangi tingka'),
	('172.70.147.142', 'ulfah', '18', '7', '13', 'Sedang', 'normal', 'normal', 'Jaga Kesehatan Mental dan Olahraga', 'Dengan berolahraga teratur dapat mengurangi tingka'),
	('172.68.144.121', NULL, '5', '2', '4', 'Normal', 'normal', 'normal', 'Jaga Kesehatan Mental', 'Tetap jaga Kesehatan mental kamu dan hindari hal y'),
	('172.70.143.9', 'Ann', '23', '10', '0', 'Parah', 'sedang', 'normal', 'Meditasi dan Gaya hidup sehat  ', 'Meditasi bekerja untuk mengalihkan pikiran kamu da'),
	('172.70.147.142', 'Dinni Miftahul Al Azizah', '24', '9', '15', 'Parah', 'ringan', 'ringan', 'Latihan pernapasan kamu dan Tetap Meditasi  ', 'Ketika kamu khawatir, kamu menjadi cemas dan berna'),
	('172.70.143.9', 'Ann', '24', '9', '18', 'Parah', 'ringan', 'ringan', 'Latihan pernapasan kamu dan Tetap Meditasi  ', 'Ketika kamu khawatir, kamu menjadi cemas dan berna'),
	('172.70.147.184', NULL, '49', '20', '22', 'Sangat Parah', 'sangat parah', 'sedang', 'Art Terapi dan Manajemen waktu dengan baik  ', 'Art therapy memberikan ruang untuk mengekspresikan'),
	('172.70.142.72', 'Monica Sinta', '12', '4', '19', 'Ringan', 'normal', 'sedang', 'Jaga Kesehatan Mental dan Olahraga', 'Dengan berolahraga teratur dapat mengurangi tingka'),
	('172.70.142.218', 'Lillah', '16', '4', '15', 'Sedang', 'normal', 'ringan', 'Jaga Kesehatan Mental dan Olahraga', 'Dengan berolahraga teratur dapat mengurangi tingka'),
	('172.70.147.142', 'fitrianarahmah', '29', '12', '21', 'Sangat Parah', 'sedang', 'sedang', 'Meditasi dan Manajemen waktu dengan baik ', 'Meditasi bekerja untuk mengalihkan pikiran kamu da'),
	('172.70.142.252', 'Ilham', '16', '5', '22', 'Sedang', 'normal', 'sedang', 'Jaga Kesehatan Mental dan Manajemen waktu dengan b', 'Manajemen waktu yang baik dapat mengurangi distres'),
	('172.70.147.142', 'FA', '6', '3', '12', 'Normal', 'normal', 'normal', 'Jaga Kesehatan Mental', 'Tetap jaga Kesehatan mental kamu dan hindari hal y'),
	('172.70.147.184', 'Melody', '19', '6', '11', 'Sedang', 'normal', 'normal', 'Jaga Kesehatan Mental dan Olahraga', 'Dengan berolahraga teratur dapat mengurangi tingka'),
	('172.70.147.142', 'Daniel', '32', '7', '15', 'Sangat Parah', 'normal', 'ringan', 'Jaga Kesehatan Mental dan Terapi Musik', 'Dengan mendengarkan musik klasik atau bernyanyi be'),
	('172.70.147.142', 'Daniel', '32', '7', '15', 'Sangat Parah', 'normal', 'ringan', 'Jaga Kesehatan Mental dan Terapi Musik', 'Dengan mendengarkan musik klasik atau bernyanyi be'),
	('172.70.147.142', 'Fina', '19', '7', '19', 'Sedang', 'normal', 'sedang', 'Jaga Kesehatan Mental dan Manajemen waktu dengan b', 'Manajemen waktu yang baik dapat mengurangi distres'),
	('172.70.147.180', NULL, '46', '18', '30', 'Sangat Parah', 'parah', 'parah', 'Art Terapi dan Journaling  ', 'Art therapy memberikan ruang untuk mengekspresikan'),
	('172.70.147.180', 'Dewi Handayani', '4', '1', '21', 'Normal', 'normal', 'sedang', 'Jaga Kesehatan Mental dan Olahraga', 'Dengan berolahraga teratur dapat mengurangi tingka'),
	('172.70.147.162', 'nurul vadilla', '24', '1', '32', 'Parah', 'normal', 'parah', 'Jaga Kesehatan Mental dan Yoga', 'Dengan memfokuskan pikiran kamu pada gerakan dan p'),
	('172.70.147.162', 'n', '24', '1', '32', 'Parah', 'normal', 'parah', 'Jaga Kesehatan Mental dan Yoga', 'Dengan memfokuskan pikiran kamu pada gerakan dan p'),
	('172.70.142.252', 'Billa', '10', '1', '15', 'Ringan', 'normal', 'ringan', 'Jaga Kesehatan Mental dan Kegiatan yang menyenangk', 'Luangkan waktu kamu untuk kegiatan santai seperti '),
	('172.70.143.9', 'CK', '14', '4', '16', 'Sedang', 'normal', 'ringan', 'Jaga Kesehatan Mental dan Tidur yang Cukup', 'Kurang tidur memiliki efek negatif yang signifikan'),
	('172.70.147.184', 'Rahmi', '13', '5', '28', 'Ringan', 'normal', 'parah', 'Jaga Kesehatan Mental dan Menggunakan Aroma therap', 'Menggunakan aroma therapy saat tidur seperti esens'),
	('172.70.147.162', 'Nadia', '16', '4', '12', 'Sedang', 'normal', 'normal', 'Jaga Kesehatan Mental dan Olahraga', 'Dengan berolahraga teratur dapat mengurangi tingka'),
	('172.70.147.142', 'Asri Rahmi Izzati', '19', '9', '6', 'Sedang', 'ringan', 'normal', 'Latihan pernapasan kamu dan Olahraga ', 'Ketika kamu khawatir, kamu menjadi cemas dan berna'),
	('118.96.134.133', 'vyan', '30', '16', '10', 'Sangat Parah', 'parah', 'normal', 'Tulis kekhawatiran kamu dan Journaling ', 'Jika pikiran kamu cemas, coba buat catatan singkat'),
	('118.96.134.133', 'Rafid Fahar', '12', '4', '11', 'Ringan', 'normal', 'normal', 'Jaga Kesehatan Mental dan Kegiatan yang menyenangk', 'Luangkan waktu kamu untuk kegiatan santai seperti '),
	('103.111.102.10', 'Khalid', '18', '5', '18', 'Sedang', 'normal', 'ringan', 'Jaga Kesehatan Mental dan Olahraga', 'Dengan berolahraga teratur dapat mengurangi tingka'),
	('118.96.134.133', 'Bima Arya Saputra Wibowo', '30', '8', '19', 'Sangat Parah', 'ringan', 'sedang', 'Latihan pernapasan kamu dan Art terapi ', 'Ketika kamu khawatir, kamu menjadi cemas dan berna'),
	('112.215.174.101', 'Tri Mulia Pertiwi', '28', '10', '20', 'Sangat Parah', 'sedang', 'sedang', 'Meditasi dan Manajemen waktu dengan baik ', 'Meditasi bekerja untuk mengalihkan pikiran kamu da'),
	('2001:448a:1100:1b1a:b5d9:fe6b:72d4:84e3', NULL, '16', '3', '19', 'Sedang', 'normal', 'sedang', 'Jaga Kesehatan Mental dan Olahraga', 'Dengan berolahraga teratur dapat mengurangi tingka'),
	('2001:448a:4007:278e:80a7:3120:582b:7718', NULL, '13', '5', '7', 'Ringan', 'normal', 'normal', 'Jaga Kesehatan Mental dan Kegiatan yang menyenangk', 'Luangkan waktu kamu untuk kegiatan santai seperti '),
	('182.1.49.47,141.0.9.99', 'Teguh Rakhmat Mulyawan', '9', '2', '12', 'Normal', 'normal', 'normal', 'Jaga Kesehatan Mental', 'Tetap jaga Kesehatan mental kamu dan hindari hal y'),
	('114.124.163.227', 'Nabilla Hilzaviani', '26', '9', '18', 'Parah', 'ringan', 'ringan', 'Latihan pernapasan kamu dan Tetap Meditasi  ', 'Ketika kamu khawatir, kamu menjadi cemas dan berna'),
	('140.213.149.215', 'Fitri Handayani ', '20', '4', '23', 'Sedang', 'normal', 'sedang', 'Jaga Kesehatan Mental dan Manajemen waktu dengan b', 'Manajemen waktu yang baik dapat mengurangi distres'),
	('140.213.13.63', 'Poni indah sari', '22', '9', '18', 'Parah', 'ringan', 'ringan', 'Latihan pernapasan kamu dan Tetap Meditasi  ', 'Ketika kamu khawatir, kamu menjadi cemas dan berna'),
	('103.142.194.51', 'Latifah Khairiyyah fitri', '1', '1', '4', 'Normal', 'normal', 'normal', 'Jaga Kesehatan Mental', 'Tetap jaga Kesehatan mental kamu dan hindari hal y'),
	('180.252.160.91', 'Aam', '41', '5', '26', 'Sangat Parah', 'normal', 'parah', 'Jaga Kesehatan Mental dan Terapi Musik', 'Dengan mendengarkan musik klasik atau bernyanyi be'),
	('114.124.188.173', 'Afdhila', '27', '5', '21', 'Parah', 'normal', 'sedang', 'Jaga Kesehatan Mental dan Manajemen waktu dengan b', 'Manajemen waktu yang baik dapat mengurangi distres'),
	('114.124.188.99', 'Felya', '24', '15', '28', 'Parah', 'parah', 'parah', 'Tulis kekhawatiran kamu dan Meditasi ', 'Jika pikiran kamu cemas, coba buat catatan singkat'),
	('180.244.132.163', 'Hanifatul', '9', '1', '15', 'Normal', 'normal', 'ringan', 'Jaga Kesehatan Mental dan Tidur yang Cukup', 'Kurang tidur memiliki efek negatif yang signifikan'),
	('114.142.173.47', 'Ridha Melati N', '30', '8', '22', 'Sangat Parah', 'ringan', 'sedang', 'Latihan pernapasan kamu dan Art terapi ', 'Ketika kamu khawatir, kamu menjadi cemas dan berna'),
	('114.124.163.115', 'Nabila SW', '34', '13', '23', 'Sangat Parah', 'sedang', 'sedang', 'Meditasi dan Manajemen waktu dengan baik ', 'Meditasi bekerja untuk mengalihkan pikiran kamu da'),
	('114.124.161.35', 'annisaaa', '0', '0', '0', 'Normal', 'normal', 'normal', 'Jaga Kesehatan Mental', 'Tetap jaga Kesehatan mental kamu dan hindari hal y'),
	('114.124.163.115', 'hhh', '60', '21', '45', 'Sangat Parah', 'sangat parah', 'sangat parah', 'Art Terapi dan Terapi Musik  ', 'Art therapy memberikan ruang untuk mengekspresikan'),
	('180.243.0.232', 'KIUUS', '42', '42', '42', 'Sangat Parah', 'sangat parah', 'sangat parah', 'Art Terapi dan Terapi Musik  ', 'Art therapy memberikan ruang untuk mengekspresikan'),
	('114.124.217.100', NULL, '25', '20', '22', 'Parah', 'sangat parah', 'sedang', 'Art Terapi dan Manajemen waktu dengan baik  ', 'Art therapy memberikan ruang untuk mengekspresikan'),
	('114.124.163.134', NULL, '21', '21', '14', 'Parah', 'sangat parah', 'normal', 'Art Terapi  dan Menggunakan aroma terapi  ', 'Art therapy memberikan ruang untuk mengekspresikan');
/*!40000 ALTER TABLE `depresi` ENABLE KEYS */;

-- Dumping structure for table hasiltest.user
CREATE TABLE IF NOT EXISTS `user` (
  `IP` text DEFAULT NULL,
  `Total_Jawaban` int(255) DEFAULT 0,
  `Quest_num` int(255) DEFAULT 0,
  `D_Score` int(255) DEFAULT 0,
  `A_Score` int(255) DEFAULT 0,
  `S_Score` int(255) DEFAULT 0,
  `Hasil` int(255) DEFAULT 0,
  `nama` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Dumping data for table hasiltest.user: ~0 rows (approximately)
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
/*!40000 ALTER TABLE `user` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
