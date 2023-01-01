#consider a binary file employee.dat containing details such as
#empno:ename:salary(separator ':') write a python function to display details of those
#employees who are earning between 20000 and 30000(both values inclusive)

import pickle
f=open("employee.dat","ab+")
employee=[]
eno=int(input("Enter number:"))
for i in range(eno):
    empno=int(input("Employee no :"))
    ename=input("Employee name :")
    salary=int(input("salary :"))
    p=[empno,ename,salary]
    n=employee.append(p)
    pickle.dump(n,f)
try:
    while True:
        j=pickle.load(f)
        if j[3]>=20000 and j[3]<=30000:
            print(j,sep=":")
except EOFError:
    f.close()

import pickle
def Readfile():
    i = open("employee.dat","rb+")
    try:
        while True:
            x=pickle.load(i)
            
            if float(x[2])>=20000 and float(x[2])<=30000:
                print(i)
    except EOFError:
        print("something's wrong..")
        i.close()
Readfile()