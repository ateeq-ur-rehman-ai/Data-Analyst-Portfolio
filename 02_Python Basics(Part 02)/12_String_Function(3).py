a="Artifical Intelligence"
# endswith()-- Returns True if the string ends with the specified value
print(a.endswith("e"))
print(a.endswith("t",10,13))

# startswith()-- Returns True if the string starts with the specified value
print(a.startswith("A"))
print(a.startswith("I",10,13))

# swapcase()-- Swap case , lower case becomes upper case and upper becomes lower 
print(a.swapcase())

# strip()-- Returns a trimmed version of a string 
b="     Machine Learning    "
c="-------- Machine Learning =============="
print(c.strip("-,="))

# split()-- Spilit  the string at the specified sperator and returns a list 
d="Hi. My name is Jack. I am 20 years old"
print(d.split("."))

# ljust()-- Returns a left justified version of a string 
x=a.ljust(50 ,"-")
print(x, "Is growing very fast ")

# ljust()-- Returns a left justified version of a string 
x=a.rjust(30 ,">")
print(x, "Is growing very fast ")

# replace()-- Returns a string where a specified value is replace with a specified value 
e="Hello my name is jack. jack like to play cricket"
print(e)
print(e.replace("jack","Rock"))

# rindex()-- search the string for a specified value and returns the last position of where it was found 
f="Harry Potter and the prisoner of zenda"
print(f.rindex("prisoner"))
print(f.rindex("Potter"))