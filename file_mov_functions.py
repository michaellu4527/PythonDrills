import os
import shutil
import time
import datetime
import sqlite3


def createDB():
    conn = sqlite3.connect('file_transfer.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS Transfer")

