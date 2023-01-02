#Write a program that copies a text file 
#"source.txt" onto "target.txt" barring the lines starting with “@”.

s = open("source.txt","r")
t = open("target.txt", "w")
d = s.readlines()
for i in d:
    if i[0] == "@":
        t.write(i)
s.close()
t.close()
