import mysql.connector  # importing the sql
from mysql.connector import Error  # importing the error


def database_connection():
    try:
        checker = mysql.connector.connect(
            database="progenFC",
            user="progenFC",
            host="localhost",
            password="Group5",
        )
        if checker.is_connected():
            print("Database Connection Successful")
            return checker
    except Error as error:
        print(f"Error is {error}")


database_connection()
