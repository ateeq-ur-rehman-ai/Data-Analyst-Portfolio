"Q no 1: Write a python program to sort a dictionary by value"

a={"a":56,"b":562,"c":-82,"d":52}
a=sorted(a.values())
print(a)

'''
Q no 2 : Write a python script to print a dictionary where the keys are numbers between 1 and 15 the values are the square  
'''

b={}
for i in range(1,16):
    b[i]=i**2
print(b)

'''
Q no 3: Write a program to multiply all the items in a dictionary
'''

c={"a":1,"b":2,"c":3,"d":4,"e":5}
mul=1
for i in c:
    mul*=c[i]
print(mul)