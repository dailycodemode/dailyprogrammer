def countUp(n):
    print(n)
    print(n+1)
    countUp(n+2)


countUp(1)

# ANSWER by school_throwaway
print(range(1, 1001))

# BREAKDOWN
# What I have done is call a function within itself. If I remove the third line and
# call itself with just a single +1 iteration then it will crash prior to getting to
# a thousand. Instead I iterate by value of 2 and have it print of the other two.
#
# SUMMARY
# The answer is certainly easier however using the answer is an implicit loop and
# defeats the point of the question. Other answers either did similar to my own,
# did not work or were the same as the answer.

