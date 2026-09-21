print("welcome")
pts = 0
password = input("enter your password : ")
if len(password) >= 8:
    pts += len(password) * 4
else:
    pts -= 20


Upper = any(c.isupper() for c in password)
lower = any(c.islower() for c in password)
Nember = any(c.isdigit() for c in password)
dach = any(c.isalpha() for c in password)


if Upper == True:
    pts += 10

if lower == True:
    pts += 10

if Nember == True:
    pts += 10

if dach == False:
    pts += 15

if Upper == True and lower == True and Nember == True and dach == False:
    pts += 15

if Upper == False and lower == False and Nember == True and dach == True:
    pts -= 20

if Upper == True and lower == True and Nember == False and dach == True:
    pts -= 15


def passw(password):
    for i in range(len(password) -2):
        if password[i] == password[i + 1 ] == password[i + 2]:
            return True

if passw(password) == True:
    pts -= 5

if pts >= 80:
    print("your password is very strong 🟢")
elif pts >= 60:
    print("your password is strong 🟡")
elif pts >= 40:
    print("your password is weak 🔴")
elif pts < 40:
    print("your password is very weak 🔴")

import requests

url = "https://github.com/danielmiessler/SecLists/blob/master/Passwords/Default-Credentials/default-passwords.txt"
passwords = requests.get(url).text

if password in passwords:
    print("This password used, please change it")
