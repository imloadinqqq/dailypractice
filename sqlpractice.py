import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

fname = input("What is your first name? ")
lname = input(f"Hi, {fname}! What's your last name? ")
pos = input("Enter your desired position: ")

resetQuery = """
DROP TABLE IF EXISTS employees;
CREATE TABLE employees(
id int PRIMARY KEY AUTO_INCREMENT,
FirstName varchar(255),
LastName varchar(255),
Position varchar(255)
)
"""
migrateTable = """
DROP TABLE IF EXISTS save;
CREATE TABLE save(
    id int PRIMARY KEY AUTO_INCREMENT,
    FirstName varchar(255),
    LastName varchar(255),
    Position varchar(255)
)
"""
insertQuery = "INSERT INTO employees (FirstName, LastName, Position) VALUES (%s, %s, %s)"
copyQuery = "INSERT INTO save SELECT * FROM employees"
selectQuery = "SELECT * FROM employees"

def insertNewEmployee():
    while True:
        fname = input("Enter first name: ")
        lname = input("Enter last name: ")
        pos = input("Enter position: ")

        try:
            connection = mysql.connector.connect(
                user=os.getenv("DB_USER"), 
                password=os.getenv("DB_PASS"),
                host=os.getenv("DB_HOST"), 
                database=os.getenv("DB_NAME")
            )

            if connection.is_connected():
                print("CONNECTED TO DB")
            
            with connection.cursor() as cursor:
                cursor.execute(insertQuery, (fname, lname, pos))
                connection.commit()

                cursor.execute(selectQuery)
                results = cursor.fetchall()
                print("Employees:")
                for row in results:
                    print(row)

        except mysql.connector.Error as err:
            print(f"Error Connecting: {err}")
        finally:
            if connection.is_connected():
                connection.close()
                print("CONNECTION CLOSED")

        response = input("Would you like to insert another employee? (y/n): ").lower()
        if response != 'y':
            print("Exiting employee insertion.")
            break

try:
    # create connection
    connection = mysql.connector.connect(
        user=os.getenv("DB_USER"), 
        password=os.getenv("DB_PASS"),
        host=os.getenv("DB_HOST"), 
        database=os.getenv("DB_NAME")
    )

    if connection.is_connected():
        print("CONNECTED TO DB")

    with connection.cursor() as cursor:
        for statement in resetQuery.split(';'):
            if statement.strip():
                cursor.execute(statement.strip())

        cursor.execute(insertQuery, (fname, lname, pos))
        connection.commit()

        cursor.execute(selectQuery)
        results = cursor.fetchall()
        print("Employees:")
        for row in results:
            print(row)

        for statement in migrateTable.split(';'):
            if statement.strip():
                cursor.execute(statement.strip())

        cursor.execute(copyQuery)
        connection.commit()
        print("DATA SUCCESSFULLY COPIED TO 'save'")

except mysql.connector.Error as err:
    print(f"Error Connecting: {err}")
finally:
    if connection.is_connected():
        connection.close()
        print("CONNECTION CLOSED")

insertNewEmployee()
