#Vikram has a list containing 10 integers. You need to help him create a program with separate user
#defined functions to perform the following operations based on this list.
#Traverse the content of the list and push the ODD numbers into a stack.
#Pop and display the content of the stack.
#For Example If N=[12, 13, 34, 56, 21, 79, 98, 22, 35, 38] the sample output should be
#35,89,21,13

def isempty(l):
  if l==[]:
    return True
  else:
    return False
def PushOn(l,m):
  l.append(m)
def pop(l):
  if isempty(l):
    print("Error:-stack underflow")
  else:
    l.pop()
def display(l):
    if isempty(l):
        print("The stack is empty")
    for i in l[::-1]:
        print(str(i),end=",")
p=[]
n=[12, 13, 34, 56, 21, 79, 98, 22, 35, 38]
for i in n:
    if i%2!=0:
        PushOn(p,i)
pop(p)
display(p)