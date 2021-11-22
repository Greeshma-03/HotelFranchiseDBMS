# DBMS project- Hotel Franchise
Data and application project

By TEAM
* Kurukunda Bhargavi
* Pamulapati Pallavi
* Greeshma Amaraneni

## What is this project about ?
We have implemented a database for a Hotel Franchise containing a total of five hotels and are dealing with the data related to this Franchise. To get a better overview of our Database have look at the **ER diagram, Relational model diagram and the Requirements PDF** all the three uploaded above.

## How to run ?
* Open your terminal and run `mysql -u 'username' -p`
* Your terminal will prompt you to enter the password. Enter the password you set for the mysql server.
* After entering correct credentials you will be able to access your **mysql Terminal**.
* Download the code in this repository to initiate the database.
* Now if run `source <path_to_.sql_file>` your database named **Franchise** will be created.
* You can check by running `SHOW DATABASES;` in your mysql terminal. You will find **Franchise** in your databases table.
* Once the initialization is done, come out of your mysql terminal and get into the folder containing the files of this repository.
* Run `python3 main.py` on your terminal.

## What are the functionalities implemented ?
Below are the implemented functionalities:
* Display or view
* Add or Insert
* Modify or Update
* Delete
* Search 
* Financial Analysis

## How good is the user interface ?
Once we have run `python3 main.py` on our terminal our program will prompt you to enter your database credentials i.e., Username and password. If the credentials entered are invalid, then our program will throw an ERROR message and allows you to try again.

Once it has been given the correct credentials it will display the above the functionalities implemented and requests user to choose one of the functionalities to get the needed information.

They will further display new options for the user so as to make our database interface user friendly.

For every invalid input(No data or out of constraints data) it will show an ERROR or WARNING which is dealt by the error handling functions used in every case.

******************************************************************************************************************
> There is a vedio uploaded showing how to run and use our databasae. Do watch it do get a better idea :)
### Try running our DATABASE and hope you enjoy playing with it. 

###                                             Thank You :)
