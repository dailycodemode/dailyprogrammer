#  MINE
list = [1,2,3,4,"a", "e", 6]

list1 = list[:int(len(list)/2)]
list2 = list[int(len(list)/2):]

print(list1, list2)

# ANSWER by prophile
def splitter(lister):
    d = int(len(list)/2)
    return lister[:d], lister[d:]

print(splitter(list))

# BREAKDOWN
# didn't realise that you could return more than one thing from
# a function at once which in this case returns as a a tuple

SUMMARY
There is a balancing act in Python between doing things on a single line versus breaking them apart to make the steps a little clearer. So I would be happy with either of the above
