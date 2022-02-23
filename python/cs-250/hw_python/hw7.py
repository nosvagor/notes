from random import randint, seed, shuffle
from time import time

# This time I thought we'd take a different approach with the python portion.
# Last week we were really in the weeds with recursion.
# This week, you don't need to write anything.
# We're just running programs.

# We're going to take a different approach to algorithms.
# Instead of trying to understant everything mathmematically,
# I thought we'd actually try some science in the computer science course.
# This will also give you some good intuition on what complexity classes actually mean.


# Ok, so we saw that there were several standard complexity classes.
# I want to see if we can determine these without actually looking at the algorithm.

# Here's how we do it.  I'm going to give you five functions.
# for each functions that each depend on a parameter n.
# n will be the input size for the function.
# I want you to
#  1. find a value for n0 where f(n0) takes about a second
#      Each function will print our how much time it takes to run.
#  2. now run f(2*n0), f(3*n0) f(4*n0) ... until you can establish a pattern.
#      2.5 for example if the function is linear we'd expect f(2*n0) to be roughly 2 seconds.
#  3. graph these points, and try to match it to a function.
#      This isn't exact, since we're only graphing a few points, but you can get an idea.
#  4. make a guess at the complexity class
#      Your options are
#        logrithmic
#        linear
#        polinomial
#        exponential
#        factorial
#  5. sort the function based on their complexity class.
#


#######################################
# Helper functions (don't test these)
#######################################


def randList(n):
    seed(3326489)
    l = list(range(n))
    shuffle(l)
    return l


def randSortedList(n):
    seed(3326489)
    l = np.arange(n)
    l[0] = randint(0, 10)
    for i in range(n - 1):
        l[i] = l[i - 1] + randint(0, 10)
    return l


def perms(a, i):
    if len(a) == i:
        yield a
    for j in range(i, len(a)):
        a[i], a[j] = a[j], a[i]
        yield from perms(a, i + 1)
        a[i], a[j] = a[j], a[i]


def sorted(l):
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            return False
    return True


def safe(a, i, j):
    issafe = True
    for k in range(i):
        issafe = issafe and j != a[k] and abs(j - a[k]) != i - k
    return issafe


def rec(n, a, r, c):
    a[r] = c
    if c == n:
        return 0
    count = 0
    if r < n - 1:
        if safe(a, r, c):
            count = rec(n, a, r + 1, 0)
    else:
        if safe(a, r, c):
            count = 1
    return count + rec(n, a, r, c + 1)


###################
# Test functions
###################


def f1(n):
    l = randList(n)
    startTime = time()
    for p in perms(l, 0):
        if sorted(p):
            break
    endTime = time()
    print("%d seconds", endTime - startTime)


def f2(n):
    startTime = time()
    i = 1
    while 2 ** i < n:
        i += 1
    endTime = time()
    print("%d seconds", endTime - startTime)


def f3(n):
    l = randList(n)
    startTime = time()
    for i in range(n):
        minj = i
        for j in range(i + 1, n):
            if l[j] < l[minj]:
                minj = j
        l[i], l[minj] = l[minj], l[i]
    endTime = time()
    print("%d seconds", endTime - startTime)


def f4(n):
    l = randList(n)
    startTime = time()
    mini = 0
    for i in range(n):
        if l[i] < l[mini]:
            mini = i
    endTime = time()
    print("%d seconds", endTime - startTime)


def f5(n):
    a = [0] * n
    startTime = time()
    print(rec(n, a, 0, 0))
    endTime = time()
    print("%d seconds", endTime - startTime)
