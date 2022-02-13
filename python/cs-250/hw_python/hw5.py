# CS 250
# homework 5: Recursion
# cullyn newman

# If we're going to talk about inducting,
# then we really need to talk about recursion.
# Fundamentally they're really the same thing.

# Let's work on some recursive functions.

# First we'll start of with the hello world of recursion.
# The factorial function n! is just multiplying the numbers from 1 to n
# n! = 1 * 2 * 3 ... n
# but we can write this function recursively.
# give a recursive definition
def fac(n):
    return 1 if (n == 1) else n * fac(n - 1)


print(fac(3))

# The fibbonacci numbers are an interesting sequence of numbers.
# the sequence is
# 1, 1, 2, 3, 5, 8, 13, 21, ...
# We start with two 1s, and each term of the sequence is
# created by adding the two previous terms
# so 5 = 3 + 2, 8 = 3 + 5 and so on.
# give a recursive definition for a function that calculated
# the nth fibbonacci number.
# so fib(1) = 1, fib(2) = 1, fib(3) = 2 and so on.
# What's different about the base case here?
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)


for i in range(1, 10):
    print(fib(i))

# we can also do recursion with sequences.
# In python we use a list instead of a sequence.
# In C/C++ we would call this an array.
# It's the same concept.
# we can make a new list with
a = [1, 2, 3, 4, 5]
# Then instead of a_1, we write a[i] to get the ith element of a.
# The difference is that we start at 0
# so a[0] is the first element
# a[1] is the second element and so on.

# We usually use for loops when working with lists,
# but we can use recursion just as well.
# for example, suppose I want to add all of the elements in a list.
# If n is the length of a, then the sum is
# sum(a,n) = a[0] + a[1] + a[2] + ... a[n-1]
# remember, we start counting at 0, so we stop at n-1.
# but we can rewrite this as
# (a[0] + a[1] + a[2] + ... a[n-2]) + a[n-1]
# = sum(a,n-1) + a[n])
#
# We can write this recursively
def sumList(a, n):
    if i < 0:
        return 0
    else:
        return sum(a, n - 1) + a[n]


# we can sum all of the elements with sum(a,len(a))

# We can use this to write more interesting function.
# First, a palindrome is a list that's the same forwards as backwards.
# "tacocat" is a palindrome because if I reverse it, I get the same word.
# so I could solve that with
# palindrome(list): return reverse(list) == list
# But I can also solve this recursively.
# But we'll have to be careful about how we do it.
# take a look at the first and last character.
# What do you notice?
# use this observation to write a recursive definition for a palindrome.
# I should be able to call panindrome(a,0,len(a)-1)
def palendrome(a, i, j):
    if j == 0:
        return True

    if i == j:
        return True

    if a[i] != a[j]:
        return False

    return palendrome(a, i + 1, j - 1)


a = list("tacocat")
a1 = list("hannah")
a2 = list("asetteasasetteas")
a3 = list("helloworld")
print(palendrome(a, 0, len(a) - 1))
print(palendrome(a1, 0, len(a1) - 1))
print(palendrome(a2, 0, len(a2) - 1))
print(palendrome(a3, 0, len(a3) - 1))

# Finally We should look at a recursive data structure.
# If you haven't seen data structures before, that's fine.
# You're honestly probably going to be less confused that the people who took 163.
#
# We're going to look at an "inductively defined data structure".
# All this means is that we're defining a data structure in terms of itself.
# In this case we want to make a sqequence data structure that we access in order.
# so we have a_1 -> a_2 -> a_3 ... a_n.
# we define the sequence with a class
class Seq:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    def __repr__(self):
        if self.tail == None:
            return str(self.head) + " -> !"
        else:
            return str(self.head) + " -> " + repr(self.tail)


# You only need to know 3 things about classes for this part.
# 1. We can create a sequence with the Seq() function (this is called a constructor).
# 2. if we make a sequence s, then we can get the first element with s.head
# 3. We can get the sequence without the first element with s.tail
#
# This is the sequence for [1,2,3,4,5]
testSequence = Seq(1, Seq(2, Seq(3, Seq(4, Seq(5, None)))))
# We can print out the first element, and we get 1
print("first element of testSequence:", testSequence.head)
# We can print out the third element, and we get 3
print("third element of testSequence:", testSequence.tail.tail.head)
print("you can print out the whole sequence", testSequence)
#
# Mathematically we define a Sequence as
# A sequence is either empty (with the value None)
# Or a sequence has a head, which is an integer, and a tail, which is a sequence.

# This is an inductive definition, because the tail is also a sequence.
# Inductive definitions are nice, because they work really well with recursion.
# If I want to add all of the number of my sequence, I just look at the two possible cases
# addSeq(None) = 0
# addSeq(Seq(head,tail)) = head + addSeq(tail)
# Unfortunately python doesn't let us define recursive function with equations like this
# but we can definen it in python with an if statement
def addSequence(s):
    if s == None:
        return 0
    else:
        return s.head + s.tail


# We can also make sequences with recursion.
# Suppose I want to make a sequence of integers between m and n
# so I want Seq(m, Seq(m+1, Seq(m+2 ... Seq(n,None) ... ) ) )
# We can do this with recursion too
# if m > n, then there's no sequence to make
# if m <= n, then we want a sequence starting with m.
def makeSeq(m, n):
    if m > n:
        return None
    else:
        return Seq(m, makeSeq(m + 1, n))


# I can also make new sequences out of old ones.
# For example, I can append two sequences
# Appending two sequences is pretty easy.
# If a is empty, then it's just b
# If a has an element, then that element is the head of the new sequence.
# append(None, b) = b
# append(Seq(head,tail), b) = Seq(head, append(tail,b))
def append(a, b):
    if a == None:
        return b
    else:
        return Seq(a.head, append(a.tail, b))


# here's where you come in.
# I want to reverse a sequence.
# I know a couple of things about reverse.
# When I reverse a sequence, it's first element now comes at the end.
#
# Step 1. come up with a recursive equation for reversing a sequence
# reverse(None) = ???
# reverse(Seq(head,tail)) = Seq(tail,head))
#
# Step 2. implement reverse in python
def reverse(s):
    if s.head == None:
        return Seq(s.tail, s.head)

    return reverse(Seq(s.tail, s.head))


print(reverse(testSequence))
