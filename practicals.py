#1
'''def countnow(places):
    for x in places:
        if len(x)>7:
            print (x)
places = ["Melbourne", "Tokyo", "Pinkcity", "Beijing", "Suncity"]
countnow(places)'''

#2
'''def countmy():
    f= open("data.txt", "r")
    count =0
    x= f.read()
    w= x.split()
    for i in w:
        if i == "my":
            count= count+1
    print ("my occurs", count, "times")
    f.close()
countmy()'''

#3
'''def dispk():
    f= open("mynotes.txt", "r")
    l= f.readlines()
    for i in l:
        if i[0] =='k':
            print (i, end="")
    f.close()
dispk()'''

#4
'''s = open("data.txt","r")
t = open("realreal.txt", "w")
d = s.readlines()
for i in d:
    if i[0] == "@":
        t.write(i)
s.close()
t.close()'''

#5
'''def srcnt():
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
srcnt()'''

#6
'''def display():
    file = open("data.txt", "r")
    data = file.read()
    bag = data.split()
    for i in bag:
        if len(i) >= 3:
            print(i)
    file.close()
display()'''

#7
'''def count_AS_IS():
    f=open('story.txt', 'r')
    count=0
    n=f.read()
    for i in n.split():
        if i=='is' or i=='as':
            count=count+1
    print("as & is occurs",count,"times")
    f.close()
count_AS_IS()'''

#8
'''f=open("xyz.txt", 'r', encoding="utf8")
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
print("lowercase: ",lc)'''

