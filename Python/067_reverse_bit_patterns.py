# def reverse_bit_pattern(n):
#     binary= "{0:b}".format(n)
#     pre = "0" * (32 - len(binary)) + binary
#     reversed_binary = pre[::-1]
#     return int(reversed_binary, 2)
#
# print(reverse_bit_pattern(13))
#
# # Answer by xjtian
# numNormal = int(input())
# binNumNormal = str(format(numNormal,'b'))
#
# while len(binNumNormal) < 32:
#     binNumNormal = ('0' + binNumNormal);
#
# binNumReversed = binNumNormal[::-1]
# numReversed = int(binNumReversed,2)
#
# print(numReversed)
#
# BREAKDOWN
# print(str(format(12,'b')))
# The format section converts the given number to a number (which is an integer). We then cast it to a string so that we can reverse it later
#
# SUMMARY
# Most answers were about the same. In a question like this I think it is a good idea to take a few more lines to explain what is happening instead of trying to fit it all into one line which would look neat but would take a while for a reader to review the code as there is a lot of unpacking necessary
#
#
#
