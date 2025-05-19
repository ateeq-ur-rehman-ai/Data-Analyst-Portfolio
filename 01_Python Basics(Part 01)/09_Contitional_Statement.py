# Conditional Statement 
'''
Contitional statement allows computer to excute a certain condition only if it is true.
Types of conditional statement 
1.if 
2.if-else 
3.if-elif-else
4.nested 
5.short hand if 
'''

marks=67
if marks>50:
    print("You Pass The Exam :")

marks=23
if marks>50:
    print("You Pass The Exam :")
else:
    print("You are fail in exam :")

marks=70
if marks>=85:
    print("your GPA is 3.5")
elif marks>=84 and marks>70:
    print("your GPA is 3")
elif marks>=69 and marks>50:
    print("Your GPA is 2.5")
else:
    print("Your GPA is Below 2.5")
