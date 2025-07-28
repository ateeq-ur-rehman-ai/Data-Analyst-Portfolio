values="Ali",35,25,2.4,"Jabbar",839,"Moeen",6872729,True,False
print(values)

# With for loop
for i in values:
    print(i)

print("-"*30)

# Along with range and length in for loop
for i in range(len(values)):
    print(values[i])

print("-"*30)

# With while loop
i=0
while i<len(values):
    print(values[i])
    i+=1