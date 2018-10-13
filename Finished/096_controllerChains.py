# # DAILY CODE MODE
# def controllerChains(budget):
#     controller = 20
#     multi = 12
#     available_spaces = 2
#
#     dict = {"c": 0, "m": 0}
#     while budget >= controller and available_spaces > 0:
#         while available_spaces != 1:
#             budget -= controller
#             dict["c"] += 1
#             available_spaces -= 1
#         if budget >= controller + multi:
#             budget -= multi
#             dict["m"] += 1
#             available_spaces += 3
#         if budget > controller and budget < controller + multi:
#             budget -= controller
#             dict["c"] += 1
#             available_spaces -= 1
#     return "Max no of peoples: " + str(dict["c"])
#
# print(controllerChains(116))
#
# # Answer by ret0
# def controllers(money):
#     total =  1
#     total += money // 72 * 3
#     if money % 72 >= 20:
#         total += 1
#     if money % 72 >= 52:
#         total += 1
#     return total
#
# BREAKDOWN
# The answer divides by 72 as this gives the cost of a multi with 3 controleers. This total is then added up by 3. he then checks the modulo of 72 to see what is left to buy more controllers. Then he checks if the modulo of the two controllers plus a controller exists however, I think this should be added by 2 seeing as two controllers are being added.
# Another issue is that the total starts on 1 which assumes the budget will be greater than 20$
#
# SUMMARY
# A fab answr by ret0 which was a great way of understanding of the problem and what the python language can do. Rather enjoyed this one as well.
#
#
