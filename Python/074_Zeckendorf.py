# DAILY CODE MODE
# def is_prime(a):
#     return all(a % i for i in range(2, a))
#
# def zeckendorf(num):
#     answer = []
#     temp = num - 1
#     while num > 0:
#         if is_prime(temp):
#             number = num - temp
#             answer.append(temp)
#             temp = num
#         else:
#             temp -= 1
#     return answer
#
# print(zeckendorf(11))
#
# Answer by Frustrate
# def zeckendorf(num):
#     # Generate the fibonacci sequence up to num
#     fib = [0,1]
#     while fib[-1] < num:
#         fib.append(fib[-1] + fib[-2])
#
#     found = []
#
#     while sum(found) < num:
#         found.append(max([x for x in fib if x <= num - sum(found)]))
#
#     return found
#
# print(zeckendorf(3**15))
#
# BREAKDOWN
# fib = [0, 1]
# while fib[-1] < num:
#     fib.append(fib[-1] + fib[-2])
#
# This is a pretty nice way of creating the fibinacci sequence by simply adding all the values to eachother.
#
# x in fib if x <= num - sum(found)]))
# x is only allowed to go as far the number. The max functiono is then bringing back the last number however this could have just as easily been done by returning the last value.
#
# SUMMARY
# Lovely answer by Frustrate