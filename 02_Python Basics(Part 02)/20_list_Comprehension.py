l1=[20,39,89,682]
l2=[]
for i in l1:
    l2.append(i)

print(l1,"\n",l2)

l3=[i for i in l1 if i > 30]
print(l3)