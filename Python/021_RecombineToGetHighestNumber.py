# input = input("numbers please")
input = 435676

str_input = str(input)
str_sortedInput = sorted(str_input, reverse=True)

ans = ""

for num in str_sortedInput:
    ans = ans + num

# OR DO A REVERSE SPLIT AT THIS POINT

# print(int(ans))

### ANSWER
# from itertools import permutations
#
# def permutate(n):
#     normal = []
#     for permutation in permutations(n):
#         perm = ''.join(permutation)
#         normal.append(int(perm))
#     normal.sort()
#     index = normal.index(int(n))
#     return normal[index+1]
# print(permutate(argv[1]))

n = 445677
li = [i for i in str(n)]
print(reversed(li))
print(li)

#
# def next_smallest(n):
#     li = [i for i in str(n)]
#     inds = (li.index(i) for i in reversed(li) if i < li[-1])
#     try:
#         swap = next(inds)
#         li[-1], li[swap] = li[swap], li[-1]
#         return int(''.join(li))
#     except StopIteration:
#         return NoneD