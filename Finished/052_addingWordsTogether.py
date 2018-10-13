# # DAILY CODE MODE
# letter_values_dict = {}
# for i, letter in enumerate(range(ord("a"), ord("z")+1)):
#     letter_values_dict[chr(letter)] = i+1
#
# words = ['hat', 'cabbage', 'hen']
#
# word_values = {}
# for word in words:
#     value= 0
#     c_count = 0
#     for c in word:
#         value += letter_values_dict[c]
#         c_count+= 1
#
#     word_values[word] = value / c_count
#
# print(word_values)
#
# import operator
#
# sorted_word_values = sorted(word_values.items(), key=operator.itemgetter(1))
#
# print(sorted_word_values)
#
# # Answer by ret0
# def mytotal(word):
#     return sum([ord(x)-96 for x in word.lower()])
#
#
# def mysort(seq):
#     return sorted(seq, key=mytotal)
#
# BREAKDOWN
# WHen we want to get the sum of the letter values we can use sum() and wrap it around a list
# So what they do here is really clever as it cuts out a lot of the stuff which I didn't need to do
# sum([ord(x)-96 for x in word.lower()])
# as it did not need to create a dictioinary, instead it just finds the ascii value and then subtracts 96 from it and
# then all of this in a one liner.
#
# One thing that I didn't know before today was that the square brackets which are used in all one liner loops is actually a generator
# which I had no idea about. I'll have to an entry just explaining generators.
#
# The other brilliant piece of code is the mysort function which sorts the sequence by passing into a function which
# will be sorted on this.
#
# SUMMARY
# My answer was only so so but the given answer by ret0 is brilliant