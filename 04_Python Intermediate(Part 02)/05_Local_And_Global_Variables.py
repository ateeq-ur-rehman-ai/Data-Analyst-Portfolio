'''
Local Variables: Local Variables are restricted to only one block of code and cannot be changed throughout the program.
'''
x=25
print("Value of X is " , x)
def local():
    x=26
    return x
print (local())


'''
Global Variables:Global Variable are not restricted to only one block of code and can be changed throughout the program.
'''

y=25
print("Value of X is " , y)
def Global():
    global y
    x=26
    return y
print (local())
print(y)

