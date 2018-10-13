# # Answer by DAILY CODE MODE
# ABACABA = ""
# for letter in [chr(x) for x in range(65, 65+26)]:
#     ABACABA = ABACABA + letter + ABACABA
#
#
# # Answer by loonybean
# def getSequence(n):
#     if n == 1:
#         return 'a'
#     t = getSequence(n-1)
#     return t + chr(96+n) + t
#
# def sequenceFun():
#     f = open('output123.txt','w')
#     f.write(getSequence(26))
#     f.close()
#
# sequenceFun()
#
# BREAKDOWN
# def sequenceFun():
#     f = open('output123.txt','w')
#     f.write(getSequence(4))
#     f.close()
#
# We create a file here as printing off to the debugging screen is time consuming so instead, we create a file, create the sequence and pop it in before closing it. When I ran my answer it took about .9s however if we run it using the answer 1 method
# However when I do this with my own file there seems to be decrease in perfromance so I'm wondering is the errason that people write to a file is so that thye can actually look at the thing.
#
#
# Summary
# I gave two answers to this because I wanted a good example of recursive programmig and why I don't like it. If you look at answer 1, the answer is all contained in getSequencece
# which gets passed in a number, checks if its not zero and then keeps on calling itself until it gets to zero. When it does it will return the letter along with its wrapper
# I believe this is a good example of why recursion can be really very tricky because when we are taught it initially it makes sense however it can be very difficult to follow as we have just seen in the above example which is essentially still a very basic recursioin algorithim.
#
# However the point of this whole blog is to become a better programmer so whenever I see these type of answers I like to go through them because as I always say in programming. Nothing in programming is difficult if you have practiced it a few times
