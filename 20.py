#Write a program for a linear search from a list using a function

def lsearch(AR,ITEM):
    i=0
    while i<len(AR) and AR[i]!=ITEM:
        i+=1
        if AR[i]==ITEM:
            return i
    else:
        return False
l=eval(input("Enter the list "))
a=eval(input("Enter the item to be searched: "))
p=lsearch(l,a)
print(p)