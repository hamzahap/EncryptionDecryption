# EncryptionDecryption

A simple Encryption/Decryption script for Databases using PyMySQL and Cryptography library. 

# Backup.py

The library for dotenv is https://pypi.org/project/python-dotenv/ <br/>
The main function creates the Backups and Keys Directories if they don't exist. <br/>
The encrypt and decrypt function do exactly what they sound like they do. <br/>
The library used to make a connection with the database is https://pypi.org/project/PyMySQL/ <br/>
The scripts collects data from tables in your database. <br/>
The data is then saved into .csv files using pandas dataframes. <br/>
The .csv files are then encrypted via the the cryptography Fernet library. <br/>

To run the script type py Backup.py in the command line obviously. <br/>

The file format for the csv files is Tablename-date.csv . <br/>
The file format for the key files is Key-date.key . <br/>

# Encrypt.py

The main function looks for the first two arguments, the file and the key file. <br/>

To run the script type py Encrypt.py "Tablename-date" "Key-date" in the command line. <br/>

Note: The script has to be run in the same directory as the Backups and Keys folder access are manually set in the script.

# Decrypt.py

The main function looks for the first two arguments, the encrypted file and the key file. <br/>

To run the script type py Decrypt.py "Tablename-date" "Key-date" in the command line. <br/>
Note: The script has to be run in the same directory as the Backups and Keys folder access are manually set in the script.