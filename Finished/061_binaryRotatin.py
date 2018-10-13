# # DAILY CODE MODE
# number = 54321
# binary = list("{0:b}".format(number))
#
# ans = []
# for x in range(len(binary)):
#     ans.append(int("".join(binary), base=2))
#     binary.insert(0, binary.pop())
#
# print(ans)
#
# # Answer by xjtian
# def rotateChain(b):
#     if not '0' in b:
#         return str(int(b, 2))
#     else:
#         return str(int(b, 2)) + ' -> ' + rotateChain(rotateString(b))
#
# def rotateString(s):
#     return s[:-1] if s[-1] == '0' else '1' + s[:-1]
#
# print(rotateChain(bin(341)[2:]))
#
# BREAKDOWN
# The user passes in a number to the function like this bin(54321)[2:] as bin will return the string with the 0b before the stringed number so we need to get rid of that
#
# str(int(b, 2))
# This is taking a binary number, b, and converting to an int. The int method is taking 2 parameters. The stringed number which we are used to and then the base that the number is expected to be in i.e. base 2 for binary
#
# if not '0' in b:
# This is checking if a number contains any zeros because if a value is '11' or '1111111111', well then there is no variation of this.
# This is also how we break out of the recursion.
#
# str(int(b, 2)) + ' -> ' + rotateChain(rotateString(b))
# So yet more recursion. the part on the left is in binary and then the second part is thrown into the main formula again but this time without the zero which was sent to the front
#
# SUMMARY
# Nice answer. I should probably read the questions more carefully as my answer isn't correct because I've kept in the leading zeros. Woops.