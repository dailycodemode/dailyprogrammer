# DAILY CODE MODE
# titles =['Name', 'Address', 'Description']
# input =  [['Reddit', 'www.reddit.com', 'the frontpage of the internet'],
#         ['Wikipedia', 'en.wikipedia.net', 'The Free Encyclopedia'],
#         ['xkcd', 'xkcd.com', 'Sudo make me a sandwich.']]
#
# print("*" * 34 *  3)
# for x in range(len(titles)):
#     print("********", "{: ^16s}".format(titles[x]), "********", end = "")
# print()
# for x in range(len(titles)):
#     inp = input[x]
#     for y in inp:
#         print("*", "{: ^30s}".format(y), "*", end = "")
#     print()
# print("*" * 34 * 3)
#
# Answer by acero
# def getLength(title, listItems):
#   longestItemLength = max(len(x) for x in listItems)
#   titleLength = len(title)
#   if titleLength > longestItemLength:
#     length = titleLength + 4
#   else:
#     length = longestItemLength + 4 + ((longestItemLength - titleLength) % 2)
#   return length
#
# def printHeader(title, length):
#     numSpaces = (length - len(title) - 2) // 2
#     print('+' + '-' * (length - 2) + '+')
#     print('|' + ' ' * numSpaces + title + ' ' * numSpaces + '|')
#     print('+' + '-' * (length - 2) + '+')
#
# def printRow(listItem, length):
#     extraSpaces = length - len(listItem) - 3
#     print('| ' + listItem + ' ' * extraSpaces + '|')
#
# def printFooter(length):
#     print('+' + '-' * (length - 2) + '+')
#
# title = 'Necessities'
# listItems = ['fairy', 'cakes', 'happy', 'fish', 'disgustedddddddd', 'melon-balls']
#
# length = getLength(title, listItems)
#
# printHeader(title, length)
# [printRow(listItem, length) for listItem in listItems]
# # printFooter(length)
#
# BREAKDOWN
# numSpaces = (length - len(title) - 2) // 2
# // is a math operator called floor division which is equivalent to int(11/2) = 5 and it just rounds down to an integer whatever you are looking for
#
# longestItemLength = max(len(x) for x in listItems)
# This is a generator which returns the length of each item in the list. Then we only take the max value of it. Nice clean way of getting longest value
#
# [printRow(listItem, length) for listItem in listItems]
# This is yet more list comprehensions in python although this is interesting because it is throwing the iterated item into a function along with the length and then performing an action on it.
# The only problem I have with this is that the list isn't used for anything so I wonder if this would be the correct pythonic way of doing things
#
# SUMMARY
# I'm not the biggest fan of these type of challenges because they just seem to be pretty awards which isn't that interesting and would usually one of the last things you would address on a project
# The answer here does do a nice job of maintaining a certain length throughout.
#
#
