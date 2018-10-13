# DAILY CODE MODE
# with open("thetyger.txt") as f:
#     content = f.readlines()
#
# content = [x.strip().split()[::-1] for x in content]
#
# for sen in content[::-1]:
#     print(" ".join(sen))
#
# Answer by Svhizo
# i = open('thetyger.txt', 'r')
# o = open('thetygerreversed.txt', 'w')
# for l in reversed(i.readlines()):
#     o.write('%s\n' % ' '.join(l.split()[::-1]))
#
# o = open('thetygerreversed.txt', 'w')
# Opens a new file or existing file and writes to it afresh
# o.write
# Writes a line to the file
#
# ' '.join(l.split()[::-1])
# Swaps a sentence around to read back to front
#
# for l in reversed(i.readlines()):
# Reverses the iterable object. I've never seen it done this way rbut it is a really handy way to do it for a generator object
#
# for x in reversed(range(4)):
#     print(x)
#
# >>> 3
# >>> 1
# >>> 2
# >>> 0
