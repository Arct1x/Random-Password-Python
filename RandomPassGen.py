import string
import random
import pyperclip # type: ignore
import os

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

while True:
    pass_legnth = int(input("In Numerical form, please type out how long you wish your password to be (8-36): "))
    if pass_legnth > 36 or pass_legnth < 8:
        print("Please try again")
    else:
        print("Generating Password")
        break

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

p1 = round(pass_legnth * (30/100))
p2 = round(pass_legnth * (20/100))
result = []

for x in range(p1):
    result.append(s1[x])
    result.append(s2[x])
for x in range(p2):
    result.append(s3[x])
    result.append(s4[x])

random.shuffle(result)

password = "".join(result)

print("Your generated password is:", password)
QSave = str(input("Would you like to save this to a file (A new one will be generated if there isn't already an existing one.) [Y/N]: "))
str.upper(QSave)

if QSave == "N":
    print("Your password has been copied to clipboard.")
    pyperclip.copy(password)
else:
    f = open("Passwords.txt", "a")
    Qfor = input("What website and/or application will this be used for?: ")
    f.write("\n Password for ")
    f.write(Qfor)
    f.write(": ")
    f.write(password)
    print("Saved password to \v", os.path.realpath("Passwords.txt"))
