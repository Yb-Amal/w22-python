users = ['Dave', 'John' , 'Sara']

data = ['Dave', 34 , True]

emptylist = []

# print("Dave" in emptylist)

# print(users[0])
# print(users[-2])

# print(users.index('Sara'))

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(users))

users.append('Elsa') #adding name append
print(users)

users += ['Jason'] # also adding name +=
print(users)

users.extend(['Robert' , 'Jimmy']) # adding names 

print(len(users))

# users.extend(data)
# print(users)

users.insert(0, 'Bob') # position in place and adding a name 
print(users)

users[2:2] = ['Eddie' , 'Alex'] 
print(users)

users[1:3] = ['Amal', 'JB'] # replace the value
print(users)

users.remove('Bob')
print(users)

print(users.pop())
print(users)

del users[1]
print(users)

# data.clear()
# print(data)

users[1:2] =['Dave']
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums= [4,25,13,11,2]
nums.reverse()
print(nums)

# nums.sort(reverse=True) # greater nums to less num 
# print(nums)

print(sorted(nums, reverse=True))

numscopy = nums.copy()
mynums = list(nums)
mynums = nums[:]

# Tuples

mytuples = tuple(('Dave', 24 ,True))
anothertuple = (1, 6, 4, 21, 2, 2)

print(mytuples)
print(anothertuple)
print(type(mytuples))
print(type(anothertuple))

# newlist = list(mytuples)
# newlist.append('Neil')
# newtuple = tuple(newlist)
# print(newtuple)

# (one, *two, hey) = anothertuple
# print(one)
# print(two)
# print(hey)

# print(anothertuple.count(2))