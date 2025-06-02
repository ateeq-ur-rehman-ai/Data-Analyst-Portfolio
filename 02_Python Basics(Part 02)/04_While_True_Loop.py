'''
It is a infinte loop 
To break a while true loop , break statement is used .
'''

while True:
    num1=int(input("Enter num 1: "))
    num2=int(input("Enter num 2: "))
    print(num1+num2)
    choice=input("Do you want to stop the program: ")
    if choice=="yes":
        print("Thank You")
        break
