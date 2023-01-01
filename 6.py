#Write a function Display( ) in python to read lines from a text file “XYZ.txt” and
#display those words, which are greater than or equal to 3 characters.

def Display():
    file = open("XYZ.txt", "r")
    data = file.read()
    bag = data.split()
    for i in bag:
        if len(i) >= 3:
            print(i)
    file.close()
Display()