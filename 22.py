#i)Write AddCustomer(Customer) method in Python to add a new customer, considering it to act as a
# PUSH operation of the stack data structure. Also display the contents of the Stack after PUSH
# operation.
#ii) Write RemoveCustomer(Customer) method in Python to remove a Customer, considering it to act as
# a POP operation of the stack data structure. Also return the value deleted from stack. Details of the
# Customer are: CID and Name.

def AddCustomer(Customer,s):
    Customer.append(s)
    print(Customer)
Bills=["Alisha","Remi","Mia"]
c="Tiffany"
AddCustomer(Bills, c)
def empty(s):
    if len(s)==0:
        return True
    else:
        return False
def RemoveCustomer(Customer,c):
    if empty(Customer)==True:
        print("Underflow!")
    else:
        return Customer.pop(c)
        
c={1:"Tate",2:"Carlos",3:"Drew"}
d=1
g=RemoveCustomer(c,d)
print(g,"Removed")
print("New dictionary",c)