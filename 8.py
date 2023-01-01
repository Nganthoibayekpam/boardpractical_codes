#Read a text file and display the number of vowels/consonants/uppercase/lowercase characters in the
#file.

f=open("xyz.txt", 'r')
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
print("lowercase: ",lc)