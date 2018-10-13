inputs = ["76 74 45 48 13 75 16 14 79 58 78 82 46 89 81 88 27 64 21 63",
          "37 35 88 57 55 29 96 11 25 42 24 81 82 58 15 2 3 41 43 36",
          "54 64 52 39 36 98 32 87 95 12 40 79 41 13 53 35 48 42 33 75",
          "21 87 89 26 85 59 54 2 24 25 41 46 88 60 63 23 91 62 61 6",
          "94 66 18 57 58 54 93 53 19 16 55 22 51 8 67 20 17 56 21 59",
          "6 19 45 46 7 70 36 2 56 47 33 75 94 50 34 35 73 72 39 5"]

for x in range(len(inputs)):
    inputs[x] = inputs[x].split()

gap = 1

for line in range(len(inputs)):

    sumDistance = 0
    for x in inputs[line]:
        distance = 0
        target = [str(int(x) + gap), str(int(x) - gap)]

        for y in range(inputs[line].index(x) + 1, len(inputs[line])):
            distance += 1
            if inputs[line][y] in target:
                sumDistance = sumDistance + distance

    print(sumDistance)

# def rate(line, difference=1):
#     nums = {int(n):i for i, n in enumerate(line.split())}
#     s = sorted(nums)
#     rating = 0
#     for i, j in zip(s, s[1:]):
#         if j - i == difference:
#             rating += abs(nums[i]-nums[j])
#     return rating
#
# for x in range(len(inputs)):
#     inputs[x] = inputs[x].split()
#     print(rate(x))  # bett er as itbreaks the bits apart




### code breakdown

line = "76 74 45 48 13 75 16 14 79 58 78 82 46 89 81 88 27 64 21 63"
# for i, n in enumerate(line.split()):
#     print(i, n)
#  enumerate will split apart each object in a list or string and assign an index number to them

nums = {int(n):i for i, n in enumerate(line.split())}
# # created a dictionary where the number is the key and the index is the value
# # there is also a for statement within a dictionary which I wasn't aware that you could do

s = sorted(nums)
### creates a list from a dictionary where the dictionary keys are sorted, hence why he sorted his index as his dictionary values in the previous step

print(s[1:])
# for i, j in zip(s, s[1:]):
#     print(i,j)
### the zip function here matches each ascending value with the next ascending value. They did this by creating another list from the
### first but just cut out the first entry which would also have the effect of not having to worry about the last entry of the s list
### lovely piece of code.


### Summary
# His is a much cleaner piece of code as he sorts his inputs so that they are much easier to identify. The only thing i wonder is if
# creating a dictionary was necessary and would converting your string list to integers be easier to follow.
# The other piece which I enjoy about his code over mine is that his is not getting lost in a bunch of for loops.