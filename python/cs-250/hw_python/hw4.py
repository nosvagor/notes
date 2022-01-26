# ┬ ┬┌─┐┌┬┐┌─┐┬ ┬┌─┐┬─┐┬┌─  ┌─┐┌─┐┬ ┬┬─┐
# ├─┤│ ││││├┤ ││││ │├┬┘├┴┐  ├┤ │ ││ │├┬┘
# ┴ ┴└─┘┴ ┴└─┘└┴┘└─┘┴└─┴ ┴  └  └─┘└─┘┴└─
###### introduction to algorithms ######
# cullyn newman
# CS: 250

# Here's the part of the class where we finally get to talking about code.
# So far I haven't assumed any knowledge of how to program,
# but we're going to need at least a little bit to apply concepts in class.

# Why are we doing this when talking about proofs?
# Writing a programs is a lot like writing a math proof.
# We need to break down the problems,
# and work out step by step how to solve it,
# and then explain the steps
#
# In fact, there's an entire area of CS devoted to automatic theorem proving.
# The theorems are types in a programming language
# and the proofs are programs in that language.

# so let's look at programming in Python.
# most of you will already know this.

##################################
# Operators
##################################

# We can use python like a calculator
# There are several operators we can use
# They're generally split into three classes
# arithmetic operators work on numbers
# boolean operators work on the boolean values True and False.
# comparison operators work on most any type of data, and return boolean values.

# Arithmetic operators:
# We have the operators +, -, *, /, and ** from hw1.
# We also have the % operator for modulus.

# comparison operators:
# a == b a and b are equal
# a != b a and b are not equal
# a < b a is less than b
# a > b a is greater than b
# a <= b a is less than or equal to b
# a >= b a is greater than or equal to b


# boolean operators: also from homework 1
# a and b
# a or b
# not a

##################################
# Variables and Assignment
##################################
# We can make a variable with
# name = expression
# for example
x = 2 * 3 + 6
# Now the name x has the value 12
print("x =", x)

# unlike variables in math, we can change the definition of x at any time
x = 13
print("x =", x)


##################################
# IF Statements
##################################

# If statements let us choose between two branches
# in python an if statement doesn't need parentheses
# but it does need a colon
# and everything after the if statement must be tabbed in
# It's an error in python if you have bad formatting.

# if boolean expression:
#     true branch
# else:
#     false branch

if x < 10:
    print("x is less than 10")
else:
    print("x is greater than or equal to 10")

##################################
# WHILE loops
##################################

# We can also repeat things in Python.
# the syntax is
# while boolean expression:
#    loop body
#
# Again, you need to indent the loop body
# otherwise it's an error.
#
# Usually we use a loop to count things
i = 0
while i < 10:
    print("i =", i)
    i = i + 1

# The last line is called an increment.
# It's a little weird to have i on both sides of an assignment
# i = i + 1
# If i is 0 when we get to this line,
# then i = 0 + 1, so i is now 1.
# if i = 1 when we get to the line,
# then i = 1 + 1, so i is now 2.
# We're just adding 1 to the current value of i.

# but we can do more than just increment i
# we can also keep a running total of something
# 2^n = 2 * 2 * 2 ... 2, n times.
# We can compute this with a loop
def twoToThe(n):
    total = 1
    i = 0
    while i < n:
        total = total * 2
        i = i + 1
    return total


##################################
# problems
##################################

# problem 1:
# Write a function to compute the division algorithm
# That is, assume a >= b
# return a q and r such that a = qb + r
def division(a, b):
    q = 0
    r = 0
    return (q, r)


# Problem 2:
# write a function that returns True if a | b
# you can use problem 1 for this, but you don't need to.
def divides(a, b):
    return False


# problem 3: factorial
# the factorial function multiplies all of the numbers between 1 and n.
# We write it as n!
# n! = 1 * 2 * 3 * 4 ... n
# Write a function to compute n!
# Since you don't know how big n is, you're going to need to use a loop.
# You should keep track of your running total.
def factorial(n):
    return 1


# Problem 4: euclids algorithm
# The greatest common divisor, gcd(a,b)
# is the largest number that divides both a and b
# In the written part of the homework you showed
# if a >= b, then gcd(a,b) = gcd(b,a%b)
# You can also verify that if b|a, then gcd(a,b) = b
# So, we can compute gcd(a,b) be repeatedly moding the numbers.
# example:
# gcd(135,117)
# = gcd(117,18)
# = gcd(18,9)
# = 9 because 9 | 18
#
# write a function to compute gad, you can assume a > b.
def gcd(a, b):
    return 1
