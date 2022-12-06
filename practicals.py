#1 Write the definition of a method countnow(places) to find and display those place names, in which there are more than 7 characters.
#For example: If the list places contains. ["MELBOURNE", "TOKYO", "PINKCITY", "BEIJING", "SUNCITY]

def countnow(places):
    for x in places:
        if len(x)>7:
            print (x)
places = ["Melbourne", "Tokyo", "Pinkcity", "Beijing", "Suncity"]
countnow(places)

#2 Write a function countmy() in python to read the text file "DATA.TXT" and count the
#number of times "my" occurs in the file.

def countmy():
    f= open("data.txt", "r")
    count =0
    x= f.read()
    w= x.split()
    for i in w:
        if i == "my":
            count= count+1
    print ("my occurs", count, "times")
    f.close()
countmy()

#3 Write a method in python to read lines from a text file MYNOTES.TXT and display those
#lines which start with alphabets 'K'.

def dispk():
    f= open("mynotes.txt", "r")
    l= f.readlines()
    for i in l:
        if i[0] =='k':
            print (i, end="")
    f.close()
dispk()

#4 Write a program that copies a text file "source.txt" onto "target.txt" barring the lines starting with “A”.
s = open("data.txt","r")
t = open("realreal.txt", "w")
d = s.readlines()
for i in d:
    if i[0] == "@":
        t.write(i)
s.close()
t.close()

#5 Write a function SRCount() in Python, which should read each character of a text file
#STORY.TXT, should count and display the occurrence of alphabets S and R (including
#small cases s and r too)

def srcnt():
    f = open("story.txt", "r")
    S = 0
    R = 0
    k = f.read()
    for i in k:
        if i == "S" or i == "s":
            S = S+1
        if i == "R" or i == "r":
            R = R+1
    print ("Occurence of s in story: ", S)
    print ("Occurence of r in story: ", R)
    f.close()
srcnt()

#6 Write a function Display( ) in python to read lines from a text file “XYZ.txt” and
#display those words, which are greater than or equal to 3 characters

def display():
    file = open("data.txt", "r")
    data = file.read()
    bag = data.split()
    for i in bag:
        if len(i) >= 3:
            print(i)
    file.close()
display()

#7 Write a function count_is_as() in Python that counts the number of “is” and “as” words
#present in a text file “STORY.TXT”.

def count_AS_IS():
    f=open('story.txt', 'r')
    count=0
    n=f.read()
    for i in n.split():
        if i=='is' or i=='as':
            count=count+1
    print("as & is occurs",count,"times")
    f.close()
count_AS_IS()

#8 Read a text file and display the number of vowels/consonants/uppercase/lowercase characters in the file.
f=open("xyz.txt", 'r', encoding="utf8")
lc=0
uc=0
vow=0
cons=0
for i in f.read():
    if i.isalpha():
        if i in ['a','e','i','o','u','A','E','I','O','U']:
            vow=vow+1
        else:
            cons=cons+1
        if i.isupper():
            uc=uc+1
        if i.islower():
            lc=lc+1
print("vowels: ",vow)
print("consonants: ",cons)
print("uppercase: ",uc)
print("lowercase: ",lc)

#9 Remove all the lines that contain the character ‘a’ in a file and write it to another file.
f=open("harry.txt", 'r')
fh=open("openall.txt", 'w')
a = []
l=f.readlines()
for i in l:
    if 'a' in i:
        a += [i]
fh.writelines(a)
f.close()
fh.close()

#10  Create a binary file with name and roll number. Search for a given roll number and display the name, if not found display appropriate message
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

#check code
#11 Create a binary file with roll number, name and marks. Input a roll number and update the marks.
import pickle
def insertRec():
    rollno = int(input('Enter roll number: '))
    name = input('Enter Name: ')
    marks = int(input('Enter Marks: '))
    rec = {'Rollno':rollno,'Name':name,'Marks':marks}
    f = open('history.dat','ab')
    pickle.dump(rec,f)
    f.close()
insertRec()

#12 consider a binary file employee.dat containing details such as
#empno:ename:salary(separator ':') write a python function to display details of those
#employees who are earning between 20000 and 30000(both values inclusive)
import pickle
f=open("employee.dat","wb+")
employee=[]
eno=int(input("Number of employee datas: "))
for i in range(eno):
    empno=int(input("Employee number: "))
    ename=input("Employee name: ")
    salary=int(input("Salary: "))
    p=[empno,ename,salary]
    rec=employee.append(p)
    pickle.dump(rec,f)
try:
    while True:
        j=pickle.load(f)
        if j[3]>=20000 and j[3]<=30000:
            print(j,sep=":")
except EOFError:
    f.close()
f=open("employee.dat","rb+")
def Readfile():
    i = open("employee.dat","rb+")
    x = i.readline()
    while(x):
        if (20000>=float(x[2])<=30000):
            print(x, sep=":")
            x = i.readline()
Readfile()

#13 Write a function Count_Rec() in Python that would read contents of the file
#“SCHOOL.DAT” and display the details of those students whose percentage is below 33%.
#Also display the number of students scoring below 33%
import pickle
f=open("student.dat", "wb")
n = int(input("Enter number of records: "))
for i in range(n):
    sname= input("Enter Student name: ")
    srollnm= int(input("Enter student roll no.: "))
    smarks= int(input("Enter marks in %: "))
    rec = ['sname','srollnm','smarks']
    pickle.dump(rec, f)
def countrec():
    count = 0
    f = open("STUDENT.dat", "rb")
    try:
        while True:
            t = pickle.load(f)
            if t[2]<33:
                count=count+1
                print(t)
    except:
        print("Number student with per  greater than 33%", count)
        f.close()
def disp_rec(a):
    f = open("STUDENT.dat", "rb")
    try:
        while True:
            item = pickle.load(file)
            if item['sname'][0] == a:
                print(item)
    except:
        f.close() 
countrec()
disp_rec('L')
