#Create a binary file with roll number, name and marks.
#Input a roll number and update the marks.

import pickle
def  Writerecord(sroll,sname,sperc):
    with open ('StudentRecord.dat','ab') as Myfile:
        srecord={"SROLL":sroll,"SNAME":sname,"SPERC":sperc}        
        pickle.dump(srecord,Myfile)
       
def Readrecord():
    with open ('StudentRecord.dat','rb') as Myfile:
        print("DISPALY STUDENTS DETAILS")
        print("\nRoll No.",' ','Name','\t',end='')
        print('Percetage')
        while True:
           try:
               rec=pickle.load(Myfile)
               print(' ',rec['SROLL'],'\t  ' ,rec['SNAME'],'\t ',end='')
               print(rec['SPERC'],'\t   ')
           except EOFError:
                break
def Input():
    n=int(input("How many records you want to create :"))
    for ctr in range(n):
        sroll=int(input("Enter Roll No: "))
        sname=input("Enter Name: ")
        sperc=float(input("Enter Percentage: "))
        Writerecord(sroll,sname,sperc)
        

def Modify(roll):
    with open ('StudentRecord.dat','rb') as Myfile:
        newRecord=[]
        while True:
           try:
               rec=pickle.load(Myfile)
               newRecord.append(rec)
           except EOFError:
                break
    found=1       
    for i in range(len(newRecord)):
        if newRecord[i]['SROLL']==roll:
            name=input("Enter Name: ")
            perc=float(input("Enter Percentage: "))

            newRecord[i]['SNAME']=name
            newRecord[i]['SPERC']=perc
            found =1
        else:
            found=0

    if found==0:

        print("Record not found")
    with open ('StudentRecord.dat','wb') as Myfile:
         for j in newRecord:
             pickle.dump(j,Myfile)


def main():
   
    while True:
        print('\nYour Choices are: ')
        print('1.Insert Records')
        print('2.Dispaly Records') 
        print('3.Update Records')
        print('0.Exit (Enter 0 to exit)')
        ch=int(input('Enter Your Choice: '))
        if ch==1:
            Input()
        elif ch==2:
            Readrecord()
        elif ch==3:
            r =int(input("Enter a Rollno to be update: "))
            Modify(r)
        else:
            break
main()