#Write a function count_is_as() in Python that counts the number of “is” and “as” words
#present in a text file “STORY.TXT”.

def count_is_as():
    f=open('story.txt', 'r')
    count=0
    n=f.read()
    for i in n.split():
        if i=='is' or i=='as':
            count=count+1
    print("as & is occurs",count,"times")
    f.close()
count_is_as()