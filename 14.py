#A binary file “Store.dat” has structure [ItemNo, Item_Name, Company, Price].
# i) Write a function CountRec(Company) in Python which accepts the Company name as
#  parameter and count and return number of Items by the given Company.
# ii) Write a function AddRecord(<List>) which accepts a List of the record [ItemNo, Item_Name,
#  Company, Price] and appends in the binary file “Store.Dat”.

import pickle
def CountRec(company):
    f=open("store.dat","rb")
    p=[]
    h={}
    try:
        while True:
            g=pickle.load(f)
            p.append(g)
    except EOFError:
        for i in p:
            if i[2] in h:
                h[i[2]]=h[i[2]]+1
            else:
                h[i[2]]=1
        n=h.items()
        for i in n:
            if i[0]==company:
                print('Company name: ',i[0],"Count",i[1])
    f.close()
def AddRecord(list):
    fh=open("store.dat","wb")
    g=pickle.dump(list,fh)
    fh.close()