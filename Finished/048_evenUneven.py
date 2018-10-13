# Answer by DAILY CODE MODE
def split_list_to_even_and_uneven(arr):
    even = []
    for unit in arr:
        if unit % 2 != 0 : even.append(unit)
        else: even.insert(0, unit)
    return even

# Answer by n1ncha
def paritypart(l):
    x1 = 0
    x2 = len(l)-1
    while x1 < x2:
        while l[x1]%2==0:
            x1+=1
        while l[x2]%2==1:
            x2-=1
        if x1<x2:
            t = l[x1]
            l[x1] = l[x2]
            l[x2] = t

# Breakdown
# The only thing that really jumps out at me is
        while l[x1]%2==0:
            x1+=1
        while l[x2]%2==1:
            x2-=1
# where the answerer is attempting to figure out where to put his answer.
# SO it works by looping until x1 is larger than x2 which can only happen when all
# the value have been
# The above piece just finds at what pointn the intersection of even
# to uneven happens and then lets x1 equal it and inserts it at position x2

# Summary
# My answer works fine but it's sloppy as it just splits the answer willy nilly.
# Thnking about it now, I should have just split them into two lists and then
# joined them together which would have been a lot more straight forward.
# The given answer is very impressive however it takes a longn time to
# figure out what it is trying to achieve and would take even longer without
# some additional comments.
