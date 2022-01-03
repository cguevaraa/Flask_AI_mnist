import os 
from dotenv import load_dotenv
from pathlib import Path
import mysql.connector as mariadb

# Connect to DBMS MariaDB
def db_connect():
    # Manually provide the path to .env
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)

    # Load the credentials
    db_usr = os.getenv('DB_USR')
    db_pwd = os.getenv('DB_PWD')

    db = mariadb.connect(host='localhost', user=db_usr, password=db_pwd)

    return db

# Get all users in DB
def get_users(table='users'):
    db = db_connect()
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS p5flask")
    cursor.execute("USE p5flask")
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id int NOT NULL PRIMARY KEY AUTO_INCREMENT, firstname VARCHAR(255) NOT NULL, lastname VARCHAR(255) NOT NULL, nickname VARCHAR(255) NOT NULL, gender VARCHAR(255) NOT NULL)")
    cursor.execute(f"SELECT * FROM {table}")
    users = cursor.fetchall()
    cursor.close()
    db.close()
    return users

# Check if nickname already exists in DB
def exists(nickname, cursor, table='users'):
    cursor.execute("CREATE DATABASE IF NOT EXISTS p5flask")
    cursor.execute("USE p5flask")
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id int NOT NULL PRIMARY KEY AUTO_INCREMENT, firstname VARCHAR(255) NOT NULL, lastname VARCHAR(255) NOT NULL, nickname VARCHAR(255) NOT NULL, gender VARCHAR(255) NOT NULL)")
    cursor.execute(f"SELECT nickname FROM {table}")
    nicknames = cursor.fetchall() # Store all nicknames in DB
    for entry in nicknames:
        if entry[0] == nickname:
            return True
    return False

# Create new entry in table users
def db_create_user(firstname, lastname, nickname, gender, table='users'):
    db = db_connect()
    cursor = db.cursor()

    if exists(nickname, cursor)==True: # Check if nickname exists in DB
        print('**** NICKNAME ALREADY EXISTS ****')
        cursor.close()
        db.close()
        return 'The provided nickname already exists'
    else:
        cursor.execute("CREATE DATABASE IF NOT EXISTS p5flask")
        cursor.execute("USE p5flask")
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id int NOT NULL PRIMARY KEY AUTO_INCREMENT, firstname VARCHAR(255) NOT NULL, lastname VARCHAR(255) NOT NULL, nickname VARCHAR(255) NOT NULL, gender VARCHAR(255) NOT NULL)")
        cursor.execute(f"INSERT INTO {table} (firstname, lastname, nickname, gender) VALUES ('{firstname}', '{lastname}', '{nickname}', '{gender}')")
        db.commit()
        cursor.close()
        db.close()
        return 'SUCCESS'


