#A programmer wants to prepare a stack from a given list of integer elements only for numbers
#which are divisible by 3. Help him create a program with user defined functions to perform the
#following operations based on this list.
# Traverse the content of the list and push the numbers into a stack which are divisible by 3.
# Pop and display the content of the stack.
#If N=[3,5,10,13,21,23,45,56,60,78]
#The output will be 60,45,21,3

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
n=[3,5,10,13,21,23,45,56,60,78]
for i in n:
    if i%3==0:
        PushOn(p,i)
pop(p)
display(p)