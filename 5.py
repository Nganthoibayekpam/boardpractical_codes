#Write a function SRCount() in Python, which should read each character of a text file
#STORY.TXT, should count and display the occurrence of alphabets S and R (including
#small cases s and r too).

def SRCount():
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
SRCount()