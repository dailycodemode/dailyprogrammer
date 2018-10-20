# # DAILY CODE MODE
# sentence = "Double, double, toil and trouble"
# subS = "il an"
#
# for x in range(len(sentence)):
#     for y in range(len(sentence[x:])-1):
#         if subS == sentence[x:x+y+1]:
#             print(x)
#
# # Answer by xjtian
# def findSubstring(search, key):
#     for i in range(0, len(search) - len(key) + 1):
#         if search[i:i+len(key)] == key:
#             return i
#     return -1
#
# SUMMARY
# Quite an easy question but the answer is better for two reasons. Instead of using a nested for loop which can slow things down considerably with longer sentencese or perhaps even paragraph so instead, the answer checks the length of the substring and then runs through the main sentence once, only checking if that part of the sentence
# is equal to the substring. The other thing that is happening is that you don't need to check to the end of the sentence instead, only needing to check to the length at the end
