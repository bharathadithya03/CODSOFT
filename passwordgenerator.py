#Task1

import random
import string
listpassword=[]
n_letters=int(input("How many letters you want in Password:?\n"))
n_numbers=int(input("How many numbers you want in Password:?\n"))
n_symbols=int(input("How many symbols you want in Password:?\n"))
for i in range(1,n_letters+1):
    ch=random.choice(string.ascii_letters)
    listpassword += ch
for i in range(1,n_numbers+1):
    ch=random.choice(string.digits)
    listpassword += ch
for i in range(1,n_symbols+1):
    ch=random.choice(string.punctuation)
    listpassword += ch

random.shuffle(listpassword)

password=""
for char in listpassword:
    password+=char
print("password is generated:",password)