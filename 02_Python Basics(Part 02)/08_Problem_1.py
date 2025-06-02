# Qno1: Write a program to find a sum of all even numbers up to 50.
sum=0
for i in range (1,51):
    if i % 2 == 0:
        sum  += i
print("The sum of all even number is : ", sum)

# Qno2: Write a program to write first 20 numbers and their square number.
for i in range (1,21):
    print(i , i**2)

# Qno3: Write a program to find sum of first 10 odd numbers using while loop
sum=0 
n=0
while n<=20:
    if n % 2 !=0:
        sum += n 
    n +=1
print("The sum of first 10 odd number is : ", sum)

# Qno4: Write a program to check if number is divisible by 8 and 12, upto 100 numbers.
for i in range (1,101):
    if i % 8==0 and i % 12 ==0:
        print(i)

for i in range (1,6):
    for j in range (5,i,-1):
        print(" ", end = " ")
    for k in range(i):
        print("*", end = " ")
