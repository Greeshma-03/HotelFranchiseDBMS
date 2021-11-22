import subprocess as sp
import pymysql
import pymysql.cursors
import sys

from colorama import Fore, Style
from simple_colors import *
from tabulate import tabulate
from os import system, name
from time import sleep

from Update import *
from Clear import *
from Functions import *
from add import *
from Display import *
from delete import *
from ViewTable import *
from Retrievals import *
from Finance import *


# *************** Declaring global variables ********************

# global username
# global password
# global con
# global cur

#******************************************** Program starts here ************************************************************

while(1):
    tmp = sp.call('clear', shell=True)
    username = input(green("Username: ", 'bold'))
    password = input(green("Password: ", 'bold'))

    try:
        con = pymysql.connect(host='localhost',
                              user=username,
                              password=password,
                              db='Franchise',
                              cursorclass=pymysql.cursors.DictCursor)
    except Exception as e:
        print(e)
        tmp = sp.call('clear', shell=True)
        print(red('Connection Failed:', 'bold'))
        print(Fore.RED + "Credentials entered are incorrect or user doesn't have access to database")
        tmp = input(Fore.GREEN + "Enter any key to CONTINUE > ")
        print(Style.RESET_ALL)
        continue

    with con:
        cur = con.cursor()
        exitflag = 0
        while(1):
            tmp = sp.call('clear', shell=True)
            
            print(blue("----------- CHOOSE AN OPTION -----------\n", 'bold'))
            print(yellow("\t--> 1.  Display Options", 'bold'))
            print(yellow("\t--> 2.  Addition Options", 'bold'))
            print(yellow("\t--> 3.  Deletion Options", 'bold'))
            print(yellow("\t--> 4.  Modify/Update Options", 'bold'))
            print(yellow("\t--> 5.  Search Options", 'bold'))
            print(yellow("\t--> 6.  Finance Analysis Options", 'bold'))
            print(yellow("\t--> 7.  Quit", 'bold'))
            
            inp = input(cyan("\nCHOICE ? ", 'bold'))
            
            if(inp == '1'):
                Display(cur,con)
            elif(inp == '2'):
                addOptions(cur,con)
            elif(inp == '3'):
                deleteOptions(cur,con)
            elif(inp == '4'):
                Update(cur,con)
            elif(inp=='5'):
                Retrievals(cur,con)
            elif(inp=='6'):
                Finance(cur,con)
            elif(inp == '7'):
                    exitflag = 1
                    print(blue("\n\nThanks for Coming!!\nSee you again\n",'bold'))
                    break
            
            print(blue("Press enter to continue ... "))
            x=input()

    if exitflag == 1:
        break
