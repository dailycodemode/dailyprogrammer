# # Answer by DAILY CODE MODE
# def print_a_triangle(limit):
#     triangle_range = range(1, limit + 1)
#
#     end = 1
#     while len(triangle_range)>0:
#         cut = triangle_range[:end]
#         triangle_range = triangle_range[end:]
#         end += 1
#         for x in cut:
#             print(x, end = " ")
#         print("")
#
# # ANSWER by Should_I_say_this
# def triangle(n):
#     totalnumbers=0
#     lastrow=1
#     for i in range(1,n):
#         if totalnumbers+i<=n:
#             totalnumbers+=i
#             lastrow=i
#         else:
#             break
#     while lastrow >0:
#         for i in range(totalnumbers-lastrow+1,totalnumbers+1):
#             print(i,end =' ')
#         totalnumbers -=lastrow
#         lastrow -= 1
#         print('')
#
# # Summary
# # I think this is a good example in the answer when it
# # is a good time to use a while loop instead of a for loop.
# # When I originally attempted this, I provided a very
# # similar answer to the given answer and we both ran into
# # the same problem- 'What to do if your number is too short
# # or too long. What the answer does is the least preferable
# # way, in # that if a certain condition is met then he will
# # break out of the for loop. The problem with doing this is
# # that it can lead to unforseen behaviours, looks a little
# # messy and is usually not the best way of doing things
# # because you may not have been able to think of a better
# # answer. One thing that I could have done better is rename
# # my variables. End should be probably either be i or step.