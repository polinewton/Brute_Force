import os
r = range(0,10001)
lst = []

for num in r:
    lst.insert(num,num)

lsts = str(lst)

os.remove("codes.txt")

f = open("codes.txt", "w")

f.write(lsts)

f1 = open("codes.txt","r")
print(f1.read())
f.close()