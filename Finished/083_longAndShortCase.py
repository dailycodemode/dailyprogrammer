# DAILY CODE MODE
# num = 1234567891111
#
# shortCase = {10**6:	"million",
# 10**9:	"billion"	,
# 10**12:	"trillion"	,
# 10**15:	"quadrillion"	,
# 10**18:	"quintillion"	,
# 10**21:	"sextillion"}
#
# answer = ""
# for x in range(21, 5, -3):
#     if num // (10**x) > 0:
#         answer = answer + str((num // (10**x) )) + " " + shortCase[10**x] + ", "
#         num = num - (num // (10**x)) * 10**x
#
# print(answer[:-2])
#
# Answer by lawlrng
# def solve(num):
#     num_li = []
#     while num > 0:
#         num, rem = divmod(num, 10 ** 3)
#         num_li.append(rem)
#
#     print_num(num_li, True)
#     print_num(num_li, False)
#
# def print_num(n, is_short):
#     if not n: return
#
#     text = "and %d" % (n[0])
#     if is_short: end = "_ thousand million billion trillion quadrillion quintillion".split()
#     else: end = "_ thousand million milliard billion billiard trillion".split()
#
#     if len(n) > 1:
#         print "%s %s" % (', '.join(["%d %s" % (n[i], end[i]) for i in range(1, len(n))][::-1]), text)
#     else: print text[4:]
#
# if __name__ == '__main__':
#     solve(input("Number -> "))
#
#
# BREAKDOWN
# num, rem = divmod(num, 10 ** 3)
# divmod returns the qutotient as well as the remainder of a number.
# num, rem = divmod(7, 2)
# >>> num = 3
# >>> rem = 1
#
# What lawlrng is doing is taking a number and dividing it by 1,000 and addng the remainder to a list until there is no more number greater than 1,000
# Afterwards, this list gets sent to the print function where it is determinded where it is a short or long case.
# Inside here, there are two strings which are the cases which are split into lists which is then brought through the name pronouncer where everyrthing gets subbed in all nice and tidy
#
# SUMMARY
# The answer here is the clear winner here because playing around with natural strings and converting them to understandable computer language is fierce dull. I'm happy enough here to simply understand what has happened and move onto the next challenge.
