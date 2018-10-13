# # DAILY CODE MODE
# def split_repeats_chars_from_word(word):
#     cleaned_word = ""
#     second_word = ""
#     for x in range(len(word)-1):
#         if word[x] == word[x+1]:
#             second_word = second_word + word[x]
#         else:
#             cleaned_word = cleaned_word + word[x]
#     cleaned_word = cleaned_word + word[-1]
#
#
# # ANSWER by Should_I_say_this
# def removedup(a):
#     b=''
#     c=''
#     for prev,cur in zip(' '+a[:-1],a):
#         if prev ==cur:
#             b+=prev
#         else:
#             c+=cur
#     print(c,'\n',b,sep='')
# #
# BREAKDOWN
# for prev,cur in zip(' '+a[:-1],a):
#
# zip is a deceptively powerful method.
# zip pairs up two or more lists against their indexes until
# it can't pair any more to form one combined list. Zip is really
# useful when you have to compare something to itself.
# #
# SUMMARY
# Very similar answers. I like the use of zip in given answer.