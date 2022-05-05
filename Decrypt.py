from cryptography.fernet import Fernet
import sys

def main():
    encryptedfile = "Backups/" + sys.argv[1] + ".csv"
    keyfile = "Keys/" + sys.argv[2]  + ".key"
    key = open(keyfile, "rb").read()
    decrypt(encryptedfile, key)

def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)
    print("Decryption for {} done!".format(filename))

main()