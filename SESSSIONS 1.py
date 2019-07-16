# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 18:36:34 2019

@author: 60111
"""

import mysql.connector # the libarry used to connect to the MySQL server
#THE CUSTOMER INFROMATION
HOUSE_NUMBER = '50'
STREET_NAME = 'BANDAR MANJALARA'
CITY = 'KEPONG'
ZIPCODE = '52200'
STATE = 'MELAKA'

#Connecting to the MySQL server create a query
try:
    con = mysql.connector.connect(
            host = "localhost", 
            user = "root",
            password = "",
            database = "Customer_info_db",
            port = 3306
)
    print("hey we are connected")
except:
    print("Hey we are not connected")

#Creating cursor to create query
cur= con.cursor()

#crete query for the databases
#(1) Create table in the database
cur.execute("CREATE TABLE IF NOT EXISTS CUSTOMER_ADDRESS (HOUSE NO VARCHAR(60), STREET NAME VARCHAR(60), CITY VARCHAR(60), STATE VARCHAR(60), ZIPCODE INT)")

#(2)Addinformation into the databases using 
cur.execute(f"INSERT INTO CUSTOMER_ADDRESS VALUES ({HOUSE_NUMBER},[STREET_NAME],{CITY},{ZIPCODE},{STATE})")

#(3)change information such as dtabases name types to 
cur.execute("ALTER TABLE CUSTOMER_ADDRESS ['HOUSE_NUMBER']['APARMENT_NUMBER']")
cur.execute("Alter TABLE CUSTOMER_ADDRESS (STREET NAME VARCHAR(200))")




#commit changes on the databases
con.commit()




