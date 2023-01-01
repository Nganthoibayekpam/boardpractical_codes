#i)Write a function Count_Rec() in Python that would read contents of the file
# “SCHOOL.DAT” and display the details of those students whose percentage is below 33%.
# Also display the number of students scoring below 33%.
#ii) Write a function Disp_Rec(alphabet) in Python that would read contents of the file
# “SCHOOL.DAT” and display the details of those students whose name begin with the
# alphabet as passed as parameter to the function.

import pickle
print("Searching... please wait..")
def Count_Rec():
    with open('school.dat', 'rb') as fin:
        count=0
        while True:
                try:
                    ind=pickle.load(fin)
                    if ind[2]<33:
                        print(ind)
                        count = count + 1 
                except EOFError:
                    fin.close()  
                    break
        print ("Search successful!")
        print ("Students scored less than 33% are ", count)
Count_Rec()

def disp_rec(a):
    f = open("school.dat", "rb")
    try:
        while True:
            t = pickle.load(f)
            if t[1][0]==a:
                print(t)
    except EOFError:
        f.close()
g=input("Enter a letter: ")
disp_rec(g)
