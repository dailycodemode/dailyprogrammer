# DAILY CODE MODE
import random

array = [1, 2, 4, 5, 6, -7, 3, 5, 4, 3, 8]
window = 3

i = random.randint(0,len(array) - window)

print(sum([x for x in array[i:i+window] if x > 0]))


# Answer by ashashwat
def max_subarray(A):
    max_so_far = max_ending_here = lo = hi = 0
    for y,x in enumerate(A):
        if x > max_ending_here + x:
            max_ending_here, lo = x, y
        else:
           max_ending_here += x
        if max_ending_here > max_so_far:
           max_so_far, hi = max_ending_here, y
    return (A[lo:hi + 1], max_so_far)


lst = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
print(max_subarray(lst))

# BREAKDOWN
# What the answer is doing is looping through each number and then checking if the sum of it and the previous versions is greater than the current number. If it is then it sets to this number and if not then it gets added on. I'm really not sure why this is happening because whenever the answer encounters a negative numbre then it resets the chain
# and so it seems it is just returning the highest sequence of numbers in the array.
#
# SUMMARY
# Perhaps my solution isn't what the question was asking but I feel that it was the quickest answer possible.
#
# We are taking a look at the given answer just to see what he was trying to achieve.
#
#
