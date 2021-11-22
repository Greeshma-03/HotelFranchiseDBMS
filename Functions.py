import pymysql
import pymysql.cursors

from add import *
from Retrievals import *
from Clear import *
from delete import *


def addOptions(cur, con):
    try:
        print("Choose an item to add info!!")
        info = ["Events", "Order", "Menu",
                "Furniture", "Staff"]

        for var in range(len(info)):
            print(var+1, ". ", info[var], sep="")

        val = int(input("Enter your choice: "))

        if(val == 1):
            Add_Events(cur, con)
        elif(val == 2):
            Add_Order(cur, con)
        elif(val == 3):
            Add_Menu(cur, con)
        elif(val == 4):
            Add_Furniture(cur, con)
        elif(val == 5):
            Add_Staff(cur, con)
        # elif(val == 6):
        #     Add_Raw_Materials(cur, con)
        else:
            print("Oops!! You Entered an invalid choice")
            print("Press enter to continue ....")
        return

    except Exception as e:
        print(e)
        print(red("Try again!!"), 'bold')
        return


def Retrievals(cur, con):
    try:
        clear()
        print("Choose a Query type to Search information!!")
        info = ["Select a row specific to some data", "Search by a particular attribute",
                "Get information from entire columns", "Search by text", "Analysis on order"]

        for var in range(len(info)):
            print(var+1, ". ", info[var], sep="")

        val = int(input("Enter your choice: "))
        clear()
        if(val == 1):
            Selection(cur, con)
        elif(val == 2):
            Projection(cur, con)
        elif(val == 3):
            Aggregate(cur, con)
        elif(val == 4):
            Search(cur, con)
        elif(val == 5):
            Analysis(cur, con)
        else:
            print("Oops!! You Entered an invalid choice")
        return

    except Exception as e:
        print(e)
        print(red("Try again!!"), 'bold')
        return


def deleteOptions(cur, con):
    try:
        print("Choose the table from which you like to delete")
        tables_present = ["Events", "Order", "Menu",
                          "Furniture", "Staff", "Raw_Materials"]
        count = 0
        for i in tables_present:
            count = count + 1
            print(str(count) + '.' + i)

        j = int(input("Enter your choice: "))

        if(j == 1):
            delete_event(cur, con)
        elif(j == 2):
            delete_order(cur, con)
        elif(j == 3):
            delete_MenuItem(cur, con)
        elif(j == 4):
            delete_Furniture(cur, con)
        elif(j == 5):
            delete_Staff(cur, con)
        elif(j == 6):
            delete_RawMaterials(cur, con)
        else:
            print("please select a valid choice")

    except Exception as e:
        print(e)
        print(red("Try again!!"), 'bold')
        return
