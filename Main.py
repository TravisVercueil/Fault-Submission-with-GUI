import tkinter.messagebox
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import datetime
import sqlite3
 #Import the SQLite3 package and connect our database and cursor
con = sqlite3.connect('travis.db')
mycursor = con.cursor()
#creating the sql query that is used to create the database
table_query = "CREATE TABLE IF NOT EXISTS `fault_data`(`ID` INTEGER PRIMARY KEY AUTOINCREMENT,`FName` TEXT,`LName` TEXT,`Contact` TEXT,`Gender` ,`Report_Date` TEXT,`Unit` TEXT,`Apartment` TEXT,`Fault` TEXT);"
#Executing the SQL query
mycursor.execute(table_query)
con.commit()


root = tk.Tk()
root.title("Fault Management")
root.geometry("600x400")
root.configure(background="grey")

#first name label and getting text
first_name = Label(text= "First Name: ", font=12, bg="grey")
first_name.grid(row=0, column=0)
first_name_txt = Text(root, height=1, width=50)
first_name_txt.grid(row=0, column=1)

#last name label and getting text

last_name = Label(text="Last Name: ", font=12, bg="grey")
last_name.grid(row=1, column=0)
last_name_txt = Text(root, height=1, width=50)
last_name_txt.grid(row=1, column=1)

#contact nr label and getting text

contact_number = Label(text="Contact: ", font=12, bg="grey")
contact_number.grid(row=2, column=0)
contact_number_txt = Text(root, height=1, width=50)
contact_number_txt.grid(row=2, column=1)

#apartment label and getting text

apartment_name = Label(text="Apartment: ", font=12, bg="grey")
apartment_name.grid(row=3, column=0)
apartment_name_txt = Text(root, height=1, width=50)
apartment_name_txt.grid(row=3, column=1)

#Report date label and getting text

date_of_reporting = Label(text="Report_Date: ", font=12, bg="grey")
date_of_reporting.grid(row=4, column=0)
date_of_reporting_txt = Text(root, height=1, width=50)
date_of_reporting_txt.grid(row=4, column=1)

#unit nr label and getting text

unit_number = Label(text="Unit: ", font=12, bg="grey")
unit_number.grid(row=5, column=0)
unit_number_txt = Text(root, height=1, width=50)
unit_number_txt.grid(row=5, column=1)

#gender radiobutton and getting gender

genderlbl = Label(text="Gender:", font=12, bg="grey")
genderlbl.grid(row=6, column=0)
genderm = Radiobutton(root, text="Male", value=1).place(x=175, y=143)
genderf = Radiobutton(root, text="Female", value=0).place(x=350, y=143)

if genderm == 0:
    gender = "male"
if genderm == 1:
    gender = "female"

#fault label and getting text

fault = Label(text="Fault: ", font=12, bg="grey")
fault.grid(row=7, column=0)
fault_txt = Text(root, height=5, width=40)
fault_txt.grid(row=7, column=1)

#Submit button class
class Submit_Btn():
    root = tk.Tk()
    root.title("Add Faults")
    root.geometry("250x150")

    #Label Output that displays lightbulb and text
    lightbulb = Label(root, text="💡", font=12)
    lightbulb.grid(row=1, column=0)
    #Displaying Label message
    fault_sub_message = Label(root, text="Your fault has been submitted." , bg="Grey", font=50)
    fault_sub_message.grid(row=1, column=1)
    fault_sub = Label(root, text="                                                   " , bg = "Grey", font=50)
    fault_sub.grid(row=2,column=1)

    #ok button to close program
    ok_button = Button(root, text="OK", pady=15, padx=20)
    ok_button.place(x=100, y=75)

    # we tell the program that we are using the global variables for mycuror and con and not creating our own local ones
    global mycursor
    global con
    global first_name_txt, last_name_txt, contact_number_txt, gender, date_of_reporting_txt, unit_number_txt,apartment_name_txt,fault_txt
    # create our query and get our arguments that will go into the query
    query = "INSERT INTO `fault_data`(Fname,LName,Contact,Gender,Report_Date,Unit,Apartment,Fault)VALUES(?,?,?,?,?,?,?,?)"
    args = (first_name_txt, last_name_txt, contact_number_txt, gender, date_of_reporting_txt, unit_number_txt,apartment_name_txt,fault_txt)
    # Execute the query with the arguments
    mycursor.execute(query, args)
    con.commit()

    print("Fault Added Successfully \n")
    root.mainloop()


#fault class to get data from database
class fault_btn():
    global mycursor
    global con

    mycursor.execute("SELECT * FROM fault_data")
    #fetching all results
    myresult = mycursor.fetchall()
    #printing results
    for x in myresult:
        print(x)

#fault list and submit button

list_fault = Button(root, text="List Fault")
list_fault.place(x=175, y=275)

submitbtn = Button(root, text="Submit Now", command=Submit_Btn)
submitbtn.place(x=350, y=275)

root.mainloop()