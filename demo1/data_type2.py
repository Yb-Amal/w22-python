# String Methods
# s = "James"
# t = "Johnson"

# print(s)
# print(s.lower())
# print(s.upper())
# print(s)

multiline = '''
Hey, how are you?

i was just checking in.
                                All good?
'''
"""print(multiline)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += "                         "
multiline = "          " + multiline
print(len(multiline)) 

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))"""

# Build a menu
# title = "menu".upper()
# print(title.center(20, "="))
# print("Coffee".ljust(16, ".") + "$1" .rjust(4))
# print("Bagels".ljust(16, ".") + "$2.50" .rjust(4))
# print("Cheesesteak".ljust(16, ".") + "$6.50" .rjust(4))

# String index values
first = "Kevin"
last = "Joes"
# print(first[0])
# print(first[-1])
# print(first[1:3])
# print(first[1:])


# Some methods return boolean data
print (first.startswith("D"))
print (first.startswith("K"))
print ( first.endswith("n"))

# boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(myvalue)

# Numeric data types

# interger type
price = 100 
best_price = int(80)
print(type(price))
print(price)

# float type 
gpa = 3.28
y = float(1.14)
print(type(gpa))
print(gpa)

# Casting a string to a number 
zipcode = "01854"
zip_value = int(zipcode)
print(type(zipcode))
print(type(zip_value))
print(zipcode)