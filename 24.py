#A list of 10 students’ marks is given below.Write a program with separate user defined functions to
#perform the following operation.
#Traverse the content of the list and push the numbers higher than 33 into a stack.
#pop and display the content of the stack.
#For example:
# If N=[12,13,34,56,21,79,98,22,35,38]
# sample output should be 38,35,98,79,56,34

def isempty(lst):
    if lst==[]:
        return True
    else:
        return False
def push(lst,ele):
    lst.append(ele)
def pop(lst):
    if isempty(lst):
        print("the stack is empty")
    else:
        lst.pop()
def display(l):
    if isempty(l):
        print("The stack is empty")
    for i in l:
        print(i,end=",")
g=[]
N=[12,13,34,56,21,79,98,22,35,38]
for i in N:
    if i>33:
        push(g,i)
    else:
        continue
pop(g)
display(g)

