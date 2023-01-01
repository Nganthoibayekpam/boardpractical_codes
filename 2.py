#Write a function countmy() in python to read the text file "DATA.TXT" and count the
#number of times "my" occurs in the file.

def countmy():
    f= open("data.txt", "r")
    count =0
    x= f.read()
    w= x.split()
    for i in w:
        if i == "my":
            count= count+1
    print ("my occurs", count, "times")
    f.close()
countmy()