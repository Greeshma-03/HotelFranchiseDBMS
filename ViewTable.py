import subprocess as sp
import pymysql
import pymysql.cursors
import sys
from colorama import Fore, Style
from simple_colors import *
from tabulate import tabulate
from os import system, name


#***************************************** Printing table to screen *********************************************************

def viewTable(rows):

    a = []
    try:
        a.append(list(rows[0].keys()))
    except:
        print("\n-----------------\nEMPTY TABLE\n-----------------\n")   
        return
    for row in rows:
        b = []
        for k in row.keys():
            b.append(row[k])
        a.append(b)
    print(tabulate(a, tablefmt="psql", headers="firstrow"))
    print()
    return