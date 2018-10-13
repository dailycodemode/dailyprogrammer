# DAILY CODE MODE
# def checkDigit(id_num):
#     total = 0
#     toDouble = False
#     for i in reversed(range(len(id_num))):
#         if toDouble == False:
#             total += int(id_num[i])
#             toDouble = True
#         else:
#             total += int(id_num[i])*2
#             toDouble = False
#     print(total)
#     return 10 - int(str(total)[-1])
#
# def checkNum(id_num):
#      if((id_num[:len(id_num) -1])) == int(id_num[-1]):
#          return True
#      else:
#          return False
#
# Answer by Cosmologicon
# dig = lambda d, a: d + a * (d + d // 5)
# luhn = lambda n, a: n and luhn(n // 10, 1 - a) + dig(n % 10, a)
# isvalid = lambda n: luhn(n, 0) % 10 == 0
# getcheckdigit = lambda n: -luhn(n, 1) % 10
#
# print(isvalid(49927398716))
# print(getcheckdigit(4992739871))
#
# BREAKDOWN
# dig = lambda d, a: d + a * (d + d // 5)
# # The dig lambda function brings back d or 2d values below zero and then 2d+1 values if it is 5 or higher.
#
# I don't really understand what is happening with the luhn part. When it gets down to the n being 0, the code will terminate however I don;t see why this should be the case?
# Also, I've never seen a lambda being called within itself to give itself the answer. It seems circular but it works!!!
#
# SUMMARY
# Amazing code in the given answer. Probably some of the best work I've seen yet as I've difficulty in even determining to start where to analyse it all!