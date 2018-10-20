phoneNum = "1-800-COMCAST"

dic_letterToNumber = {"a": 2, "b": 2, "c": 2, "d": 3, "e": 3, "f": 3,
                     "g": 4, "h": 4, "i": 4, "j": 5, "k": 5, "l": 5,  "m": 6, "n": 6,
                     "o": 6, "p": 7, "q": 7, "r": 7, "s": 7, "t": 8, "u": 8, "v": 8,
                     "w": 9, "x": 9, "y": 9, "z": 9, }

for char in phoneNum:
    if char.isalpha():
        phoneNum = phoneNum.replace(char, str(dic_letterToNumber[char.lower()]))

print(phoneNum)


### ANSWER
def tele():
    DICT ={'a': 2, 'c': 2, 'b': 2, 'e': 3, 'd': 3, 'g': 4, 'f': 3,
        'i': 4, 'h': 4, 'k': 5, 'j': 5, 'm': 6, 'l': 5, 'o': 6,
        'n': 6, 'q': 7, 'p': 7, 's': 7, 'r': 7, 'u': 8, 't': 8,
        'w': 9, 'v': 8, 'y': 9, 'x': 9, 'z': 9, '-':'-', ' ':' '}
    numb = str.lower(input('what is the phone number?: '))
    numbers=''
    for i in numb:
        if i in ('1','2','3','4','5','6','7','8','9','0'):
            numbers +=i
        elif i in DICT:
            numbers +=str(DICT[i])
        else:
            numbers = 'You input a symbol!'

# print(numbers), basic[7:])

# BREAKDOWN
# Nothing too difficult here.

# REVIEW
# The answer builds up an entirely new stirng which I don't think is the best
# thing to do because unforseen errors can arise. I prefer my answer where I just
# check if the character is a letter and then replaces the letter accordingly.