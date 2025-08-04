#DateTime
import datetime
x=datetime.datetime.now()
print(x)

y=datetime.datetime(2005,7,30)
print(y.strftime("%A"))

#Random
import random
a=random.randint(1,20)
print(a)

import random
l=["Rock" , "Paper", "Sissors"]
y=random.choice(l)
print(y)

#Math 
import math

b=max(68,37,218)
print(b)

c=min(82,21,92)
print(c)

d=pow(3,5)
print(d)

e=math.sqrt(81)
print(e)

f=abs(-26)
print(f)

g= math.ceil(7.3)
print(g)

h=math.floor(7.3)
print(h)
