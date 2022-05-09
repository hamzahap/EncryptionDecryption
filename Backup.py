import pymysql
import pymysql.cursors
import pandas as pd
from datetime import date
from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

load_dotenv()

def main(): 
    #Make Directories if they don't exist
    os.makedirs('Backups', exist_ok=True)
    os.makedirs('Keys', exist_ok=True)
    today = date.today()
    datetoday = today.strftime("%b-%d-%Y")
    #Make connection to database
    connection = pymysql.connect(host= os.getenv('HOST'),
                            user= os.getenv('USER'),
                            password= os.getenv('PASS'),
                            database= os.getenv('DB_NAME'),
                            cursorclass=pymysql.cursors.DictCursor)
    #Retrieve all the tables in Dictionary format
    with connection:
        result1 = sql_select(connection, os.getenv('TB_NAME'))
        result2 = sql_select(connection, os.getenv('ANOTHER_TB_NAME'))
    #Convert to pandas dataframe and save to csv
    #Retrieve file name for further operations
    table1 = make_backup(result1, datetoday, os.getenv('TB_NAME'))
    table2 = make_backup(result2, datetoday, os.getenv('ANOTHER_TB_NAME'))
    #Make key for today's date (When the script is ran)
    write_key(datetoday)
    key = load_key(datetoday)
    #Encrypt the tables with the keys if you want
    #encrypt(table1, key)
    #encrypt(table2, key)

    
    
def sql_select(connection, tablename):
    #Retrieve data from table in database
    with connection.cursor() as cursor:
        sql = "SELECT * FROM {}".format(tablename)
        cursor.execute(sql)
        result = cursor.fetchall()

    return result

def make_backup(result, datetoday, filename):
    #Create Backups for each table
    df = pd.DataFrame.from_dict(result)
    df.to_csv('Backups/{}-{}.csv'.format(filename, datetoday))
    print("{} csv file for {} created".format(filename, datetoday))
    return 'Backups/{}-{}.csv'.format(filename, datetoday)

def write_key(datetoday):
    #Generate key
    key = Fernet.generate_key()
    with open("Keys/key-{}.key".format(datetoday), "wb") as key_file:
        key_file.write(key)

def load_key(datetoday):
    #Load key
    return open("Keys/key-{}.key".format(datetoday), "rb").read()

def encrypt(filename, key):
    #Encrypt file with given key
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(filename, "wb") as file:
            file.write(encrypted_data)
    print("Encryption for {} done!".format(filename))
    
def decrypt(filename, key):
    #Decrypt file method added for use if needed
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)
    print("Decryption for {} done!".format(filename))
        
main()