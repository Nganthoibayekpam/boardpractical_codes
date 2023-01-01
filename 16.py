#Create a CSV file by entering user-id and 
#password, read and search the password for given user-id.

import csv
def WriteCSV():
    fh=open("mydata.csv","w")
    n=csv.writer(fh)
    r=int(input("Enter number of accounts: "))
    for i in range(r):
        print("Student record",i+1)
        usn=input("Enter your Username: ")
        passw=input("Enter your password: ")
        rec=[usn,passw]
        n.writerow(rec)
    fh.close()
WriteCSV()
def ReadCSV(UserName):
    with open("mydata.csv", newline="\r\n") as fh:
        n=csv.reader(fh)
        for r in n:
            if r[0]==UserName:
                print('Username:',UserName,"Password:",r[1])
        fh.close()
ch=input("Enter username to be searched: ")
ReadCSV(ch)