primes = []

for x in range(2,2000):
    for y in primes:
        if x%y == 0:
            break
    else:
        primes.append(x)

print(primes)

# print([i for i in range(2,2001) if all(i%c for c in range(2,i))])

# BREAKDOWN
# there are a few pieces that need to be looked at before we can look at the overall larger piece

# print([i for i in range(2,2001) if all(i%c for c in range(2,i))])
#
# #  So this type of line has been confusing me lately during this journey but i think i have it figured out
# # when you put
#
list = [range(10)]
# #  so what is happening here is that for these list one liners, the i for range(10) is iterating and then the first is the answer
#
# all()
# returns true only if an iterable return true

# so what is happening is that c will go from the number in question all the way up to one number before it
# if any number is divisible into

# i%c for c in range(2,i)

print(list)