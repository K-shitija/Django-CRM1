import mysql.connector

dataBase = mysql.connector.connect(
    
    host = 'localhost',
    user = 'root',
    passwd = 'password123'
    
    )

 #prepare cursor obj
cursorObject = dataBase.cursor()
 
 #Create databse
 
cursorObject.execute("CREATE DATABASE klderco")
 
print("all done")