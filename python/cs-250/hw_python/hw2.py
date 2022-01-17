# ┬ ┬┌─┐┌┬┐┌─┐┬ ┬┌─┐┬─┐┬┌─  ┌┬┐┬ ┬┌─┐
# ├─┤│ ││││├┤ ││││ │├┬┘├┴┐   │ ││││ │
# ┴ ┴└─┘┴ ┴└─┘└┴┘└─┘┴└─┴ ┴   ┴ └┴┘└─┘
# Due: 1/17/22
# Cullyn Newman
# CS: 250

# ┌─┐┌─┐┌┬┐┌─┐
# └─┐├┤  │ └─┐
# └─┘└─┘ ┴ └─┘
print("-" * 79, "\nSETS")
# In Python, we can make a set with curly braces
# example
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print("s1 =", s1)
print("s2 =", s2)

# This is nice and simple, It's just like our sets in class.
# Unfortunately there's one problem
# We can't write the empty set as {}
# We have to use set()
empty = set()

# We can ask the usual question about sets.
# A == B returns True if A and B are the same set
print("s1 == {1,2,2,3} is", s1 == {1, 2, 2, 3})
print("s1 == s2 is", s1 == s2)
# x in A returns True if x is an element of A
print("2 in s1 is", 2 in s1)
print("2 in s2 is", 2 in s2)
# A <= B returns True if A is a subset of B
print("{1,3} <= s1 is", {1, 3} in s1)
print("{1,3} <= s2 is", {1, 3} in s2)
# A | B is the union of A and B
# A & B is the intersection of A and B
print("s1 | s2 is", s1 | s2)
print("s1 & s2 is", s1 & s2)

# Notice that {1,2,2,3} == {1,2,3}
# Sets really do remove duplicate elements
print("-" * 79, "\n")


print("-" * 79, "\nSET BUILDING")
# We even have set builder notation
# Although, if you search for this online, it'll be called set comprehension.
# It actually looks pretty similar
# we could square all the numbers in s1 with {x^2 : x in s1}
# we just replace the : with for
s1Squared = {x ** 2 for x in s1}
print("{x**2 for x in s1} =", s1Squared)

# we can also use the range(a,b) function in Python
# to get the set of integer from a to, but not including, b.
# set(range(a,b)) = {a, a+1, a+2, ... b-2, b-1}

# For a technical reason, if we want the set of range, we need to use
# set(range(a,b)) instead of just range(a,b)
print("set(range(1,10)) is", set(range(1, 10)))

# So, I can use this to find the square of the set of numbers from 1 to 10
# remember, we need to go to 11, because range doesn't include the end point.
print("1 to 10 squared is", {x ** 2 for x in range(1, 11)})
# here we can just use range(a,b)
# so, it turns out set(range(a,b)) is just {x for x in range(a,b)}


# Oh, wait, look at the output
# What happened here?
# On my machine I got {64, 1, 4, 36, 100, 9, 16, 49, 81, 25}
# You may get something different.

# What went wrong here?
# It turns out nothing.
# Remember, sets are unordered.
# Python will sometimes reorder a set because its more efficient.
# We don't need to worry about why this is more efficient,
# but it is good to remember that sets aren't always sorted.

# We can build more complex set comprehensions using filters.
# Remember in class we had things {x : x in N and x < 20}
# we can do something similar in Python
lessThan20 = {x for x in range(1, 50) if x < 20}
print("{x for x in range(1,50) if x < 20} is", {x for x in range(1, 50) if x < 20})

print("-" * 79, "\n")
# That's about it for sets in Python, they're actually pretty handy

# ╔═╗╦═╗╔═╗╔╗ ╦  ╔═╗╔╦╗╔═╗
# ╠═╝╠╦╝║ ║╠╩╗║  ║╣ ║║║╚═╗
# ╩  ╩╚═╚═╝╚═╝╩═╝╚═╝╩ ╩╚═╝
print("-" * 79, "\nPROBLEMS")
# give a Python expression for the set of number from 1 to 20 (including 20)
n = 20
p1 = set(x for x in range(1, n + 1))
print("p1 =", p1)

# The function isEven(x) returns True if x is even
def isEven(x):
    return x % 2 == 0


# The function isOdd(x) returns True if x is odd
def isOdd(x):
    return not isEven(x)


# use these function to create a set of even numbers from 1 to 20
p2 = set(x for x in range(1, n + 1) if isEven(x))
print("evens =", p2)

# Now get the set of odd numbers between 1 and 20, and show that the
# intersection of even numbers and odd numbers is the empty set.
p3 = set(x for x in range(1, n + 1) if isOdd(x))
print(f"odds = {p3}")

# p4 = evens intersect odds
oddEvenIntersect = p2 & p3
print("odd even intersect == set() ->", oddEvenIntersect == set())
print("-" * 79)
