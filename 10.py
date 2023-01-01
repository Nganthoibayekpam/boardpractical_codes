#Create a binary file with name and roll number. Search for a given roll number and display the name,
#if not found display appropriate message.

import pickle
f=open("student.dat", "wb")
n = int(input("Enter number of records: "))
for i in range(n):
    sname= input("Enter Student name: ")
    srollnm= int(input("Enter student roll no.: "))
    rec = {'sname':sname, 'srollnm':srollnm}
    pickle.dump(rec, f)
f.close()
f=open("student.dat", "rb")
k=int(input("Enter the Roll Number: "))
flag = False
while True:
   try:
       x=pickle.load(f)
       if x['srollnm']==k:
        print("Name: ",x['sname'])
        flag = True
   except EOFError:
       break
if flag==False:
   print("This Roll Number does not exist")