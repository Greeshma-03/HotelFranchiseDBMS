import subprocess as sp
import pymysql
import pymysql.cursors

from colorama import Fore, Style
from simple_colors import *
from tabulate import tabulate
from Clear import *


def Add_Events(cur, con):

    ######Taking in the input##############
    try:
        clear()
        print("Enter the following details of the Event:")
        Full_Name = (input("Full Name of the costumer: ")).split(' ')
        Full_Name.append(" ")
        print("\n", "Address of the Event: ")
        House_No = int(input("   House No: "))
        Colony_Name = input("   Colony Name: ")
        Street_No = int(input("   Street No: "))
        Pin_Code = int(input("   Pin-Code: "))
        Branch_ID = int(input("Branch-ID the hotel: "))

        if not(Branch_ID > 0 and Branch_ID < 6):
            print("You entered a Invalid Branch-ID")
            return

        num_items = int(input("Enter the number of food items to order: "))
        if not(num_items >= 0 and num_items <= 25):
            print("You exceeded the maximum limit of orders")
            return

        food_items = []
        food_qty = []
        for var in range(num_items):
            food_items.append(input("Enter the Food item Name: "))
            food_qty.append(int(input("Enter the Food item quantity: ")))

    except Exception as e:
        print(red("Invalid data entered!!"))
        return

    ###########Processing the queries###########
    try:

        query = "INSERT INTO Events VALUES (%d,%d,%d,'%s',%d)" % (
            Branch_ID, Pin_Code, Street_No, Colony_Name, House_No)
        cur.execute(query)

        query = "INSERT INTO Customer(Branch_ID,First_Name,Last_Name) VALUES ('%d','%s','%s')" % (
            Branch_ID, Full_Name[0], Full_Name[1])
        cur.execute(query)

        for var in range(num_items):
            query = "SELECT Food_Item_ID FROM Menu WHERE Food_Item='%s'" % (
                food_items[var])
            cur.execute(query)
            x1 = cur.fetchone()


            if(not(bool(x1))):
                print("You entered an invalid food item name")
                con.rollback()
                return

            query = "SELECT MAX(Customer_ID) as Customer_ID FROM Customer"
            cur.execute(query)
            x2 = cur.fetchone()
            con.commit()     

            # print(x2)   

            query = "INSERT INTO _Order VALUES ('%d','%d','%d')" % (
                food_qty[var], int(x2["Customer_ID"]), x1["Food_Item_ID"])
            cur.execute(query)

        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to insert into database...")
        print(e)
        print(red("Try with different data!!"))
        return

    print(green("Data has been successfully added!!"))


def Add_Order(cur, con):

    ######Taking in the input##############
    clear()
    try:
        print("Enter the following details of the Order:")
        Full_Name = (input("Full Name of the costumer: ")).split(' ')
        Full_Name.append(" ")

        Table_ID = int(input("Please Enter your Table-ID:"))
        print("\n", "Enter the food-item details:")
        Branch_ID = int(input("Branch-ID the hotel: "))

        if not(Branch_ID > 0 and Branch_ID < 6):
            print("You entered a Invalid Branch-ID")
            return

        num_items = int(input("Enter the number of food items to order: "))
        if not(num_items > 0 and num_items <= 25):
            print("You exceeded the maximum limit of orders")
            return

        food_items = []
        food_qty = []
        for var in range(num_items):
            food_items.append(input("Enter the Food item Name: "))
            food_qty.append(int(input("Enter the Food item quantity: ")))

    except Exception as e:
        print(red("Invalid data entered!!"))
        return

    ###########Processing the queries###########
    try:
        query = "INSERT INTO Customer(Branch_ID,First_Name,Last_Name,Table_ID) VALUES ('%d','%s','%s','%d')" % (
            Branch_ID, Full_Name[0], Full_Name[1], Table_ID)
        cur.execute(query)

        for var in range(num_items):
            query = "SELECT Food_Item_ID FROM Menu WHERE Food_Item='%s'" % (
                food_items[var])
            cur.execute(query)
            x1 = cur.fetchone()

            if(not(bool(x1))):
                print("You entered an invalid food item name")
                con.rollback()
                return
        
            query = "SELECT MAX(Customer_ID) as Customer_ID FROM Customer"
            cur.execute(query)
            x2 = cur.fetchone()

            query = "INSERT INTO _Order VALUES ('%d','%d','%d')" % (
                food_qty[var], x2["Customer_ID"], x1["Food_Item_ID"])
            cur.execute(query)
        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to insert into database...")
        print(e)
        print("Try with different data")
        return

    print(green("Data has been successfully added!!"))


