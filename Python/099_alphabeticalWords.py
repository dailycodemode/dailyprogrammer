# # DAILY CODE MODE
# i = open('enable1.txt', 'r')
# count = 0
# for l in i.readlines():
#     if l.strip() == ''.join(sorted(l.strip())):
#         count += 1
#     word = l[::-1]
#
# print(count)
#
#
#
# # Answer by yentup
# words, count = open('enable1.txt', 'r').readlines(), 0
# for word in words:
#     aword = word[:-2]
#     if ''.join(sorted(aword)) == aword: count += 1
# print(count)
