with open('035_doc.txt') as f:
    lines = f.readlines()
words = 0
line_num = 1
for line in lines:
    words += len(line.split())
print(len(lines), words)

# ANSWER by lawlrng_prog
import fileinput

newlines = 0
words = 0
for line in fileinput.input():
    newlines += 1
    words += len(line.split())

print ("Newlines: %s\nWords: %s" % (newlines, words))

# BREAKDOWN
# the library fileinput seems to be just another way of importing a file
# which will iterate over an input file
#
# The comment at the end is the python 2 method of printing out strings
# where the %s are placeholder words. This stuff is usually taught
# earlier on in most courses but I've never found too much use for it
# The  \n   brings you to the next line.

# SUMMARY
# Very similar and it seems that using the standard library is more
# popular than fileinput