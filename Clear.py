import subprocess as sp
import pymysql
import pymysql.cursors
import sys
from colorama import Fore, Style
from simple_colors import *
from tabulate import tabulate
from os import system, name
from time import sleep


#***************************************** Clear screen option implemented **************************************************

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')