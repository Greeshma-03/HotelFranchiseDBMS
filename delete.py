from datetime import datetime

import subprocess as sp
import pymysql
import pymysql.cursors
from colorama import Fore, Style

from colorama import Fore, Style
from simple_colors import *
from tabulate import tabulate
from Clear import *

from datetime import datetime

def delete_event(cur, con):
    try:
        event = {}
        print("Enter the details of the event you want to delete")
        event['branch'] = int(input("Branch id:"))
        print("Enter Address details of the event")
        event['pin'] = int(input("Pin_Code:"))
        event['Street'] = int(input("Street Number:"))
        event['Colony'] = input("Colony Name:")
        event['Door'] = int(input("Door Number:"))
        if not(event['branch'] > 0 and event['branch'] < 6):
            print("You entered a Invalid Branch-ID")
            return
        del_query = "DELETE FROM Events WHERE Branch_ID = %d AND Pin_Code = %d AND Street_Number = %d AND Colony_Name = '%s' AND Door_No = %d ;" %(event['branch'],event['pin'],event['Street'],event['Colony'], event['Door'])
        cur.execute(del_query)
        con.commit()
        print("Event Deleted")

    except Exception as e:
        con.rollback()
        print("Failed to delete event")
        print(red("Invalid data!!",'bold'))
    return

def delete_Staff(cur,con):
    try:
        print("Enter the Staff_ID of the Staff you would like to delete")
        id = int(input("Staff ID: "))
        del_query = "DELETE FROM Staff WHERE Staff_ID = %d;" %(id)
        
        select_query = "SELECT Department_Name FROM Staff WHERE Staff_ID = %d;" %(id)
        cur.execute(select_query)
        con.commit()
        outp = cur.fetchall()

        cur.execute(del_query)
        con.commit()
        
        workers_query = "SELECT Num_Workers FROM Department WHERE Department_Name = '%s';" %(outp[0]['Department_Name'])
        cur.execute(workers_query)
        con.commit()
        num_workers = cur.fetchall()
        
        update_query = "UPDATE Department SET Num_Workers = %d WHERE Department_Name = '%s';" %(int(num_workers[0]['Num_Workers']) - 1 ,outp[0]['Department_Name'])
        cur.execute(update_query)
        con.commit()

        print("Person with Staff_ID",id,"deleted")
    except Exception as e:
        con.rollback()
        print("Failed to delete person with staff id", id)
        print(red("Invalid data!!",'bold'))

def delete_order(cur, con):
    try:
        print("Enter the following details of the order you like to delete")
        ID = int(input("Customer_ID of the Customer who ordered:"))
        Fid = int(input("Food Item ID:"))
        
        del_query = "DELETE FROM _Order WHERE Customer_ID = %d AND Food_Item_ID = %d;" %(ID,Fid)
        cur.execute(del_query)
        con.commit()

        print("Deleted Order")
    except Exception as e:
        con.rollback()
        print("Failed to delete Order")
        print(red("Invalid data!!",'bold'))

def delete_MenuItem(cur,con):
    try:
        name = input("Enter Name of the food Item you like to delete: ")
        select_query = "SELECT Food_Item_ID FROM Menu WHERE Food_Item = '%s';" %(name)
        cur.execute(select_query)
        con.commit()
        outp = cur.fetchall()
        id = int(outp[0]['Food_Item_ID'])
        del_query = "DELETE FROM Menu WHERE Food_Item_ID = %d;" %(id)
        cur.execute(del_query)
        con.commit()

        print("Item Deleted")
    except Exception as e:
        con.rollback()
        print("Failed to delete Menu Item")
        print(red("Invalid data!!",'bold'))

def delete_Furniture(cur,con):
    try:
        print("Enter the following details of Furniture you like to delete")
        id = int(input("Branch ID: "))
        if not(id > 0 and id < 6):
            print("You entered a Invalid Branch-ID")
            return
        Name = input("Name of the Furniture: ")
        del_query = "DELETE FROM Furniture WHERE Branch_ID = %d AND Furniture_Name = '%s';" %(id, Name)
        cur.execute(del_query)
        con.commit()

        print("Furniture item Deleted")
    except Exception as e:
        con.rollback()
        print("Failed to delete Furniture item")
        print(red("Invalid data!!",'bold'))

def delete_RawMaterials(cur, con):
    try: 
        print("Enter the details of raw materials you like to delete")
        branch_id = int(input("Branch ID: "))
        
        if not(branch_id > 0 and branch_id < 6):
            print("You entered a Invalid Branch-ID")
            return

        print("Choose Raw Material Type:\n1. Poultry\n2. Vegetables\n3. Dairy\n")
        Source_id = int(input("Choice: "))
        name = "Poultry"

        if(Source_id == 2):
            name = "Vegetables"
        elif(Source_id == 3):
            name = "Dairy"

        Today_date = datetime.now().strftime('%Y-%m-%d')
        Year, Month, Day = Today_date.split('-')

        del_query = "DELETE FROM %s WHERE (%d - Year_date = 1 AND %d - Month_date = 1 AND %d - Day_date <= 0 AND Branch_ID = %d) OR  (%d - Year_date = 0 AND %d - Month_date = 0 AND %d - Day_date >= 0 AND Branch_ID = %d) OR (%d - Year_date = 0 AND %d - Month_date = 1 AND %d - Day_date <= 0 AND Branch_ID = %d);" %(name, int(Year), int(Month), int(Day),branch_id,int(Year), int(Month), int(Day),branch_id ,int(Year), int(Month), int(Day), branch_id)
        cur.execute(del_query)
        con.commit()
        print("Last one month data from",name,"from brach with branch_ID",branch_id,"is deleted")
    except Exception as e:
        con.rollback()
        print("Failed to delete the data")
        print(red("Invalid data!!",'bold'))
