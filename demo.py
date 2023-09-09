a = 5
c = 10

print(type(a))
float(a)
str(a)

print(isinstance(c, complex))

# list
["Hello", "World"]

myList = [1,2 ,3]
myList = []
myList = [1, "Hell0", 3.4]
myList = ["mouse", [8, 4, 6], ['a']]

# print 1st index pos
print(myList[0])

# 5th last item
print(myList[-2])

myList = ['h', 'e', 'l', 'l', 'o']

# elements from index 2 to 4
print(myList[2:5])

# append to list
odd = [1, 3 ,5]
odd.append(7)

# concat arrays & repeating list
odd = [1, 3, 5]
print(odd + [9, 7, 5])

del myList[2]

'List comprehension: Elegant way to create lists'
pow2 = [2 ** x for x in range(10)]
print(pow2)

#which is equiv
for x in range(10):
    pow2.append(2 ** x)

#Different tuples - cannot be modified
myTuple = ()
print(myTuple)

myTuple = (1, 2, 3)
print(myTuple)

myTuple = (1, "Hello", 3.4)

myTuple = ([2, 3], 's')
print(myTuple)

# differentiating a tuple
myTuple = ('s')
print(myTuple)

myTuple = ('s', ) # a tuple
print(myTuple)


'''
Python dictionary unordered collection of items 
 '''
# json (Javascript )
myDict = {}

myDict = {1: 'apple', 2: "sss"}

myDict = {'name': 'John', 1: [1,2,43,4]}


#dict of tuples
myDict = dict([(1, 'apple'), (2, 'ball')])


# if statements
num = 10
if num > 0: 
    print("positive number")
else:
    print("negative number")    


# #iterables

word = "Giovanny"
for letter in word:
    print(letter) # each char...
    

words = ["Gio", "vanny"]
for word in words:
    print(word) # each element...

# nested 
for word in words: 
    print("Element: " + word) # element
    for letter in word:
        print(letter) # each char of word

for x in range (3):
    print(x)

for n in range(1, 10, 3):
    print(n)


newList = []
fruits = ["apple", "melon"]
for x in fruits:
    if 'a' in x:
        newList.append(x)


i = 5
n = 10
while i <= n:
    print(i)
    i += 1

while i <= n:
    print(i)
    i += 1
else:
    print("done")