def Add_Menu(cur, con):

    #############Taking in the input##############
    clear()
    try:
        print("Enter the details of food-item to add: ")
        Food_Item = input("Food Item Name: ")
        Food_type = input("Food Type: ")
        Food_Cost = int(input("Food Item Cost: "))
        disco = input("Do you want to give discount on this item? [Y/n]: ")
        if(disco == 'Y' or disco == 'y'):
            Min = int(input("  Enter the Minimum Cost to avail discount: "))
            amt = int(input("  Enter the corresponding discount Amount: "))

    except Exception as e:
        print("Invalid data is entered")
        return

    ###########Processing the queries###########
    try:
        query = "INSERT INTO Menu(Food_Type,Item_Cost,Food_Item) VALUES ('%s','%d','%s')" % (
            Food_type, Food_Cost, Food_Item)
        cur.execute(query)
        con.commit()

        if(disco == 'Y' or disco == 'y'):            
            query = "SELECT MAX(Food_Item_ID) as Food_Item_ID FROM Menu"
            cur.execute(query)
            x = cur.fetchone()
            con.commit()

            query = "INSERT INTO Discount VALUES ('%d','%d','%d')" % (
                x["Food_Item_ID"], amt, Min)
            cur.execute(query)

        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to insert into database...")
        print(e)
        print("Try with different data")
        return

    print(green("Data has been successfully added!!"))


def Add_Furniture(cur, con):

    #############Taking in the input##############
    clear()
    try:
        print("Enter the following details of furniture: ")
        Branch = int(input("Enter the Branch-ID: "))
        if not(Branch > 0 and Branch < 6):
            print("You entered a Invalid Branch-ID")
            return
        Name = input("Enter the furniture name: ")
        Qty = int(input("Enter the furniture quantity to be added: "))

    except Exception as e:
        print(red("Invalid data is entered"))
        return

    ###########Processing the queries###########
    try:
        query = "SELECT Furniture_Name FROM Furniture WHERE Furniture_Name='%s' AND Branch_ID='%d'" % (
            Name, Branch)
        cur.execute(query)
        x1 = cur.fetchone()
        if((bool(x1))):
            print(yellow("Already inserted..Try to update!!"))
            con.rollback()
            return

        query = "INSERT INTO Furniture VALUES ('%s','%d','%d')" % (
            Name, Qty, Branch)
        cur.execute(query)
        con.commit()

    except Exception as e:
        con.rollback()
        print(red("Failed to insert into database..."))
        print(e)
        print(yellow("Try with different data"))
        return

    print(green("Data has been successfully added!!"))


