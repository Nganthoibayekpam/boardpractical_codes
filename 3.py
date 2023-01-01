#Write a method in python to read lines from a text file MYNOTES.TXT and display those
#lines which start with alphabets 'K'.

def dispk():
    f= open("mynotes.txt", "r")
    l= f.readlines()
    for i in l:
        if i[0] =='k':
            print (i, end="")
    f.close()
dispk()