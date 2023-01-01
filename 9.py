#Remove all the lines that contain the character ‘a’ in a 
#file and write it to another file.

f=open("story.txt", 'r')
fh=open("file.txt", 'w')
a = []
l=f.readlines()
for i in l:
    if 'a' in i:
        a += [i]
fh.writelines(a)
f.close()
fh.close()