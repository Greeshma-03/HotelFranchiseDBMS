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


#************************************* Display to screen options implemented **************************************************

def Display(cur, con):
    clear()     # Clearing screen before displaying further options
    
    # Displaying options to choose

    print(blue("--------------------------------------------------------------------------", 'bold'))
    print(red("\t\t     Choose what you want to view", 'bold'))
    print(blue("--------------------------------------------------------------------------\n", 'bold'))
    
    print(green("--> 1.  Hotel branches", 'bold'))
    print(green("--> 2.  Staff details", 'bold'))
    print(green("--> 3.  Customer details", 'bold'))
    print(green("--> 4.  Departments", 'bold'))
    print(green("--> 5.  Land lords", 'bold'))
    print(green("--> 6.  Menu", 'bold'))
    print(green("--> 7.  Discounts", 'bold'))
    print(green("--> 8.  Furniture present", 'bold'))
    print(green("--> 9.  Raw material source", 'bold'))
    
    print("\n\n")

    viewOption = input(magenta("Your choice(1 - 10) ? ", 'bold'))

    clear()     # Clearing screen before displaying further oprtions

    if viewOption == '1':
        query = "SELECT * FROM Hotel;"
    elif viewOption == '2':
        
        clear()

        #****************************** Further options to view in staff details ***************************************
        print(magenta("------------- Select one from below -------------\n", 'bold'))
        print(yellow("--> 1. Branch-1 Staff details"))
        print(yellow("--> 2. Branch-2 Staff details"))
        print(yellow("--> 3. Branch-3 Staff details"))
        print(yellow("--> 4. Branch-4 Staff details"))
        print(yellow("--> 5. Branch-5 Staff details"))
        print(yellow("--> 6. Staff details of all branches\n"))

        staffOption = input(magenta("Your choice(1 - 5) ? ", 'bold'))

        if staffOption == '1':
            query = "SELECT Staff_ID, First_Name, Last_Name, concat(Day_date,'-',Month_date,'-',Year_date) AS DOB, Department_Name, Shift, Salary FROM Staff WHERE Branch_ID = 1;"
        elif staffOption == '2':
            query = "SELECT Staff_ID, First_Name, Last_Name, concat(Day_date,'-',Month_date,'-',Year_date) AS DOB, Department_Name, Shift, Salary FROM Staff WHERE Branch_ID = 2;"
        elif staffOption == '3':
            query = "SELECT Staff_ID, First_Name, Last_Name, concat(Day_date,'-',Month_date,'-',Year_date) AS DOB, Department_Name, Shift, Salary FROM Staff WHERE Branch_ID = 3;"
        elif staffOption == '4':
            query = "SELECT Staff_ID, First_Name, Last_Name, concat(Day_date,'-',Month_date,'-',Year_date) AS DOB, Department_Name, Shift, Salary FROM Staff WHERE Branch_ID = 4;"
        elif staffOption == '5':
            query = "SELECT Staff_ID, First_Name, Last_Name, concat(Day_date,'-',Month_date,'-',Year_date) AS DOB, Department_Name, Shift, Salary FROM Staff WHERE Branch_ID = 5;"
        elif staffOption == '6':
            query = "SELECT Staff_ID, First_Name, Last_Name, concat(Day_date,'-',Month_date,'-',Year_date) AS DOB, Department_Name, Shift, Salary FROM Staff;"

    elif viewOption == '3':
        
        clear()

        #****************************** Further options to view in customer details ******************************************
        print(magenta("------------- Select one from below -------------\n", 'bold'))
        print(yellow("--> 1. Customer details at Branch-1"))
        print(yellow("--> 2. Customer details at Branch-2"))
        print(yellow("--> 3. Customer details at Branch-3"))
        print(yellow("--> 4. Customer details at Branch-4"))
        print(yellow("--> 5. Customer details of all branches\n"))

        customerOption = input(magenta("Your choice(1 - 5) ? ", 'bold'))
    
        if customerOption == '1':
            query = "SELECT Customer_ID, concat(First_Name,' ',Last_Name) AS Name, Table_ID AS 'Table booked' FROM Customer WHERE Branch_ID = 1;"
        elif customerOption == '2':
            query = "SELECT Customer_ID, concat(First_Name,' ',Last_Name) AS Name, Table_ID AS 'Table booked' FROM Customer WHERE Branch_ID = 2;"
        elif customerOption == '3':
            query = "SELECT Customer_ID, concat(First_Name,' ',Last_Name) AS Name, Table_ID AS 'Table booked' FROM Customer WHERE Branch_ID = 3;"
        elif customerOption == '4':
            query = "SELECT Customer_ID, concat(First_Name,' ',Last_Name) AS Name, Table_ID AS 'Table booked' FROM Customer WHERE Branch_ID = 4;"
        elif customerOption == '5':
            query = "SELECT Customer_ID, concat(First_Name,' ',Last_Name) AS Name, Branch_ID, Table_ID AS 'Table booked' FROM Customer;"


    elif viewOption == '4':
        query = "SELECT * FROM Department;"
    elif viewOption == '5':
        query = "SELECT concat(First_Name,' ', Last_Name) AS Name, Monthly_Rent AS Rent, Branch_ID AS 'Owner of Branch' From Owners;"
    elif viewOption == '6':
        
        clear()

        #******************************** Further options to view in Menu ******************************************
        print(magenta("------------- Select one from below -------------\n", 'bold'))
        print(yellow("--> 1.  Veg Starters"))
        print(yellow("--> 2.  Non veg starters"))
        print(yellow("--> 3.  Soups"))
        print(yellow("--> 4.  Table dips"))
        print(yellow("--> 5.  Salads"))
        print(yellow("--> 6.  Sauce, Pasta, eggs and Lassies"))
        print(yellow("--> 7.  Deserts"))
        print(yellow("--> 8.  Non veg main course"))
        print(yellow("--> 9.  Veg main course"))
        print(yellow("--> 10. Chaat"))
        print(yellow("--> 11. View complete menu\n"))

        menuOption = input(magenta("Your choice(1 - 11) ? ", 'bold'))

        if menuOption == '1':
            query = "SELECT Food_Item_ID, Food_Item, Item_Cost FROM Menu WHERE Food_Type = 'Veg Starters';"
        elif menuOption == '2':
            query = "SELECT Food_Item_ID, Food_Item, Item_Cost FROM Menu WHERE Food_Type = 'Non-veg Starters';"
        elif menuOption == '3':
            query = "SELECT Food_Item_ID, Food_Item, Item_Cost FROM Menu WHERE Food_Type = 'Soup';"
        elif menuOption == '4':
            query = "SELECT Food_Item_ID, Food_Item, Item_Cost FROM Menu WHERE Food_Type = 'Table Dips';"
        elif menuOption == '5':
            query = "SELECT Food_Item_ID, Food_Item, Item_Cost FROM Menu WHERE Food_Type = 'Salads';"
        elif menuOption == '6':
            query = "SELECT Food_Item_ID, Food_Item, Item_Cost FROM Menu WHERE Food_Type = 'Sauce' OR 'Pasta Counter' OR 'Egg Counter' OR 'Lassi Counter';"
        elif menuOption == '7':
            query = "SELECT Food_Item_ID, Food_Item, Item_Cost FROM Menu WHERE Food_Type = 'Dessets';"
        elif menuOption == '8':
            query = "SELECT Food_Item_ID, Food_Item, Item_Cost FROM Menu WHERE Food_Type = 'Non-veg Main Course';"
        elif menuOption == '9':
            query = "SELECT Food_Item_ID, Food_Item, Item_Cost FROM Menu WHERE Food_Type = 'Veg Main Course';"
        elif menuOption == '10':
            query = "SELECT Food_Item_ID, Food_Item, Item_Cost FROM Menu WHERE Food_Type = 'Chaat';"
        elif menuOption == '11':
            query = "SELECT * FROM Menu;"
    
    elif viewOption == '7':
        query = "SELECT * From Discount;"
    elif viewOption == '8':
        clear()
        # **************************** Further options to view in furniture ****************************************
        print(blue("----- What do you want to view? -----", 'bold'))
        print(yellow("1. Specific furniture in all branches"))
        print(yellow("2. Furniture in a particular branch"))
        
        FurOption = input(cyan("Your choice(1-2)? "))
        if FurOption == '1':
            clear()

            print(blue("----- Choose one from below furniture -----", 'bold'))
            print(yellow("1. Table"))
            print(yellow("2. Stool"))
            print(yellow("3. Chair"))
            print(yellow("4. Desk"))
            print(yellow("5. Cushion"))

            furChoice = input(cyan("Your choice(1-5)? "))

            if furChoice == '1':
                query = "SELECT * FROM Furniture WHERE Furniture_Name = 'Table';"
            if furChoice == '2':
                query = "SELECT * FROM Furniture WHERE Furniture_Name = 'Stool';"
            if furChoice == '3':
                query = "SELECT * FROM Furniture WHERE Furniture_Name = 'Chair';"
            if furChoice == '4':
                query = "SELECT * FROM Furniture WHERE Furniture_Name = 'Desk';"
            if furChoice == '5':
                query = "SELECT * FROM Furniture WHERE Furniture_Name = 'Cushion';"
        
        elif FurOption == '2':
            clear()
            b_ID = int(input(yellow("Enter the branch ID: ")))
            validQuery = "Select * From Hotel WHERE Branch_ID = %d;" % (b_ID)
            
            cur = con.cursor()
            cur.execute(validQuery)
            data = cur.fetchall()

            # ****************** Error handling ***************************
            if not data:
                print(red("Error: No branch EXISTS with branch ID = %d !!" % (b_ID), 'bold'))
                print(red("... TRY AGAIN WITH NEW DATA !!"))
                return
            else:
                query = "Select * From Furniture WHERE Branch_ID = %d;" % (b_ID)
            
    elif viewOption == '9':
        query = "SELECT * From Raw_Materials;"

    try:
        no_of_rows = cur.execute(query)
    except Exception as e:
        print(e)
        print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
        return

    rows = cur.fetchall()
    viewTable(rows)
    con.commit()
