# # Answer by DailyCodeMode
# def numOfOnesInNum(num):
#     str_binary_num = str(bin(num))
#     return str_binary_num.count("1")
#
# # Answer by Cisphyx
# print((lambda n=50031: bin(n).count('1')))
#
# # Breakdown
# The only thing that we should really note is that bin will
# return the binary conversion as a string so no need for str()
# bin(n)
# Secondly, the last '()' is a little confusing because it
# just seems to be doing nothing however it is just another
# very common thing we see all the time i.e. calling a function.
# If you just take out the () then it will return the location
# of the lambda without it actually running so we get the values
# by running the lambda which requires the brackers.
#
# # Summary
# # Very similar answers but the given answer is neater.
#
