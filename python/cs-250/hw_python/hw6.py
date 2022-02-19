# cullyn newman
# CS 250
# homework 6
# Permutations and combinations

# In this homework I want to look at combinitorial algorithms
# Also known as brute force algorithms.
# This class of algorithms is incredibly powerful,
# but also very, very slow.
# So, they're important to know, but we usually want to avoid them.

# We'll start simple (well, that's kind of relative).
# I want to increase a binary number by 1.
# I've represented a binary number as a list of digits
# [1,0,1,0] is 10
# [1,0,0,0] is 8
# [1,0,1] is 5
# I want you to write a function to increment a number
# so binInc([1,0,1]) should return [1,1,0]
# so binInc([1,1,1]) should return [1,0,0,0]
# and so on.
# Two things to think about
# 1. What is your stoping condition?
# 2. What do you do in a number is all 1's?
# 3. We read numbers backwards so num[0] is going to be the most siginificant bit.
#    That means you probably want to start at len(num)-1 and work backwards.
#
# you can use list.insert(pos, elem) to insert an element into a list at a position


def binInc(num):
    carry = False
    for i in range(len(num) - 1, -1, -1):
        if num[i] == 1:
            num[i] = 0
            carry = True
        else:
            num[i] = 1
            carry = False
            break
    if carry:
        num.insert(0, 1)
    return num


print(binInc([1, 0, 1]) == [1, 1, 0])
print(binInc([0, 0, 1]) == [0, 1, 0])
print(binInc([1, 1, 1]) == [1, 0, 0, 0])
print(binInc([1, 0, 1, 1, 1]) == [1, 1, 0, 0, 0])
print(binInc([1, 1, 1, 1, 1]) == [1, 0, 0, 0, 0, 0])
print("-" * 79)

# Now, we can repeat the process with base 10 numbers.
# This is going to be very similar to base 2 numbers.
# But this time we represent a number with the digits 0 through 9
# 1024 is [1,0,2,4]
def decInc(num):
    carry = False
    for i in range(len(num) - 1, -1, -1):
        if num[i] == 9:
            num[i] = 0
            carry = True
        else:
            num[i] += 1
            carry = False
            break
    if carry:
        num.insert(0, 1)
    return num


print(decInc([0]) == [1])
print(decInc([1]) == [2])
print(decInc([9]) == [1, 0])
print(decInc([9, 9]) == [1, 0, 0])
print(decInc([9, 9, 9]) == [1, 0, 0, 0])
print(decInc([4, 2, 0]) == [4, 2, 1])
print(decInc([1, 0, 2, 9]) == [1, 0, 3, 0])
print(decInc([6, 9]) == [7, 0])
print(decInc([0, 0, 9]) == [0, 1, 0])
print(decInc([1, 9, 9]) == [2, 0, 0])
print("-" * 79)

# now use the decInc function to print out all two digit numbers.
# they can have leading 0s.
def printNums():
    num = [0, 0]
    while len(num) < 3:
        print(num)
        decInc(num)


# printNums()

# next we want to find a way to print out all combinations.
# We'll just do the combinations for numbers in the set [0,1,...n-1] for now,
# but this can easily generalize to combinations of any set.

# I've given you the combs function, so combs(n,k) should return all of the
# combinations of length k form the numbers [0...n-1].
# but this function, just calls a recursive helper function.
# That's where you come in.


def combs(n, k):
    combsRec(n, k, [], 0)


# in this helper function, we want to break down what a combination is.
# and we want some way to get the "next" one.
#
# We add 2 new parameters
# first comb is the current combination we've seen
# second s is the start number, it's the first number we haven't used in the combination yet.
#
# This give use our two cases.
# if the length of comb is k, then we've found a combination, and we can print.
# if the length of comb is less than k
# then for each number we haven't see in the combination yet,
# add that number to our combination,
# and recursively call comb_rec.
# for example: if we call comb(7,4,[1,2,3],4),
# then our recursive calls would be:
#   comb(7,4,[1,2,3,4],5)
#   comb(7,4,[1,2,3,5],6)
#   comb(7,4,[1,2,3,6],7)
#
# You can add an element i to the end of a list comb with the syntax
# comb+[i]


def combsRec(n, k, comb, s):
    if len(comb) == k:
        print(comb)
        return


# I really don't know what this problem is asking me to do.

# Finally, we can look at permuting a list.
# We're going to use a fact from group theory to solve the problem.
# That is, any permutation can be broken down into a series of swapped elements.
# for example the permutation [2,3,1] is [1,2,3] where we swapped (1,2), then we swapped (1,3).
# Since every permutation can be broken down to a sequence of swaps,
# if we can find all of the swaps, then we can generate all permutations.
# This is Heap's algorithm.
#
# permute has 2 parameters
# a is the list we're permuting
# i is the current index we're looking at.
# if i is the length of the list, we're done, and we print the list.
# otherwise, for each j to the end of the list:
#   swap the elements at i and j
#   permute the list at index i+1
#   swap the elements back
def permute(a, i):
    if i == len(a):
        print(a)
        return

    for j in range(i + 1):
        a[i], a[j] = a[j], a[i]
        permute(a, i + 1)
        a[j], a[i] = a[i], a[j]


permute([1, 2, 3, 4], 0)
