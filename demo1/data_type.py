# String daa type

# literal assignment 

first = "Joe"
last = "Smith"

# print(type(first))
# print(type(first)==str)
# print(isinstance(first, str))

# constructor function
# pizza = str("Pepper")

# print(type(pizza))
# print(type(pizza)==str)
# print(isinstance(pizza, str))

# Concatenation = combine together
fullname = first + " " + last
print(fullname)

# Adding a fullname
fullname += "!" 
print(fullname)

# Casting a number to a string
decade = str(1990)
print(type(decade))
print(decade)

statement = "I like Jazz music from the " + decade + "s."
print(type(statement))
print(statement)

# Multple lines
multiline = '''
Hey, how are you?

i was just checking in.
                                All good?
'''
print(multiline)

# Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

