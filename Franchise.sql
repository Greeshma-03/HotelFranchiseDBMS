-- MySQL dump 10.13  Distrib 8.0.26, for Linux (x86_64)
--
-- Host: localhost    Database: Franchise
-- ------------------------------------------------------
-- Server version	8.0.26-0ubuntu0.20.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Creating Database: Franchise
DROP DATABASE IF EXISTS Franchise;
CREATE SCHEMA Franchise;
USE Franchise;

-- Creating Table structure for table "Hotel"
DROP TABLE IF EXISTS Hotel;
CREATE TABLE Hotel(
    Branch_ID INT NOT NULL,
    Pin_Code INT NOT NULL,
    Street_No INT NOT NULL,
    Colony_Name VARCHAR(40) NOT NULL,
    Door_No INT NOT NULL,
    PRIMARY KEY (Branch_ID)
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

-- Inserting values into table "Hotel"
INSERT INTO Hotel VALUES
(1, 400065, 23, 'Privet Drive', 102),
(2, 400015, 9, 'KingsCross', 73),
(3, 400104, 17, 'Grimauld', 12),
(4, 400128, 12, 'Hogsmead', 3),
(5, 400122, 36, 'Hangelton', 6);

-- Creating Table structure for table "Furniture"
DROP TABLE IF EXISTS Furniture;
CREATE TABLE Furniture(
    Furniture_Name VARCHAR(40),
    Quantity INT,
    Branch_ID INT,
    PRIMARY KEY(Furniture_Name, Branch_ID),
    CONSTRAINT Furniture_ibfk_1 FOREIGN KEY (Branch_ID) REFERENCES Hotel (Branch_ID)
    ON UPDATE CASCADE
    ON DELETE CASCADE
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

-- Inserting values into table "Furniture"
INSERT INTO Furniture VALUES
('Table', 10, 1), ('Chair', 47, 1), ('Cushion', 12, 1), ('Desk', 2, 1), ('Stool', 0, 1),
('Table', 6, 2), ('Chair', 30, 2), ('Desk', 2, 2), ('Stool', 3, 2), ('Cushion', 0, 2),
('Table', 50, 3), ('Chair', 270, 3), ('Cushion', 316, 3), ('Desk', 7, 3), ('Stool', 15, 3),
('Table', 12, 4), ('Chair', 58, 4), ('Stool', 16, 4), ('Desk', 2, 4), ('Cushion', 0, 4),
('Table', 11, 5), ('Chair', 50, 5), ('Stool', 12, 5), ('Desk', 3, 5), ('Cushion', 10, 5);

-- Creating Table structure for table "Staff"
DROP TABLE IF EXISTS Staff;
CREATE TABLE IF NOT EXISTS Staff(
    Staff_ID INT NOT NULL AUTO_INCREMENT,
    Branch_ID INT NOT NULL,
    First_Name VARCHAR(40) NOT NULL,
    Last_Name VARCHAR(40),
    Day_date INT NOT NULL,
    Month_date INT NOT NULL,
    Year_date INT NOT NULL,
    Salary INT NOT NULL,
    Shift VARCHAR(40) NOT NULL,
    Department_Name VARCHAR(40) NOT NULL,
    PRIMARY KEY(Staff_ID),
    CONSTRAINT Staff_ibfk_1 FOREIGN KEY (Branch_ID) REFERENCES Hotel (Branch_ID)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
)ENGINE = InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET = utf8;


-- Inserting values into table "Staff" -- (First Hotel)
INSERT INTO Staff VALUES
(1, 1, 'Minerva', 'McGonagall', 12, 10, 1981, 10000, 'Morning', 'Chef'),
(2, 1, 'Albus', 'Dumbeldore', 9, 11, 1966, 27000, 'Afternoon', 'Manager'),
(3, 1, 'Arthur', 'Weasley', 30, 5, 1991, 2500, 'Morning', 'Security'),
(4, 1, 'Severus', 'Snape', 17, 9, 1985, 20000, 'Night', 'Manager'),
(5, 1, 'Rebues', 'Hagrid', 28, 3, 1971, 12000, 'Afternoon', 'Chef'),
(6, 1, 'Luna', 'Lovegood', 15, 7, 1989, 2300, 'Morning', 'Cleaner'),
(7, 1, 'Dean', 'Thomas', 14, 5, 1969, 15000, 'Morning', 'Chef'),
(8, 1, 'Abeforth', 'Dumbeldore', 10, 10, 1970, 19000, 'Morning', 'Manager'),
(11, 1, 'Draco', 'Malfoy', 5, 12, 1986, 1100, 'Afternoon', 'Security'),
(12, 1, 'Ted', 'Tonks', 4, 6, 1994, 1250, 'Afternoon', 'Cleaner'),
(13, 1, 'Bellatrix', 'Lestrange', 30, 7, 1982, 1210, 'Night', 'Cleaner'),
(14, 1, 'Regulus', 'Black', 21, 8, 1999, 11900, 'Night', 'Chef'),
(15, 1, 'Fluer', 'Delacaur', 15, 12, 1996, 14300, 'Afternoon', 'Chef');


-- Inserting values into table "Staff" -- (Second Hotel)
INSERT INTO Staff VALUES
(16, 2, 'Araina', 'Dumbeldore', 2, 10, 1991, 11300, 'Morning', 'Chef'),
(17, 2, 'Molly', 'Weasley', 19, 11, 1986, 18000, 'Afternoon', 'Manager'),
(18, 2, 'Reamus', 'Lupin', 20, 5, 1987, 2100, 'Morning', 'Security'),
(19, 2, 'Peter', 'Petigrew', 27, 9, 1987, 16000, 'Night', 'Manager'),
(20, 2, 'Petunia', 'Dursley', 18, 3, 1971, 11500, 'Afternoon', 'Chef'),
(21, 2, 'Kingsley', 'Shakelbolt', 15, 9, 1989, 2120, 'Morning', 'Cleaner'),
(22, 2, 'Belladora', 'Took', 24, 11, 1979, 12300, 'Morning', 'Chef'),
(23, 2, 'Bilbo', 'Baggins', 10, 12, 1984, 18300, 'Morning', 'Manager'),
(24, 2, 'Amos', 'Diggory', 23, 9, 1989, 9150, 'Night', 'Chef'),
(25, 2, 'Alecto', 'Carrowl', 22, 2, 1987, 2040, 'Night', 'Cleaner'),
(29, 2, 'Astoria', 'Malfoy', 21, 8, 1999, 11400, 'Night', 'Chef'),
(30, 2, 'Grabille', 'Delacaur', 5, 12, 1998, 13700, 'Afternoon', 'Chef');

-- Inserting values into table "Staff" -- (Third Hotel)
INSERT INTO Staff VALUES
(31, 3, 'Ginny', 'Weasley', 12, 10, 1998, 13300, 'Morning', 'Chef'),
(32, 3, 'Lily', 'Potter', 9, 7, 1987, 17950, 'Afternoon', 'Manager'),
(33, 3, 'Amycus', 'Carrowl', 23, 7, 1982, 1930, 'Morning', 'Security'),
(34, 3, 'Fred', 'Weasley', 17, 3, 1997, 13175, 'Night', 'Manager'),
(35, 3, 'George', 'Weasley', 17, 3, 1997, 10500, 'Afternoon', 'Chef'),
(38, 3, 'Rosmerta', 'Bartin', 20, 2, 1974, 17325, 'Morning', 'Manager'),
(39, 3, 'Cornelus', 'Fudge', 13, 8, 1982, 9025, 'Night', 'Chef'),
(40, 3, 'Percy', 'Weasley', 21, 7, 1989, 2015, 'Night', 'Cleaner'),
(41, 3, 'Dudley', 'Dursley', 18, 12, 1999, 1370, 'Afternoon', 'Security'),
(42, 3, 'Parvati', 'Patil', 29, 7, 1981, 1077, 'Afternoon', 'Cleaner'),
(43, 3, 'Cho', 'Chang', 22, 4, 1987, 1020, 'Night', 'Cleaner'),
(44, 3, 'John', 'McLaggen', 11, 1, 1989, 10400, 'Night', 'Chef');

-- Inserting Values into table "Staff" -- (Fourth hotel)
INSERT INTO Staff VALUES
(45, 4, 'Bathilda', 'Bagshot', 15, 4, 1988, 12700, 'Afternoon', 'Chef'),
(28, 4, 'Delphi', 'Diggory', 30, 7, 1982, 1010, 'Night', 'Cleaner'),
(46, 4, 'Bill', 'Weasley', 13, 6, 1987, 945, 'Night', 'Security'),
(47, 4, 'Charlie', 'Weasley', 24, 11, 1989, 12075, 'Morning', 'Chef'),
(48, 4, 'Vernon', 'Dursley', 27, 1, 1981, 16400, 'Afternoon', 'Manager'),
(49, 4, 'Xeno', 'Lovegood', 18, 12, 1972, 19700, 'Morning', 'Manager'),
(50, 4, 'Tom', 'Riddle', 24, 9, 1989, 11555, 'Night', 'Chef'),
(51, 4, 'Alastor', 'Moody', 27, 1, 1983, 19950, 'Night', 'Manager');

-- Inserting Values into "Staff" -- (Fifth Hotel)

INSERT INTO Staff VALUES
(26, 5, 'Lucius', 'Malfoy', 15, 2, 1989, 1500, 'Afternoon', 'Security'),
(27, 5, 'Crabbe', 'Goyle', 14, 7, 1991, 1150, 'Afternoon', 'Cleaner'),
(36, 5, 'Nymphadora', 'Tonks', 5, 9, 1981, 2100, 'Morning', 'Cleaner'),
(37, 5, 'Ted', 'Lupin', 14, 1, 1989, 12140, 'Morning', 'Chef'),
(9, 5, 'Pansy', 'Parkinson', 21, 7, 1999, 9500, 'Night', 'Chef'),
(10, 5, 'Morvolo', 'Gaunt', 22, 6, 1987, 2140, 'Night', 'Cleaner');


-- Creating Table structure for Table "Owners"
DROP TABLE IF EXISTS Owners;
CREATE TABLE Owners(
    First_Name VARCHAR(40) NOT NULL,
    Last_Name VARCHAR(40),
    Monthly_Rent INT NOT NULL,
    Branch_ID INT NOT NULL,
    PRIMARY KEY(First_Name, Last_Name),
    CONSTRAINT Owners_ibfk_1 FOREIGN KEY (Branch_ID) REFERENCES Hotel (Branch_ID)
    ON UPDATE CASCADE
    ON DELETE CASCADE
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

-- Inserting values into table "Owners"

INSERT INTO Owners VALUES
('Godric', 'Gryffindor', 40000, 1),
('Salazar', 'Slytherin', 70000, 2),
('Rowena', 'Ravenclaw', 95000, 3),
('Helga', 'Hufflepuff', 60700, 4),
('Hepzibah', 'Smith', 86500, 5);

-- Creating a Table structure for Table "Department"
DROP TABLE IF EXISTS Department;
CREATE TABLE Department(
    Department_Name VARCHAR(40) NOT NULL,
    Num_Workers INT NOT NULL,
    PRIMARY KEY(Department_Name)
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

-- Inserting values into table "Department"
INSERT INTO Department VALUES
('Manager', 12),
('Chef', 20),
('Cleaner', 12),
('Security', 7);

-- Creating a Table structure for Table "Menu"
DROP TABLE IF EXISTS Menu;
CREATE TABLE Menu(
    Food_Type VARCHAR(40),
    Food_Item_ID INT AUTO_INCREMENT,
    Item_Cost INT,
    Food_Item VARCHAR(70),
    PRIMARY KEY(Food_Item_ID)
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

-- Inserting values into table "Menu" --(Veg Starters)

INSERT INTO Menu VALUES
('Veg Starters', 1, 30, 'Achari Paneer Tikka'),
('Veg Starters', 2, 27, 'Hariyali Mushroom'),
('Veg Starters', 3, 25, 'Crispy corn'),
('Veg Starters', 4, 27, 'Oriental grill veg'),
('Veg Starters', 5, 27, 'Churasco Pineapple');

-- Inserting values into table "Menu" --(Non-veg Starters)
INSERT INTO Menu VALUES
('Non-veg Starters', 6, 39, 'Kalmi Chicken Tikka'),
('Non-veg Starters', 7, 37, 'Mutton Pudina Seekh'),
('Non-veg Starters', 8, 36, 'Bhuna wings'),
('Non-veg Starters', 9, 42, 'Coastal BBQ Fish'),
('Non-veg Starters', 10, 37, 'Chilly menuGarlic Prawns');

-- Inserting values into table "Menu" --(Soup)
INSERT INTO Menu VALUES
('Soup', 11, 22, 'Veg manchow Soup'),
('Soup', 12, 41, 'Lemon coriander chicken soup');

-- Inserting into table "Menu" --(table Dips)
INSERT INTO Menu VALUES
('Table Dips', 13, 10, 'Mint Chutney'),
('Table Dips', 14, 12, 'Garlic Mayo'),
('Table Dips', 15, 12, 'Mango Mint'),
('Table Dips', 16, 11, 'Tomato Salsa');

-- Inserting into table "Menu" --(Salads)
INSERT INTO Menu VALUES
('Salads', 17, 48, 'German Potato Salad'),
('Salads', 18, 51, 'Carrot Raisin Salad'),
('Salads', 19, 54, 'Green Salad'),
('Salads', 20, 54, 'Fried Fryum and Baked Papad');

-- Inserting values into table "Menu" --(Sauce, Pasta, Eggs, Lassi)
INSERT INTO Menu VALUES
('Sauce', 21, 31, 'Asian Black Pepper Sauce'),
('Sauce', 22, 36, 'Moroccan Sauce'),
('Sauce', 23, 40, 'Black Bean Sauce'),
('Sauce', 24, 48, 'Toofani Indian Curry Sauce'),
('Pasta Counter', 25, 41, 'Red Sauce and Cheesee Sauce'),
('Egg Counter', 26, 47, 'Fried Masala Egg'),
('Lassi Counter', 27, 52, 'Punjabi Lassi'),
('Lassi Counter', 28, 66, 'Dil Bahar Lassi'),
('Lassi Counter', 29, 57, 'Chaas');

-- Inserting into table "Menu" --(Desserts)
INSERT INTO Menu VALUES
('Dessets', 30, 124, 'Angoori Gulab Jamun'),
('Dessets', 31, 129, 'AB celebration Chocolate Pastry'),
('Dessets', 32, 101, 'Chocolate Walnut Brownie'),
('Dessets', 33, 135, 'Assorted Ice Cream');


-- Inserting into table "Menu" --(Non-veg main course)
INSERT INTO Menu VALUES
('Non-veg Main Course', 34, 99, 'Mutton Rogan Josh'),
('Non-veg Main Course', 35, 119, 'Allepy Fish Curry'),
('Non-veg Main Course', 36, 84, 'Szechuan Chicken Fried Rice'),
('Non-veg Main Course', 37, 121, 'Hyderabadi Chicken Dum Biryani');


-- Inserting into table "Menu" --(Veg Main course)
INSERT INTO Menu VALUES
('Veg Main Course', 38, 76, 'Kadhai Paneer'),
('Veg Main Course', 39, 121, 'Paneer Butter Masala'),
('Veg Main Course', 40, 69, 'Hyderbadi Veg Dum Viryani'),
('Veg Main Course', 41, 105, 'Butter Garlic Noodles');

-- Inserting values into table "menu" --(Chaat)
INSERT INTO Menu VALUES
('Chaat', 42, 74, 'Ragda Pattice'),
('Chaat', 43, 84, 'Pani Pauri'),
('Chaat', 44, 64, 'Dahi Puri'),
('Chaat', 45, 62, 'Bhel Puri');

-- Creating a Table structure for table "Customer"
DROP TABLE IF EXISTS Customer;
CREATE TABLE Customer(
    Customer_ID INT NOT NULL AUTO_INCREMENT,
    Branch_ID INT NOT NULL,
    First_Name VARCHAR(40),
    Last_Name VARCHAR(40),
    Table_ID INT,
    PRIMARY KEY(Customer_ID),
    CONSTRAINT Customer_ibfk_1 FOREIGN KEY (Branch_ID) REFERENCES Hotel (Branch_ID)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
)ENGINE = InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET = utf8;

-- Inserting values into table "Customer"
INSERT INTO Customer VALUES
(1, 3, 'Harry', 'Potter', 7),
(2, 3, 'Ron', 'Weasley', 7),
(3, 3, 'Hermione', 'Granger', 7),
(4, 2, 'Cedric', 'Diggory', 5),
(5, 2, 'Thorin', 'Oekinshield', 4),
(6, 2, 'Victor', 'Krum', 4),
(7, 1, 'Lockhart', 'Premb', 2),
(8, 4, 'Trienwel', 'Sinistra', 4),
(9, 4, 'James', 'Potter', 3),
(10, 4, 'Sirius', 'Black', 3),
(11, 1, 'Algus', 'Filch', 2),
(12, 1, 'Norris', 'Filch', 2);

-- Creating a table structure for table "Raw_Materials"
DROP TABLE IF EXISTS Raw_Materials;
CREATE TABLE Raw_Materials(
    Branch_ID INT NOT NULL,
    Source_ID INT NOT NULL,
    Source_Name VARCHAR(60),
    PRIMARY KEY(Branch_ID, Source_ID)
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

-- Inserting values into table "Raw_Materials"
INSERT INTO Raw_Materials VALUES
(1, 3, 'Dairy_1'),
(1, 2, 'Vegetable_Shop_1'),
(1, 1, 'Poultry_1'),
(2, 3, 'Dairy_2'),
(2, 2, 'Vegetable_Shop_2'),
(2, 1, 'Poultry_2'),
(3, 3, 'Dairy_3'),
(3, 2, 'Vegetable_Shop_3'),
(3, 1, 'Poultry_3'),
(4, 3, 'Dairy_4'),
(4, 2, 'Vegetable_Shop_4'),
(4, 1, 'Poultry_4'),
(5, 3, 'Dairy_5'),
(5, 2, 'Vegetable_Shop_5'),
(5, 1, 'Poultry_5');

-- Creating table structure for table "Poultry"
DROP TABLE IF EXISTS Poultry;
CREATE TABLE Poultry(
    Non_veg_Item VARCHAR(60),
    Item_Cost INT NOT NULL,
    Quantity FLOAT NOT NULL,
    Day_date INT NOT NULL,
    Month_date INT NOT NULL,
    Year_date INT NOT NULL,
    Branch_ID INT NOT NULL,
    PRIMARY KEY(Non_veg_Item, Branch_ID)
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

-- Inserting values into "Poultry"

INSERT INTO Poultry VALUES
('Chicken', 89, 50, 12, 10, 2020, 3),
('Egg', 40, 200, 9, 8, 2021, 3),
('Egg', 40, 210, 9, 8, 2021, 4),
('Chicken', 89, 70, 30, 9, 2021, 1),
('Egg', 40, 100, 16, 2, 2021, 2),
('Meat', 52, 100, 21, 11, 2020, 1),
('Meat', 52, 110, 26, 10, 2021, 4),
('Chicken', 89, 70, 18, 9, 2021, 5),
('Meat', 52, 110, 26, 10, 2021, 5),
('Egg', 40, 110, 26, 10, 2021, 1),
('Chicken', 89, 110, 23, 10, 2021, 4),
('Meat', 52, 110, 14, 10, 2021, 3),
('Chicken', 89, 70, 18, 10, 2021, 2),
('Meat', 52, 110, 26, 10, 2021, 2),
('Egg', 40, 250, 13, 4, 2021, 5);

-- Creating table structure for table "Vegetable_Shop"
DROP TABLE IF EXISTS Vegetable_Shop;
CREATE TABLE Vegetable_Shop(
    Vegetable_Name VARCHAR(60),
    Item_Cost INT NOT NULL,
    Quantity FLOAT NOT NULL,
    Day_date INT NOT NULL,
    Month_date INT NOT NULL,
    Year_date INT NOT NULL,
    Branch_ID INT NOT NULL,
    PRIMARY KEY(Vegetable_Name, Branch_ID)
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

-- Inserting values into "Vegetable_Shop"

INSERT INTO Vegetable_Shop VALUES
('Carrot', 12, 40, 25, 10, 2021, 5),
('Carrot', 12, 40, 30, 10, 2021, 4),
('Carrot', 12, 40, 30, 9, 2021, 3),
('Carrot', 12, 40, 25, 6, 2021, 2),
('Carrot', 12, 40, 27, 7, 2021, 1),
('Beetroot', 89, 50, 12, 11, 2020, 3),
('Onion', 40, 200, 9, 10, 2021, 5),
('Onion', 40, 200, 9, 9, 2021, 4),
('Onion', 40, 200, 9, 8, 2021, 3),
('Onion', 40, 200, 25, 10, 2021, 2),
('Onion', 40, 200, 26, 10, 2021, 1),
('Tomato', 40, 210, 9, 9, 2021, 5),
('Tomato', 40, 210, 9, 8, 2021, 4),
('Tomato', 40, 210, 9, 10, 2021, 3),
('Tomato', 40, 210, 19, 10, 2021, 2),
('Tomato', 40, 210, 9, 8, 2021, 1),
('Cabbage', 89, 70, 18, 12, 2021, 1),
('Cucumber', 40, 100, 16, 2, 2021, 2),
('Cauliflower', 36, 100, 25, 4, 2021, 5),
('Cauliflower', 36, 100, 25, 10, 2021, 4),
('Cauliflower', 36, 100, 25, 9, 2021, 3),
('Cauliflower', 36, 100, 30, 9, 2021, 2),
('Cauliflower', 36, 100, 25, 8, 2021, 1),
('Bottle Gaurd', 45, 80, 5, 8, 2021, 5),
('Bitter Gaurd', 40, 70, 29, 7, 2021, 2),
('Potato', 25, 150, 12, 12, 2020, 5),
('Potato', 25, 140, 11, 11, 2020, 4),
('Potato', 25, 130, 10, 10, 2020, 3),
('Potato', 25, 120, 9, 9, 2020, 2),
('Potato', 25, 110, 8, 18, 2020, 1);

-- Creating table structure for table "Dairy"
DROP TABLE IF EXISTS Dairy;
CREATE TABLE Dairy(
    Dairy_Item VARCHAR(60),
    Item_Cost INT NOT NULL,
    Quantity FLOAT NOT NULL,
    Day_date INT NOT NULL,
    Month_date INT NOT NULL,
    Year_date INT NOT NULL,
    Branch_ID INT NOT NULL,
    PRIMARY KEY(Dairy_Item, Branch_ID)
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

-- Inserting values into "Dairy"

INSERT INTO Dairy VALUES
('Milk', 12, 40, 30, 9, 2021, 5),
('Milk', 12, 40, 25, 10, 2021, 4),
('Milk', 12, 40, 25, 6, 2021, 3),
('Butter', 89, 50, 30, 9, 2021, 5),
('Butter', 89, 50, 30, 10, 2021, 4),
('Butter', 89, 50, 12, 11, 2020, 3),
('Butter', 89, 50, 25, 9, 2021, 4),
('Butter', 89, 50, 25, 8, 2021, 1),
('Cheese', 40, 200, 9, 9, 2021, 5),
('Cheese', 40, 200, 9, 10, 2021, 4),
('Cheese', 40, 200, 9, 8, 2021, 3),
('Cheese', 40, 200, 30, 10, 2021, 1),
('Yogurt', 40, 210, 9, 10, 2021, 5),
('Yogurt', 40, 210, 9, 9, 2021, 4),
('Yogurt', 40, 210, 9, 8, 2020, 3),
('Yogurt', 40, 210, 20, 10, 2021, 2),
('Yogurt', 40, 210, 30, 10, 2021, 1),
('Milk', 89, 70, 18, 12, 2021, 1),
('Milk', 40, 100, 16, 2, 2021, 2),
('Curd', 35, 150, 17, 6, 2021, 5),
('Cheese', 40, 100, 4, 7, 2021, 2),
('Curd', 35, 42, 14, 10, 2021, 4),
('Curd', 35, 42, 30, 10, 2021, 3),
('Curd', 35, 42, 30, 9, 2021, 2),
('Curd', 35, 42, 14, 8, 2021, 1);


-- Creating table structure for table "_Order"
DROP TABLE IF EXISTS _Order;
CREATE TABLE _Order(
    Quantity INT NOT NULL,
    Customer_ID INT NOT NULL,
    Food_Item_ID INT NOT NULL,
    PRIMARY KEY(Customer_ID, Food_Item_ID)
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

-- Inserting values into "_Order"

INSERT INTO _Order VALUES
(2, 4, 14),
(1, 4, 44),
(1, 4, 12),
(5, 2, 37),
(2, 1, 5),
(3, 1, 7),
(4, 7, 26),
(3, 11, 39);

-- Creating table structure for "Staff_Mobile_Number"
-- Multi-valued table
DROP TABLE IF EXISTS Staff_Mobile_Number;
CREATE TABLE Staff_Mobile_Number(
    Staff_ID INT NOT NULL,
    Mobile_Number BIGINT NOT NULL,
    PRIMARY KEY(Staff_ID,Mobile_Number),
    CONSTRAINT STN_ibfk_1 FOREIGN KEY (Staff_ID) REFERENCES Staff (Staff_ID)
    ON UPDATE CASCADE
    ON DELETE CASCADE
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

-- Inserting values into "Staff_Mobile_Number"

INSERT INTO Staff_Mobile_Number VALUES
(2, 1478963250),
(2, 5478963210),
(47, 0123654789),
(51, 3698521470),
(11, 4563210789),
(11, 8523697410),
(13, 8741236950);

-- Creating table structure for "Owners_Mobile_Number"
-- Multi-valued table
DROP TABLE IF EXISTS Owners_Mobile_Number;
CREATE TABLE Owners_Mobile_Number(
    First_Name VARCHAR(40),
    Last_Name VARCHAR(40),
    Mobile_Number BIGINT NOT NULL,
    Constraint OMN_ibfk_1 FOREIGN KEY (First_Name, Last_Name) 
    REFERENCES Owners (First_Name, Last_Name)
    ON UPDATE CASCADE
    ON DELETE CASCADE
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

-- Inserting values into "Owners_Mobile_Number"
INSERT INTO Owners_Mobile_Number VALUES
('Godric', 'Gryffindor', 9000500010),
('Godric', 'Gryffindor', 9000523410),
('Godric', 'Gryffindor', 9234500010),
('Salazar', 'Slytherin', 8000500010),
('Salazar', 'Slytherin', 8765500010),
('Salazar', 'Slytherin', 8133500010),
('Salazar', 'Slytherin', 8123500010),
('Rowena', 'Ravenclaw', 1234567890),
('Helga', 'Hufflepuff', 6000500010),
('Hepzibah', 'Smith', 4895841456);

-- Creating a table structure for table "Discount"
DROP TABLE IF EXISTS Discount;
CREATE TABLE Discount(
    Food_Item_ID INT NOT NULL,
    Discount_Amount INT NOT NULL,
    Min_Cost INT NOT NULL,
    PRIMARY KEY (Food_Item_ID, Min_Cost),
    Constraint Discount_ibfk_1
    FOREIGN KEY (Food_Item_ID) REFERENCES Menu (Food_Item_ID)
    ON UPDATE CASCADE
    ON DELETE CASCADE
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

-- Inserting values into "Discount"

INSERT INTO Discount VALUES
(12, 21, 250),
(12, 35, 350),
(12, 49, 599),
(28, 19, 259),
(31, 39, 379),
(9, 50, 549),
(44, 29, 499);

-- Creating a table structure for relationship "_Orders"
-- Customer - Orders - Menu(Food_Item)
--              |
--             Hotel
-- Above is a 3 degree relationship

DROP TABLE IF EXISTS _Orders;
CREATE TABLE _Orders(
    Food_Item_ID INT NOT NULL,
    Customer_ID INT NOT NULL,
    Branch_ID INT NOT NULL,
    PRIMARY KEY (Food_Item_ID, Customer_ID, Branch_ID),
    Constraint _Orders_ibfk_01 FOREIGN KEY (Food_Item_ID) REFERENCES Menu (Food_Item_ID)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,

    Constraint _Orders_ibfk_02 FOREIGN KEY (Customer_ID) REFERENCES Customer (Customer_ID)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,

    Constraint _Orders_ibfk_03 FOREIGN KEY (Branch_ID) REFERENCES Hotel (Branch_ID)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

-- Inserting values into "_Orders"

INSERT INTO _Orders VALUES
(12, 12, 4),
(41, 11, 1),
(41, 4, 1),
(28, 3, 3),
(42, 12, 4),
(36, 4, 1),
(27, 9, 2);

-- Creating a table structure for relationship "Offers"
-- "Hotel" offers "discount" on "order" from "Menu" to "Customer"
-- Above is a 5 degree relationship

DROP TABLE IF EXISTS Offers;
CREATE TABLE Offers(
    Food_Item_ID INT NOT NULL,
    Customer_ID INT NOT NULL,
    Branch_ID INT NOT NULL,
    Min_Cost INT NOT NULL,
    PRIMARY KEY (Food_Item_ID, Customer_ID, Branch_ID, Min_Cost),

    Constraint Offers_ibfk_1 FOREIGN KEY (Food_Item_ID) REFERENCES Menu (Food_Item_ID)
    ON UPDATE CASCADE
    ON DELETE CASCADE,

    Constraint Offers_ibfk_2 FOREIGN KEY (Customer_ID) REFERENCES Customer (Customer_ID)
    ON UPDATE CASCADE
    on DELETE CASCADE,

    Constraint Offers_ibfk_3 FOREIGN KEY (Branch_ID) REFERENCES Hotel (Branch_ID)
    ON UPDATE CASCADE
    on DELETE CASCADE,

    Constraint Offers_ibfk_4 FOREIGN KEY (Food_Item_ID, Min_Cost) REFERENCES Discount (Food_Item_ID, Min_Cost)
    ON UPDATE CASCADE
    on DELETE CASCADE
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

-- Inserting values into "Offers"

INSERT INTO Offers VALUES
(12, 12, 4, 250),
(28, 11, 1, 259),
(44, 4, 1, 499),
(9, 3, 3, 549),
(31, 12, 4, 379),
(12, 4, 1, 250),
(44, 9, 2, 499);

-- Creating a table structure for "Events"
DROP TABLE IF EXISTS Events;
CREATE TABLE Events(
    Branch_ID INT NOT NULL,
    Pin_Code INT NOT NULL,
    Street_Number INT NOT NULL,
    Colony_Name VARCHAR(70) NOT NULL,
    Door_No INT NOT NULL,
    PRIMARY KEY (Pin_Code, Street_Number, Colony_Name, Door_No)
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

-- Inserting values into "Events"

INSERT INTO Events VALUES
(4, 500012, 8, 'Hamstone', 12),
(1, 510100, 12, 'Maprud', 21),
(1, 500014, 3, 'Ravitol', 36);

-- Creating table structure for relationship "Caterings"
-- "Hotel" caterings for "orders" for "events".
-- Above is a 3 degree relationship.
DROP TABLE IF EXISTS Caterings;
CREATE TABLE Caterings(
    Branch_ID INT NOT NULL,
    Pin_Code INT NOT NULL,
    Street_Number INT NOT NULL,
    Colony_Name VARCHAR(70) NOT NULL,
    Door_No INT NOT NULL,
    Food_Item_ID INT NOT NULL,
    Customer_ID INT NOT NULL,
    PRIMARY KEY (Food_Item_ID, Customer_ID, Branch_ID, Pin_Code, Street_Number, Colony_Name, Door_No),
    
    CONSTRAINT Caterings_ibfk_1
    FOREIGN KEY (Branch_ID) REFERENCES Hotel (Branch_ID)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,
    
    CONSTRAINT Caterings_ibfk_2
    FOREIGN KEY (Pin_Code, Street_Number, Colony_Name, Door_No) 
    REFERENCES Events (Pin_Code, Street_Number, Colony_Name, Door_No)
    ON UPDATE CASCADE
    ON DELETE CASCADE,

    CONSTRAINT Caterings_ibfk_3
    FOREIGN KEY (Food_Item_ID) REFERENCES Menu (Food_Item_ID)
    ON UPDATE CASCADE
    ON DELETE CASCADE,

    CONSTRAINT Caterings_ibfk_4
    FOREIGN KEY (Customer_ID) REFERENCES Customer (Customer_ID)
    ON UPDATE CASCADE
    ON DELETE CASCADE
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

-- Inserting values into "Caterimgs"

INSERT INTO Caterings VALUES
(4, 500012, 8, 'Hamstone', 12, 21, 7),
(1, 510100, 12, 'Maprud', 21, 36, 11),
(1, 500014, 3, 'Ravitol', 36, 18, 5);
