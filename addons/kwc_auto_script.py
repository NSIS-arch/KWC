#Created by NSIS

#Libraries
import os 

###Delete the # sign in front of the operating system you are using.###

###Windows###
#os.system("cls")

###Linux###
#os.system("clear")

###input func###
x = int(input('''Choose action:

1) Auto key Create

2) Open key list

0) Exit

'''))

###Auto script###
if x == 1:
    print("Creating Keys...")
    print("If you want close this process press ctrl + c")
    while x ==1:
        os.system("python .\kwc.py")
    
###Key list open with notepad###
elif x ==2:
    os.system("notepad keys.txt")

###exit###
elif x ==0:
    exit

###Error###
else:
    
    ###Delete the # sign in front of the operating system you are using.###
    #os.system("cls")
    #os.system("clear")
    print("Please enter the correct number !")
    os.system("python addons\kwc_auto_script.py")
##End###