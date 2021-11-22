import subprocess as sp
import pymysql
import pymysql.cursors
import sys

from Clear import *

from colorama import Fore, Style
from simple_colors import *
from tabulate import tabulate
from os import system, name
from time import sleep
# from global_ import con, cur

# ******************************************** Update options implemented ****************************************************


def Update(cur, con):
    try:
        clear()

        print(
            magenta("------------- Select one from below to update-------------\n", 'bold'))
        print(yellow("--> 1.  Employee Salary"))
        print(yellow("--> 2.  Employee Shift"))
        print(yellow("--> 3.  Menu items price"))
        print(yellow("--> 4.  Event address"))
        print(yellow("--> 5.  Discount amount of items"))
        print(yellow("--> 6.  Minimum cost to offer discount"))
        print(yellow("--> 7.  Furniture quantity"))
        print(yellow("--> 8.  Raw material quantity\n"))

        updateOption = input(magenta("Your choice(1 - 8) ? ", 'bold'))

        clear()

        if updateOption == '1':     # Employee salary
            ID = int(input("Enter Staff ID: "))
            validQuery = "SELECT * FROM Staff WHERE Staff_ID = %d;" % (ID)

            cur = con.cursor()
            cur.execute(validQuery)
            data = cur.fetchall()

            # ****************** Error handling ***************************
            if not data:
                print(red("Error: Staff ID = %d NOT FOUND !!" % (ID), 'bold'))
                print(red("... TRY AGAIN WITH NEW DATA"))
                return
            else:
                salary = int(input("Enter new amount of salary: "))
                query = "UPDATE Staff SET Salary = %d WHERE Staff_ID = %d" % (
                    salary, ID)

        elif updateOption == '2':     # Employee shift
            ID = int(input("Enter Staff ID: "))
            validQuery = "SELECT * FROM Staff WHERE Staff_ID = %d;" % (ID)

            cur = con.cursor()
            cur.execute(validQuery)
            data = cur.fetchall()

            # ****************** Error handling ***************************
            if not data:
                print(red("Error: Staff ID = %d NOT FOUND !!" % (ID), 'bold'))
                print(red("... TRY AGAIN WITH NEW DATA"))
                return
            else:
                shift = input("Enter new shift of employee: ")
                query = "UPDATE Staff SET Shift = '%s' WHERE Staff_ID = %d" % (
                    shift, ID)

        elif updateOption == '3':     # Menu items price
            ID = int(input("Enter Food item ID: "))
            validQuery = "SELECT * FROM Menu WHERE Food_Item_ID = %d;" % (ID)

            cur = con.cursor()
            cur.execute(validQuery)
            data = cur.fetchall()

            # ****************** Error handling ***************************
            if not data:
                print(red("Error: Food Item ID = %d NOT FOUND !!" % (ID), 'bold'))
                print(red("... TRY AGAIN WITH NEW DATA"))
                return
            else:
                price = int(
                    input("Enter new price of food item with ID = %d" % (ID)))
                query = "UPDATE Menu SET Item_Cost = %d WHERE Food_Item_ID = %d;" % (
                    price, ID)

        elif updateOption == '4':     # Event address
            ID01 = int(input("Enter ID of branch hosting the event: "))
            ID02 = int(input("Enter present pincode of event address: "))
            street = int(
                input("Enter present street number of event address: "))
            colonyName = input("Enter present colony name of event address: ")
            D_no = int(input("Enter present door number of event address: "))
            validQuery01 = "SELECT * FROM Events WHERE  Branch_ID = %d AND Pin_Code = %d AND Street_No = %d AND Colony_Name = '%s' AND Door_No = %d;" % (
                ID01, ID02, street, colonyName, D_no)

            cur = con.cursor()
            cur.execute(validQuery01)
            data = cur.fetchall()

            # ****************** Error handling ***************************
            if not data:
                print(red("Error: DATA NOT FOUND !!", 'bold'))
                print(red("... TRY AGAIN WITH NEW DATA"))
                return
            else:
                clear()

                # ************************ Further options to update ********************************************
                print(blue("What do you want to update? ", 'bold'))
                print(yellow("1. Change the branch"))
                print(yellow("2. Change address"))
                print(yellow("3. Change both branch and address\n"))

                eventOpt = input("Your choice(1-3): ")

                if eventOpt == '2':         # Change address
                    newPin = int(input("Enter new pincode of event address: "))
                    newStreet = int(
                        input("Enter new street number of event address: "))
                    newColony = input(
                        "Enter new colony name of event address: ")
                    newDoor = int(input("Enter new door number: "))
                    query = "UPDATE Events SET Pin_Code = %d, Street_No = %d, Colony_Name = '%s', Door_No = %d WHERE Branch_ID = %d AND Pin_Code = %d AND Street_No = %d AND Colony_Name = '%s' AND Door_No = %d;" % (
                        newPin, newStreet, newColony, newDoor, ID01, ID02, street, colonyName, D_no
                    )
                elif eventOpt == '1':       # Change branch
                    newBranch = int(input("Enter new branch ID:"))
                    validQuery02 = "SELECT * FROM Hotel WHERE Branch_ID = %d;" % (
                        newBranch)

                    cur = con.cursor()
                    cur.execute(validQuery02)
                    data = cur.fetchall()

                    # ****************** Error handling ***************************
                    if not data:
                        print(
                            red("Error: No branch EXISTS with branch ID = %d !!" % (newBranch), 'bold'))
                        print(red("... TRY AGAIN WITH NEW DATA"))
                        return
                    else:
                        query = "UPDATE Events SET Branch_ID = %d WHERE Branch_ID = %d AND Pin_Code = %d AND Street_No = %d AND Colony_Name = '%s' AND Door_No = %d;" % (
                            newBranch, ID01, ID02, street, colonyName, D_no
                        )
                elif eventOpt == '3':       # Change both
                    newBranch = int(input("Enter new branch ID:"))
                    validQuery02 = "SELECT * FROM Hotel WHERE Branch_ID = %d;" % (
                        newBranch)

                    cur = con.cursor()
                    cur.execute(validQuery02)
                    data = cur.fetchall()

                    # ****************** Error handling ***************************
                    if not data:
                        print(
                            red("Error: No branch EXISTS with branch ID = %d !!" % (newBranch), 'bold'))
                        print(red("... TRY AGAIN WITH NEW DATA"))
                        return
                    else:
                        newPin = int(
                            input("Enter new pincode of event address: "))
                        newStreet = int(
                            input("Enter new street number of event address: "))
                        newColony = input(
                            "Enter new colony name of event address: ")
                        newDoor = int(input("Enter new door number: "))
                        query = "UPDATE Events SET Branch_ID = %d, Pin_Code = %d, Street_No = %d, Colony_Name = '%s', Door_No = %d WHERE Branch_ID = %d AND Pin_Code = %d AND Street_No = %d AND Colony_Name = '%s' AND Door_No = %d;" % (
                            newBranch, newPin, newStreet, newColony, newDoor, ID01, ID02, street, colonyName, D_no
                        )

        elif updateOption == '5':       # Discount amount of items
            ID = int(input("Enter food item ID: "))
            validQuery = "SELECT * FROM Discount WHERE Food_Item_ID = %d;" % (
                ID)

            cur = con.cursor()
            cur.execute(validQuery)
            data = cur.fetchall()

            # ****************** Error handling ***************************
            if not data:
                print(red("Error: Food Item ID = %d is not applicable for any discount !!" % (
                    ID), 'bold'))
                print(red("... TRY AGAIN WITH NEW DATA"))
                return
            else:
                disc = int(
                    input("Enter new discount for food item with ID = %d" % (ID)))
                query = "UPDATE Discount SET Discount_Amount = %d WHERE Food_Item_ID = %d;" % (
                    disc, ID)

        elif updateOption == '6':       # Minimum cost to offer discount
            ID = int(input("Enter food item ID: "))
            validQuery = "SELECT * FROM Discount WHERE Food_Item_ID = %d;" % (
                ID)

            cur = con.cursor()
            cur.execute(validQuery)
            data = cur.fetchall()

            # ****************** Error handling ***************************
            if not data:
                print(red("Error: Food Item ID = %d is not applicable for any discount !!" % (
                    ID), 'bold'))
                print(red("... TRY AGAIN WITH NEW DATA"))
                return
            else:
                minCost = int(
                    input("Enter new minimum cost for food item with ID = %d" % (ID)))
                query = "UPDATE Discount SET Min_Cost = %d WHERE Food_Item_ID = %d;" % (
                    minCost, ID)

        elif updateOption == '7':       # Furniture quantity
            branch = int(input("Enter branch ID: "))
            validQuery = "SELECT * FROM Hotel WHERE Branch_ID = %d;" % (branch)

            cur = con.cursor()
            cur.execute(validQuery)
            data = cur.fetchall()

            # ****************** Error handling ***************************
            if not data:
                print(red("Error: No branch EXISTS with branch ID = %d !!" %
                      (branch), 'bold'))
                print(red("... TRY AGAIN WITH NEW DATA"))
                return
            else:
                clear()

                # ***************************** Further options to choose **********************************
                print(blue("Which furniture quantity do you want to update? ", 'bold'))
                print(yellow("1. Table"))
                print(yellow("2. Chair"))
                print(yellow("3. Desk"))
                print(yellow("4. Cushion"))
                print(yellow("5. Stool\n"))

                furnitureOpt = input(magenta("Your choice(1-5)?"))

                if furnitureOpt == '1':
                    quant = int(input("Number of tables: "))
                    query = "UPDATE Furniture SET Quantity = %d WHERE Branch_ID = %d AND Furniture_Name = 'Table';" % (
                        quant, branch)
                if furnitureOpt == '2':
                    quant = int(input("Number of Chairs: "))
                    query = "UPDATE Furniture SET Quantity = %d WHERE Branch_ID = %d AND Furniture_Name = 'Chair';" % (
                        quant, branch)
                if furnitureOpt == '3':
                    quant = int(input("Number of Desks: "))
                    query = "UPDATE Furniture SET Quantity = %d WHERE Branch_ID = %d AND Furniture_Name = 'Desk';" % (
                        quant, branch)
                if furnitureOpt == '4':
                    quant = int(input("Number of Cushions: "))
                    query = "UPDATE Furniture SET Quantity = %d WHERE Branch_ID = %d AND Furniture_Name = 'Cushion';" % (
                        quant, branch)
                if furnitureOpt == "5":
                    quant = int(input("Number of Stools: "))
                    query = "UPDATE Furniture SET Quantity = %d WHERE Branch_ID = %d AND Furniture_Name = 'Stool';" % (
                        quant, branch)

        elif updateOption == '8':       # Raw material quantity

            branch = int(input("Enter branch ID: "))
            validQuery = "SELECT * FROM Raw_Materials WHERE Branch_ID = %d;" % (
                branch)

            cur = con.cursor()
            cur.execute(validQuery)
            data = cur.fetchall()

            # ****************** Error handling ***************************
            if not data:
                print(red("Error: No branch EXISTS with branch ID = %d !!" %
                      (branch), 'bold'))
                print(red("... TRY AGAIN WITH NEW DATA"))
                return
            else:

                # *************************** Further options to update **********************************
                print(blue("--> Choose source from below ", 'bold'))
                print(yellow("'1' for Poultry"))
                print(yellow("'2' for Vegetable shop"))
                print(yellow("'3' for Dairy"))

                source = input(magenta("Your choice(1-3)? "))
                if source == '1':
                    productName = input(
                        "Which product do you want to update? ")
                    qaunt = int(
                        input("Quantity of '%s' to be ordered: " % (productName)))

                    validQuery = "SELECT * FROM Poultry WHERE Branch_ID = %d AND Non_veg_Item = '%s';" % (
                        branch, productName)

                    cur = con.cursor()
                    cur.execute(validQuery)
                    data = cur.fetchall()

                    # ****************** Error handling ***************************
                    if not data:
                        print(
                            red("Error: Your mentioned product is not in the purchase list !!", 'bold'))
                        print(red("... TRY AGAIN WITH NEW DATA"))
                        return
                    else:
                        query = "UPDATE Poultry SET Quantity = %d WHERE Branch_ID = %d AND Non_veg_Item = '%s';" % (
                            branch, productName)

                elif source == '2':
                    productName = input(
                        "Which product do you want to update? ")
                    qaunt = int(
                        input("Quantity of %s to be ordered: " % (productName)))

                    validQuery = "SELECT * FROM Vegetable_Shop WHERE Branch_ID = %d AND Vegetable_Name = '%s';" % (
                        branch, productName)

                    cur = con.cursor()
                    cur.execute(validQuery)
                    data = cur.fetchall()

                    # ****************** Error handling ***************************
                    if not data:
                        print(
                            red("Error: Your mentioned product is not in the purchase list !!", 'bold'))
                        print(red("... TRY AGAIN WITH NEW DATA"))
                        return
                    else:
                        query = "UPDATE Vegetable_Shop SET Quantity = %d WHERE Branch_ID = %d AND Vegetable_Name = '%s';" % (
                            branch, productName)

                elif source == '3':
                    productName = input(
                        "Which product do you want to update? ")
                    qaunt = int(
                        input("Quantity of '%s' to be ordered: " % (productName)))

                    validQuery = "SELECT * FROM Dairy WHERE Branch_ID = %d AND Dairy_Item = '%s';" % (
                        branch, productName)

                    cur = con.cursor()
                    cur.execute(validQuery)
                    data = cur.fetchall()

                    # ****************** Error handling ***************************
                    if not data:
                        print(
                            red("Error: Your mentioned product is not in the purchase list !!", 'bold'))
                        print(red("... TRY AGAIN WITH NEW DATA"))
                        return
                    else:
                        query = "UPDATE Dairy SET Quantity = %d WHERE Branch_ID = %d AND Dairy_Item = '%s';" % (
                            branch, productName)

        try:
            no_of_rows = cur.execute(query)
            con.commit()
        except Exception as e:
            print(e)
            print(red("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n", 'bold'))
            return

    except Exception as e:
        print(red("Invalid data"))
        return

    print(green("Data updated succesfully :)", 'bold'))
