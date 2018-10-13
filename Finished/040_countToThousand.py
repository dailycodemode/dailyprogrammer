
# DAILY CODE MODE
def count(n):
    print(n)
    count(n+1)
print(1)
print(2)
count(3)

# i = 1; s = "print i; i += 1;"
# exec(1000 * s)

# Answer by orgelmorgel
print("\n".join(map(str, range(1,1001))))

# BREAKDOWN
map(str, range(1,1001))
# What map does is apply to a list of values. So in the above, all that is
# happening is that there is a list from 1 -> 1,000 and the function is str
# which means, make whatever is being accepted a string.
# Because it is a list, then is a good idea to return it as a list but that
# is not critical. In fact orgelmorgel has used the join function along with
# the \n operator to come up with a single string where each number (as a
# string) is on a new line.


# SUMMARY
# My answer will fail but not before getting to 1000 without calling a loop
# Unless what you consider a function calling itself a intrinsic loop

