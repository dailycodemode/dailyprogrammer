# DAILY CODE MODE
# with open("085_matrix.txt.txt") as f:
#     content = f.readlines()
#
# content = [x.strip().split() for x in content]
#
# row = []
# col = [0] * len(content[0])
# for row_list in content:
#     row.append(sum([float(i) for i in row_list]))
#     for i in range(len(row_list)):
#         col[i] += int(row_list[i])
#
# print(row)
# print(col)
# print([x for y, x in sorted(zip(row, content))])
#
# sorted_col = list(enumerate(col))
# sorted_col = sorted(sorted_col, key=lambda x: x[1])
#
# list_order = [item[0] for item in sorted_col]
#
# for x in content:
#     for o in list_order:
#         print(x[o], sep= " ")
#     print()
#
# Answer by bh3
# with open("085_matrix.txt.txt") as f:
#     arr = [[int(n) for n in s.split(' ')] for s in f.readlines()]
#
# trn= zip(*arr)
#
# for xi in trn:
#     print(xi)
#
# print(arr)
#
# rows = [(sum(row),row) for row in arr]
# cols = [(sum(col),col) for col in trn]
#
# print 'Rows: '+' '.join([str(row[0]) for row in rows])
# print 'Colums: '+' '.join([str(col[0]) for col in cols])+'\n'
#
# rows = sorted(rows)
# cols = sorted(cols)
#
# cols = zip(*[col[1] for col in cols])
# for row in rows:
#     for elm in row[1]:
#         print elm,
#     print ''
# print ''
# for col in cols:
#     for elm in col:
#         print elm,
#     print ''
#
#
# BReakdown
#     arr = [s for s in f.readlines()]
# This part will just read out each line
#
# int(n) for n in s.split(' ')
# Here the s is split out into a list which is used as n which is turned into an integer.
# Eventually, this line is just getting the array in integer form instead of just a string
#
# zip(*arr)
# This gets the transverse of the array. The * is a functional which unpacks the list so it allows the list to zip itself to the same list
# e.g. zip(*[(1,2,3),(4,5,6)])
# zip((1,2,3),(4,5,6))
# >>> [(1,4), (2,5), (4,6)]
#
# rows = [(sum(row),row) for row in arr]
# This is a list comprehension which is returning 2 values which I've never seen. The first part is just a sum of the row and the second part is the row itself. The next line is identical excpet for the use of columns which is now possible because of the use of the transversed matrix
#
# The rest is just a repeat of the above
#
# Summary
# I found this problem particularly challenging however the answer as given is excellent and was a great learning opportunity.
#
#
#