def Add_Staff(cur, con):

    #############Taking in the input##############
    clear()
    try:
        print("Enter the following details of Staff: ")
        Full_Name = (input("Full Name of the staff: ")).split(' ')
        Full_Name.append(" ")
        branch_id = int((input("Branch ID of the staff: ")))

        if not(branch_id > 0 and branch_id < 6):
            print("You entered a Invalid Branch-ID")
            return

        dob = (input("Date of birth of the staff: (dd-mm-yyyy)")).split('-')

        shift = (input("Shift: "))
        true_shift = ['Morning', 'Afternoon', 'Night']
        if shift not in true_shift:
            print(red("Invalid shift entered"))
            return

        Dept = input("Department: ")
        phn = 9999999999
        phn = int(input("Mobile Number: "))
        sal = int(input("Salary: "))

    except Exception as e:
        print("Invalid data is entered")
        return

    ###########Processing the queries###########
    try:
        query = "SELECT Department_Name FROM Department WHERE Department_Name='%s'" % (
            Dept)
        cur.execute(query)
        x1 = cur.fetchone()
        if(not(bool(x1))):
            print("You entered an invalid Department item name")
            con.rollback()
            return

        query = "INSERT INTO Staff(Branch_ID,First_Name,Last_Name,Day_date,Month_date,Year_date,Salary,Shift,Department_Name) VALUES ('%d','%s','%s','%d','%d','%d','%d','%s','%s')" % (
            branch_id, Full_Name[0], Full_Name[1], int(dob[0]), int(dob[1]), int(dob[2]), sal, shift, Dept)
        cur.execute(query)
        
        con.commit()

        query = "SELECT MAX(Staff_ID) as Staff_ID FROM Staff"
        cur.execute(query)
        x2 = cur.fetchone()
        con.commit()

        query = "INSERT INTO Staff_Mobile_Number VALUES ('%d','%d')" % (
            int(x2["Staff_ID"]), phn)
        cur.execute(query)
         
        query = "UPDATE Department SET Num_workers=Num_workers+1 WHERE Department_Name='%s'" % (
            Dept)
        cur.execute(query)

        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to insert into database...")
        print(e)
        print("Try with different data")
        return

    print(green("Data has been successfully added!!"))


# def Add_Raw_Materials(cur, con):

#     #############Taking in the input##############
#     clear()
#     try:
#         print("Enter the details of raw materials: ")
#         branch_id = int(input("Branch ID: "))
#         if not(branch_id > 0 and branch_id < 6):
#             print("You entered a Invalid Branch-ID")
#             return

#         print("Choose Raw Material Type:\n1.Poultry\n 2.Vegetables\n 3.Dairy\n")
#         Source_id = int(input("Choice: "))
#         Date = (input("Date of purchase(dd-mm-yyyy): ")).split('-')
#         Date.append(" ")
#         Date.append(" ")
#         Date.append(" ")
#         Item_Name = input("Item Name: ")
#         Cost = int(input("Cost of the item: "))
#         Qty = float(input("Quantity purchased: "))

#     except Exception as e:
#         print(red("Invalid data is entered"))
#         return

#     ###########Processing the queries###########

#     try:
#         Name = ""
#         my_table = ""
#         if Source_id == 1:
#             Name = "Poultry_"
#             query = "INSERT INTO Poultry VALUES ('%s','%d',%f,'%d','%d','%d','%d')" % (
#                 Item_Name, Cost, Qty, int(Date[0]), int(Date[1]), int(Date[2]), branch_id)
#             cur.execute(query)

#         elif Source_id == 2:
#             Name = "Vegetable_"
#             query = "INSERT INTO Vegetable_Shop VALUES ('%s','%d',%f,'%d','%d','%d','%d')" % (
#                 Item_Name, Cost, Qty, int(Date[0]), int(Date[1]), int(Date[2]), branch_id)
#             cur.execute(query)

#         elif Source_id == 3:
#             Name = "Dairy_"
#             query = "INSERT INTO Dairy VALUES ('%s','%d',%f,'%d','%d','%d','%d')" % (
#                 Item_Name, Cost, Qty, int(Date[0]), int(Date[1]), int(Date[2]), branch_id)
#             cur.execute(query)

#         else:
#             print("Invalid choice")
#             return

#         Name += str(branch_id)
#         add = 0
#         query = "SELECT * FROM Raw_Materials WHERE Source_Name=('%s')" % (Name)
#         cur.execute(query)
#         x1 = cur.fetchone()

#         if(not(bool(x1))):
#             con.rollback()
#             add = 1


#         if(add == 1):
#             query = "INSERT INTO Raw_Materials VALUES ('%d','%d','%s')" % (
#                 branch_id, Source_id, Name)
#             cur.execute(query)

#         con.commit()

#     except Exception as e:
#         con.rollback()
#         print(red("Failed to insert into database..."))
#         print(e)
#         print(red("Try with different data"))
#         return

#     print(green("Data has been successfully added!!"))
