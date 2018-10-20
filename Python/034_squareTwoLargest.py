# https://www.reddit.com/r/dailyprogrammer/comments/rmmn8/3312012_challenge_34_easy/

# DAILY CODE MODE
def square_two_largest(list):
    list.sort(reverse=True)
    return list[0] ** 2 + list[1] ** 2

print(square_two_largest([3,1,2]))

# ANSWER BY Should_I_say_this
def sumsq(a,b,c):
    l=[a,b,c]
    del l[l.index(min(l))]
    return sum(i**2 for i in l)

# BREAKDOWN
# del l[l.index(min(l))]
# Answer has chosen to eliminate the lowest number from the list to be only left with two arguments

sum(i**2 for i in l)
# He then squares everything in the list and then returns the value

# Comment
# Not the greatest fan of the answer provided because it can only ever be used for this scenario where
# three arguments are given and the sum of the two highest is returned.

# With my answer, it doesn't matter the size of the list.
# I should not that I should the questions a little more carefully because it asked for three arguments.
# Not three arguements contained within a list.