'''
Continue Statement:
Continue Statement is used when you want to skip a particular condition.

Break Statement:
Break statement is used when you want to destroy a loop at a certain condition and comeout of the loop.
'''
print("Continue Statement")

for i in range (1,21):
    if i == 10:
        continue
    else:
        print(i)

print("Break Statement")

for i in range (1,11):
    if i == 3:
        break
    else:
        print(i)