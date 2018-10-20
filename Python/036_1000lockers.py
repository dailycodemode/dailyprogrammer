# Answer by DAILY CODE MODE
lockers = [True for x in range(1000)]

counter = 1

for student in range(1, 1001):
    for switch in range(1, 1001):
        if switch*counter < 1001:
            print(switch, counter, switch * counter)
            if lockers[switch * counter -1] is True and switch*counter < 1001:
                lockers[switch * counter - 1] = False
            elif lockers[switch * counter - 1] is False and switch*counter < 1001:
                lockers[switch * counter - 1] = True
    counter += 1
print(sum(lockers))


# Answer by Ttl
a = [False]*1000
for i in range(1,1000):
    for j in range(0,1000,i):
        a[j]=not a[j]
print([i for i,j in enumerate(a) if j][1:])
print(a[-1])
# BREAKDOWN
a = [False]*1000
# This is a fab way of creating a list of one thing.
for j in range(0,1000,i):
    pass
# What is happening here is that he is creating the steps of how to move
# in the for loop where i will be what number the student is at
a[j]=not a[j]
# This simply reverses the boolean at that index

[i for i,j in enumerate(a) if j][1:]
# the piece at the end just gets rid of the first entry however I don't
# fully understand why you would do this seeing as there are 1000 lockers
# and to eliminate the first entry removes the first entry

# The rest is creating a list which returns the location of the values
# instead of the values themselves.

# SUMMARY
# A brilliant piece of code which outperforms mine in every aspect. I'll
# be watching out for Ttl in future. As a side note, there is a mathematical
# method of getting this answer quickly which you can check out for yourself.
