import os
import shutil
import time
import datetime
import sqlite3

# Database creation and insertion of values

def createDB():
    conn = sqlite3.connect('file_check.db')
    with conn:
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS Datetime("
                  "check_time REAL"
                  ")")

        conn.commit()
    conn.close()

# Inserts new checked time into the database.

def insertDB():
    conn = sqlite3.connect('file_check.db')
    with conn:
        c = conn.cursor()
        curr_time = datetime.datetime.now()
        print(curr_time)
        c.execute("INSERT INTO Datetime VALUES(?)", (curr_time,))
        conn.commit()
    conn.close()

# This function selects the most recent time that a file has been modified.

def lastCheck():
    conn = sqlite3.connect('file_check.db')
    with conn:
        c = conn.cursor()
        c.execute("SELECT check_time FROM Datetime WHERE ROWID = (SELECT MAX(ROWID) FROM Datetime)") # Selecting the most recent time?
        for row in c.fetchone():
            return (row)
    conn.close()

