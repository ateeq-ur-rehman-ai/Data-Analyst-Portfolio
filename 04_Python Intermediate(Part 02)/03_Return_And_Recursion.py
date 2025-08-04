'''
Return Keyword in pyhton is used to exit a function and return the value of the function.
'''

def sub(a,b):
    return(a-b)
print(sub(78,24))

'''
Recursion in most commonly mathematical and programming concept.
In Simple Words, recursion means a function can call itself, giving us a benifit of looping through data in .order to get a result
'''

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5)) 
