# Qno1: Write a program to check if a number is positive or negative
num= int(input("Enter a number:"))
if num>0:
    print("Number is positive..")
else:
    print("Number is negative..")

# Qno2: Write a program to check if a number is even or odd 

num_1= int(input("Enter a number:"))
if num_1 % 2==0:
    print("Even..")
else:
    print("Odd..")

# Qno3: Write a program to create a area calculator 

print ("============= AREA CALCULATOR ===============")
print("""
Enter 1 for area of a square.
Enter 2 for area of rectange.
Enter 3 for area of triangle.
Enter 4 for area of circle. 
""")

choice=int(input("Enter Your Choice Between 1 to 4 :"))

if choice == 1:
    side=int(input("Enter Side: "))
    area=side**2
    print(area)
elif choice==2:
    lenght=float(input("Enter lenght: "))
    width=float(input("Enter Width: "))
    area=lenght*width
    print(area)
elif choice==3:
    base=float(input("Enter base: "))
    hight=float(input("Enter hight: "))
    area=0.5*base*hight
    print(area)
elif choice==4:
    radius=float(input("Enter radius: "))
    area=3.142*radius**2
    print(area)
else:
    print("Try Again!!!")