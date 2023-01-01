#Write a menu based program to add, delete and display the records of the hostel using list as stack
#data structure in python. Record of the hostel contains the fields : Hostel number, Total Students
#and Total Rooms.

host=[ ]
ch='y'
def push(host):
  hn=int(input("Enter hostel number"))
  ts=int(input("Enter Total students"))
  tr=int(input("Enter total rooms"))
  temp=[hn,ts,tr]
  host.append(temp)

def pop(host):
  if(host==[]):
      print("No Record")
  else:
      print("Deleted Record is :",host.pop())

def display(host):
  l=len(host)
  print("Hostel Number:Total Students:Total Rooms")
  for i in range(l-1,-1,-1):
      print(host[i][0],":",host[i][1],":",host[i][2])

while(ch=='y' or ch=='Y'):
  print("1. Add Record\n")
  print("2. Delete Record\n")
  print("3. Display Record\n")
  print("4. Exit")
  op=int(input("Enter the Choice"))
  if(op==1):
      push(host)
  elif(op==2):
      pop(host)
  elif(op==3):
      display(host)
  elif(op==4):
      break
  else:
       ch=input("Do you want to enter more(Y/N)")