def decorator(str):
    for x in range(10): print(chr(126), end = " ")
    print(str, end=" ")
    for x in range(10): print(chr(126), end=" ")

decorator("hit")

# ANSWER by prophile

import textwrap
string = input("Please enter a sentence ")
string = textwrap.wrap(string,35)
print(string)
print("*" * 41)
for x in range(len(string)):
    print("*",string[x].center(37), "*")
print("*" * 41)

# BREAKDOWN
string = textwrap.wrap(string,35)
# textwrap is a standard python module for limiting what can be written to a screen
# it will limit how far the stirng can be displayed to ensure that a print read out
# limited to more readsable levels.
print("*",string[x].center(37),"*")
# string.centre will place a space wrapper around the string of length 37 and then
# place the actual center in the string of it. if we remove the textwrap though it
# will trat every line as if it is a single character as textwrap will have placed
# the string into a list of a single entry (or longer, if it goes over the defined length

# SUMMARY
# This was my first introduction to textwrap. The answer is far better than my own
# version and will keep it in mind in future
