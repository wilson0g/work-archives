# Progen FC Sports Club Management System

Progen FC is a sports club management system developed to manage the operations and data of a sports club.

## Features

- Athlete management
- Coach management
- Team management
- Membership management
- Facility management
- Facility bookings
- Competitions and matches
- Training sessions
- Transactions
- Player statistics

## Technologies Used

- Python
- Tkinter
- MariaDB / MySQL
- MySQL Connector for Python

## Database Setup

1. Install MariaDB or MySQL.
2. Import the `progenFC.sql` file into the database.
3. Create a database user with the following credentials:

   - Username: `progenFC`
   - Password: `Group5`

4. Ensure the database is named `progenFC`.

## Running the Application

Install the MySQL connector if necessary:

`pip install mysql-connector-python`

Then run:

`progenFCmain.py`

## Project Structure

The `ProgenFC_modules` folder contains the different modules used to manage athletes, coaches, teams, facilities, bookings, competitions, matches, memberships, transactions, and statistics.

## Purpose

This project was developed as a database management system project to demonstrate the use of Python with a relational database.