#Write PushOn(Book) and Pop(Book) methods/functions in Python to add a new Book
#and delete a Book from a list of Book titles, considering them to act as push and pop
#operations of the Stack data structure.

def empty(s):
    if len(s)==0:
        return True
    else:
        return False
def PushOn(Book,s):
    Book.append(s)
def Pop(Book):
    if empty(Book)==True:
        print("Underflow!")
    else:
        Book.pop()
s=["ND advent","dice","23+24"]
PushOn(s,"Money")
PushOn(s,"SelG")
Pop(s)
print(s)