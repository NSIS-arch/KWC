#Created by NSIS

#Libraries
import random
import string

###Defualt Key Length###
digit = 64

###Characters used###
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

###Character Combination###
all = lower + upper + num + symbols

###Mix###
temp = random.sample(all,digit)
password = "".join(temp)

###Writing Func###
file_object = open("keys.txt","a")

###Write Keys###
file_object.write(password + "\n")
file_object.close()
###End###