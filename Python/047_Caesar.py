# https://www.reddit.com/r/dailyprogrammer/comments/t33vi/522012_challenge_47_easy/
def decoder(code, n):
    caesarDict = {}
    key = n

    for letter in range(97,123):
        codeNum = letter + key
        if codeNum > 122:
            codeNum -= 26
        caesarDict[chr(letter)] = chr(codeNum)

    solved = []

    for x in code:
        if ord(x.lower()) in range(97, 123):
            x = caesarDict[x.lower()]
        solved.append(x)

    print(n, "".join(solved))


decoder("Spzalu - zayhunl dvtlu sfpun pu wvukz kpzaypibapun zdvykz pz uv ihzpz mvy h zfzalt vm nvclyutlua. ", 19)

# ANSWER by gjwebber

def c_shift(text, shift):
    output = ""
    bot = ord("a")
    top = ord("z")

    for c in text:
        num = ord(c.lower())

        if num >= bot and num <= top:
            new = num + shift
            if new > top:
                new -= top - bot + 1
            if c.isupper():
                new -= 32
            output += chr(new)
        else:
            output += c
    return output

print(c_shift("Hello! xYz", 3))

# # BREAKDOWN
if c.isupper():
    new -= 32
# # tHE Ascii mapping of upper characters is 32 spaces down

# SUMMARY
# Mine and the answer are quite similar. The main difference being that theirs has the added functionality
# of being able to handle upper case letters. Theirs is also more dynamic as most values are not
# hardcoded in. I created a list of all the transfers and then joined them together. They just added it
# to a new string as they wrote which is fine.
# On a final note, I intially wrote my code as a coder and a decoder however seeing as a Caesar cipher
# is only shifting characters, a coder will work the same as the decoder, just at different shift integers.

