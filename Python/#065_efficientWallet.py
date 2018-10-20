# DAILY CODE MODE
# curr = {1: "Penny",
# 5: "Nickel",
# 10: "Dime" ,
# 25: "Quarter",
# 100: "One-dollar",
# 500: "Five-dollar" ,
# 1000 : "Ten-dollar",
# 5000: "Fifty-dollar",
# 10000 : "Hundred-dollar" }
#
# vals = list(curr.keys())
# vals.sort(reverse=True)
#
# money = 5250
# wallet = []
# for val in vals:
#     print(int(money/val))
#     wallet.append({curr[val]:int(money/val)})
#     money = money - int(money/val) * val
#
# print(wallet)
#
# Answer by _Daimon_
# def coins(value, denominations):
#     value = float(value)
#     denominations = sorted(denominations, reverse = True)
#     result = [0] * len(denominations)
#     while value > 0.00001: # because floating points
#         for index, deno in enumerate(denominations):
#             if deno <= value:
#                 value -= deno
#                 result[index] += 1
#                 break
#     return result
#
# standard_us_coinage = [0.01, 0.05, 0.1, 0.25, 1.0, 5.0, 10.0, 50.0, 100.0]
# print(coins(12.33, standard_us_coinage))
#
# SUMMARY
# I rather like both this question and the given answer. The given answer just keeps reducing by the total by the reverse orderd denominations and then removing it from the total. Pretty nice.
