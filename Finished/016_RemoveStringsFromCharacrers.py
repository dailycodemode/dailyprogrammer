#  https://www.reddit.com/r/dailyprogrammer/comments/q8aom/2272012_challenge_16_easy/

# MINE

characters = "aeiou"
sentence = "my name is steed. can you believe that!"

for char in characters:
    sentence = sentence.replace(char, "")

print(sentence)

# ANSWER

s1, s2 = "some source string", "remove"
for letter in iter(s2): s1 = s1.replace(s1, letter, "")

# BREAKDOWN
# didn't realise that you could declare two variables on the same line.
# preference is to keep them on seperate lines

# The iter method seems to be similar to how records are kept in VBA
# and that the 'next' call will send the person to the next line


# REVIEW
# The 'iter' part in the answer does not appear necessary.
# For short for loops I will try and keep them to one line

