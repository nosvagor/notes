# ┌┬┐┌─┐┌┬┐┬ ┬  ┌─┐┌┐┌
# │││├─┤ │ ├─┤  ├┤ │││
# ┴ ┴┴ ┴ ┴ ┴ ┴  └  ┘└┘
# example math function
def f(x):
    return 3 * x + 4


# translate these functions written in math syntax into python syntax:

# g(x) = x^2 + 2x + 1
def g(x):
    return x ** 2 + 2 * x + 1


# h(x) = 2x^3 + 6x + 2
def h(x):
    return 2 * x ** 3 + 6 * x + 2


# ┬  ┌─┐┌─┐┬┌─┐  ┌─┐┌┐┌
# │  │ ││ ┬││    ├┤ │││
# ┴─┘└─┘└─┘┴└─┘  └  ┘└┘
# example logic function
def xor(a, b):
    return (a and not b) or (not a and b)


# write the following boolean functions using only and, or, and not:

# imp(a,b) = a -> b
def imp(a, b):
    return b if a else False


# eq(a,b) = a == b
def eq(a, b):
    return (a and b) or (not a and not b)


# ┬ ┬┬┌─┐┬ ┬┌─┐┬─┐  ┌─┐┬─┐┌┬┐┌─┐┬─┐  ┌─┐┌┐┌
# ├─┤││ ┬├─┤├┤ ├┬┘  │ │├┬┘ ││├┤ ├┬┘  ├┤ │││
# ┴ ┴┴└─┘┴ ┴└─┘┴└─  └─┘┴└──┴┘└─┘┴└─  └  ┘└┘
# example composition function
def comp(f, g):
    def h(x):
        return f(g(x))

    return h


# Making f^2 using f from above.
f2 = comp(f, f)

# now if we run f2(3) we get 43.
print(f2(3))

# That's the same thing we get if we run f(f(3))
print(f2(3) == f(f(3)))

# use comp to make g o h, using g and h you defined earlier.
goh = comp(g, h)

# verify that goh(6) = g(h(6))
print(goh(6) == g(h(6)))


# ┌─┐┌┐┌┌┬┐  ┌─┐┌─┐  ┌─┐┌─┐┌─┐┬┌─┐┌┐┌┌─┐┌┬┐┌┐┌┌┬┐
# ├┤ │││ ││  │ │├┤   ├─┤└─┐└─┐││ ┬│││├┤ ││││││ │
# └─┘┘└┘─┴┘  └─┘└    ┴ ┴└─┘└─┘┴└─┘┘└┘└─┘┴ ┴┘└┘ ┴
###############################################################################
# ┌─┐─┐ ┬┌┬┐┬─┐┌─┐
# ├┤ ┌┴┬┘ │ ├┬┘├─┤
# └─┘┴ └─ ┴ ┴└─┴ ┴


# we can define a function to take a derivative  in Python.
def deriv(f, x):
    return (f(x + 0.001) - f(x)) / 0.001


# then we can run deriv(g, 3) and we get about 8,
print(deriv(g, 3))
# which is g'(3).

# This isn't part of the assignment, just something to think about.
# How would you write a function to integrate f from a to b?
def integrate(f, a, b):
    return f(b) - f(a)


print(integrate(g, 1, 2))  # sort of close.... but not really.
