import subprocess as sp
import pymysql
import pymysql.cursors
import sys

from Clear import *
from ViewTable import *
from colorama import Fore, Style
from simple_colors import *
from tabulate import tabulate
from os import system, name
from time import sleep

#*************************************** Finance analysis ************************************************************

def Finance(cur, con):
    clear()     # Clearing screen before displaying further options
    
    # Displaying options to choose

    print(blue("--------------------------------------------------------------------------", 'bold'))
    print(red("\t\t     Choose one from below to analyze", 'bold'))
    print(blue("--------------------------------------------------------------------------\n", 'bold'))
    
    print(green("--> 1.  Average monthly rent paid by the Franchise", 'bold'))
    print(green("--> 2.  Average cost of starters in Menu", 'bold'))
    print(green("--> 3.  Average cost of soups in Menu", 'bold'))
    print(green("--> 4.  Average cost of Table dips in Menu", 'bold'))
    print(green("--> 5.  Average cost of Salads in Menu", 'bold'))
    print(green("--> 6.  Average cost of Desserts in Menu", 'bold'))
    print(green("--> 7.  Average cost of Main-course in Menu", 'bold'))
    print(green("--> 8.  Average cost of Chaat in Menu", 'bold'))


    print("\n\n")

    financeOption = input(cyan("Your choice(1-8)? "))

    clear()

    if financeOption == '1':
        print(green("----- Analysis of Average monthly rent paid -----", 'bold'))
        query = "Select AVG(Monthly_Rent) AS 'Average Rent' From Owners;"
    elif financeOption == '2':
        print(green("----- Average cost of starters in menu -----", 'bold'))
        query = "SELECT AVG(Item_Cost) AS 'Average rate of Starters' FROM Menu WHERE Food_Type = 'Veg Starters' OR 'Non-veg Starters';"
    elif financeOption == '3':
        print(green("----- Average cost of soup in menu -----", 'bold'))
        query = "SELECT AVG(Item_Cost) AS 'Average rate of Soups' FROM Menu WHERE Food_Type = 'Soup';"
    elif financeOption == '4':
        print(green("----- Average cost of Table dips in menu -----", 'bold'))
        query = "SELECT AVG(Item_Cost) AS 'Average rate of table dips' FROM Menu WHERE Food_Type = 'Table Dips';"
    elif financeOption == '5':
        print(green("----- Average cost of Salads in menu -----", 'bold'))
        query = "SELECT AVG(Item_Cost) AS 'Average rate of soups' FROM Menu WHERE Food_Type = 'Salads';"
    elif financeOption == '6':
        print(green("----- Average cost of Desserts in menu -----", 'bold'))
        query = "SELECT AVG(Item_Cost) AS 'Average rate of soups' FROM Menu WHERE Food_Type = 'Dessets';"
    elif financeOption == '7':
        print(green("----- Average cost of main-course in menu -----", 'bold'))
        query = "SELECT AVG(Item_Cost) AS 'Average rate of main-course' FROM Menu WHERE Food_Type = 'Non-veg Main Course' OR 'Veg Main Course';"
    elif financeOption == '8':
        print(green("----- Average cost of chaat in menu -----", 'bold'))
        query = "SELECT AVG(Item_Cost) AS 'Average rate of chaat' FROM Menu WHERE Food_Type = 'Chaat';"

    try:
        no_of_rows = cur.execute(query)
    except Exception as e:
        print(e)
        print("\n\nError: PLEASE TRY AGAIN !\n")
        return

    rows = cur.fetchall()
    viewTable(rows)
    con.commit()



