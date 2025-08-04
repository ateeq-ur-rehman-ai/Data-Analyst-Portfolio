'''
Q no 1 : Write a function to find maximum of three in python.
'''
def Maximum_num(num1,num2,num3):
    if num1>num2 and num1>num3:
        print("Num 1 is greatest")
    elif num2>num1 and num2>num3:
        print("Num 2 is greatest")
    else:
        print("Num 3 is greatest")    
Maximum_num(24,36,-27)

'''
Q no 2 : Write a python function to create and print a list where the values are the square of numbers between 1 and 30.
'''

def Create_list ():
    l=[]
    for i in range (1,31):
        l.append(i**2)
    return l 
print(Create_list())