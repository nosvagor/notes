# CS 250
# homework 3: relations and partial orders


# today we're going to look at relations.
# In class I said that we usually use relations for documentation.
# So, let's look at what that mean,
# and what happens when that goes wrong.
#
# We'll be looking at an idea called the topological sort.
# The code for it is defined below.
# You don't need to understand it, we're just going to call it.
def topsort(lst, lteq):
    indegree = {}
    out = []

    # loop through all pairs of elements in the list
    # and compute the in-degree for each element
    for x in lst:
        indegree[x] = 0
        for y in lst:
            if lteq(x,y):
                indegree[x] += 1
        # if the in-degree is 1
        # then there is no y such that x <= y
        # so x can go at the front of our list
        # remember: x <= x so indegree will always be at least 1
        if indegree[x] == 1:
            out.append(x)

    # now pick any item x with an in-degree of 1
    # and we'll "remove" this item from the list.
    # Just loop through every y in the list,
    # and if y <= x we decrement the indegree counter.
    #
    # if y now has an in-degree of 1, then we add it to the output list.
    for i in range(len(lst)):
        for l in lst:
            if lteq(l, out[i]) and indegree[l] > 1:
                indegree[l] -= 1
                if indegree[l] == 1:
                    out.append(l)

    # remember we started with the biggest thing, so we need to reverse the list
    return list(reversed(out))
# end of topsort

# This topological sort is a more general version of
# the sorting we all know and love...
# know and tolerate?...
# know and despise... Yeah... that feels right.
# anyway, now we have a new way of sorting things.

# So, how do we call topsort?
# It takes 2 parameters
# lst is a list
# lteq is a "comparitor"
# This means that lteq is a function that returns true if x <= y
# let's look at an example
def numberLteq(x, y):
    return x <= y

sortedNumbers = topsort([1,3,2,4,5], numberLteq)

# going back to week 1, this means that topsort is a higher order function
# because we passed a funciton in as the argument.

# That's cool, I have an inefficient complicated way to sort things.  yay?
# What makes topsort different?
#
# usually, sorting requires us to have a total ordering.
# That means that for every x and y in our set we have
# x < y or y < x or x == y.
# For numbers this is true.
# and in fact, this is true for a lot of things we run into,
# like booleans or strings,
# but it's not always true.

# Let's say you're making a game,
# and the players in your game have two stats # speed and strength.
# It might be useful to compare players.
# we can represent these players as a tuple (speed, strength)
# so (3,4) has a speed of 3 and a strength of 4.
# If two players have the same speed, but player 1 is stronger,
# then player 1 is probably the better player.
# so, we could say player 1 >= player 2.
# But what if player 1 has a higher strength and player 2 has higher speed?
# Then it's not really clear.
#
# We say these players are "incomparible"
# So we can make a comparison for players
def playerLteq(player1, player2):
    (speed1,strength1) = player1
    (speed2,strength2) = player2
    return speed1 <= speed2 and strength1 <= strength2

# You can test this out
# playerLteq((3,3), (3,5)) is True
# playerLteq((3,3), (2,2)) is False but playerLteq((2,2), (3,3)) is True
# playerLteq((3,3), (2,5)) is False and playerLteq((2,5), (3,3)) is False

# What happens when I try to sort the following players?
topsort([(1,1), (2,2), (1,2), (2,1)], playerLteq)

# Interesting It makes sense that (1,1) is first, and (2,2) is last
# but what about the other two? Well it doesn't really matter.
# We can look at this graphically
#      (2,2)
#     /     \
#    /       \
# (1,2)     (2,1)
#    \       /
#     \     /
#      (1,1)
# (1,2) and (2,1) are incomparible, so it doesn't matter which order they go in.

# Ok, but what does this have to do with relations?
# in topsort lteq is a function that takes two elements of the list
# and returns True or False.
# lteq is a relation: x ~ y if lteq(x,y)
# In fact, lteq is a special relation
# for topsort to work we need it to be
# * reflexive
# * antisymmetric
# * transitive
#
# That's right, lteq is a partial order.
# Here's the point.  We can sort any list as long as we have a partial order.
# but it's up to the programmer to make sure that lteq is a partial order.


# problems
# 1. What goes wrong with the following function?
#    What property are we missing?
def badLteq(x, y):
    return x < y

# topsort([1,2,3,4,5], badLteq)

# 2. Is the relation a partial order?
#    If not, what property is missing
#    if it is, What's going on with our call?
def eq(x, y):
    return x == y

# topsort([3,2,1,5,4], eq)


# 3. one parital order we'll talk about is divides on natrual numbers.
#    a divides b iff b % a == 0
#    Fill in the divides function, and check the results
def divides(a,b):
    return False

# topsort([64,8,16,2,32,128,4], divides)
# topsort([2,3,6,12,8,9], divides)

# 4. In python we can test for substrings with "in"
#    so "ham" in "hamburger" is True and "dent" in "student" is True.
#    substring is a partial order, but proving it is kind of technical.
#    (Hint: if s is a substring of w, then we can break w up into b+s+e for two string b and e)
#    Anyway, that means we can use substring in topsort

def substring(s, w):
    return False

# topsort(["speed","of","art","speedofart","speedo","fart"], substring)
# This is a really good example of why checking for substrings is important.
