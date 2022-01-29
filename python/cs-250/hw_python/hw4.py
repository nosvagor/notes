# ┬ ┬┌─┐┌┬┐┌─┐┬ ┬┌─┐┬─┐┬┌─  ┌─┐┌─┐┬ ┬┬─┐
# ├─┤│ ││││├┤ ││││ │├┬┘├┴┐  ├┤ │ ││ │├┬┘
# ┴ ┴└─┘┴ ┴└─┘└┴┘└─┘┴└─┴ ┴  └  └─┘└─┘┴└─
###### introduction to algorithms ######
# cullyn newman
# CS: 250

import math


# problem 1:
# Write a function to compute the division algorithm
# That is, assume a >= b
# return q and r such that a = qb + r
def division(a, b):
    q = a // b
    r = a % b
    return (q, r)


# --- Question 1 --- #
print("\n" + "-" * 42)
print("Question 1:\n")
a = 6
b = 6
q, r = division(a, b)
print(f"a,b = {a,b}\nq = {q}, r = {r}")
print(f"a == qb + r -> {a == q * b + r}")
print("-" * 42)


# Problem 2:
# write a function that returns True if a | b
# you can use problem 1 for this, but you don't need to.
def divides(a, b):
    return True if (a % b == 0) else False


# --- Question 2 --- #
print("\n" + "-" * 42)
print("Question 2:\n")

print(f"a divides b -> {divides(a, b)}")

print("-" * 42)


# problem 3: factorial
# the factorial function multiplies all of the numbers between 1 and n.
# We write it as n!
# n! = 1 * 2 * 3 * 4 ... n
# Write a function to compute n!
# Since you don't know how big n is, you're going to need to use a loop.
# You should keep track of your running total.
def factorial(n):
    return 1 if (n == 1) else n * factorial(n - 1)


# --- Question 3 --- #
print("\n" + "-" * 42)
print("Question 3:\n")
n = 9

print(f"n! = {factorial(n)}")

print(f"factorial(n) = math.factorial(n) -> {factorial(n) == math.factorial(n)}")
print("-" * 42)


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
    q, r = division(a, b)
    return b if r == 0 else gcd(a, r)


# --- Question 4 --- #
print("\n" + "-" * 42)
print("Question 4:\n")

a, b = 135, 117
print(gcd(135, 117))

print(f"gcd(a,b) = math.gcd(a,b) -> {gcd(a,b) == math.gcd(a,b)}")
print("-" * 42)
