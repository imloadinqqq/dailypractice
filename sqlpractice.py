import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

# user input
fname = input("What is your first name? ")
lname = input(f"Hi, {fname}! What's your last name? ")
pos = input("Enter your desired position: ")

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

    # queries
    resetQuery = """
    DROP TABLE IF EXISTS employees;
    CREATE TABLE employees(
        id int PRIMARY KEY,
        FirstName varchar(255),
        LastName varchar(255),
        Position varchar(255)
    )
    """
    migrateTable = """
    DROP TABLE IF EXISTS save;
    CREATE TABLE save(
        id int PRIMARY KEY,
        FirstName varchar(255),
        LastName varchar(255),
        Position varchar(255)
    )
    """
    insertQuery = "INSERT INTO employees (id, FirstName, LastName, Position) VALUES (%s, %s, %s, %s)"
    copyQuery = "INSERT INTO save SELECT * FROM employees"
    selectQuery = "SELECT * FROM save"

    # cursor executions
    with connection.cursor() as cursor:
        for statement in resetQuery.split(';'):
            if statement.strip():
                cursor.execute(statement.strip())

        cursor.execute(insertQuery, (1, fname, lname, pos))

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
    # close connection
finally:
    if connection.is_connected():
        connection.close()
        print("CONNECTION CLOSED")
