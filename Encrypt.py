from cryptography.fernet import Fernet
import sys

def main():
    thefile = "Backups/" + sys.argv[1] + ".csv"
    keyfile = "Keys/" + sys.argv[2]  + ".key"
    key = open(keyfile, "rb").read()
    encrypt(thefile, key)

def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(filename, "wb") as file:
            file.write(encrypted_data)
    print("Encryption for {} done!".format(filename))

main()