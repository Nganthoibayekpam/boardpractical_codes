#Write a program to use methods ReadCSV(UserName) and WriteCSV() to include username and
#password as some entries for a CSV file “mydata.csv” and display them.

import pickle
def WriteCSV(Username,password):
    fh=open("mydata.csv","ab")
    l=[Username,password]
    pickle.dump(l,fh)
    fh.close()
def ReadCSV():
    f=open("mydata.csv","rb")
    try:
        while True:
            n=pickle.load(f)
            print(n)
    except EOFError:
        f.close()
s=int(input('Enter no of accounts: '))
for i in range(s):
    usn=input("Username: ")
    passw=input("password: ")
    WriteCSV(usn,passw)

ReadCSV()