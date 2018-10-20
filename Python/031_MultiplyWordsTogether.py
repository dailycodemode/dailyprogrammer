# https://www.reddit.com/r/dailyprogrammer/comments/rg1vv/3272012_challenge_31_easy/
# Mine
letterToNumber = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10,
                  "k":11, "l":12, "m":13, "n": 14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20,
                  "u":21, "v":22, "w":23, "x":24, "y":25, "z": 26}

word1 = "kdj"
word2= "b"

word1num = []
word2num = []

for x in range(len(word1)):
    word1num.append(letterToNumber[word1[x]])

for x in range(len(word2)):
    word2num.append(letterToNumber[word2[x]])

word1 = "".join(str(let) for let in word1num)
word2 = "".join(str(let) for let in word1num)

print(int(word1) * int(word2))


# ANSWER by campsun
import string

class Base26:
    def __init__(self, base26_string):
        self.base26_value = base26_string
        self.decimal_value = self.__to_decimal()

    def __mul__(self, other):
        decimal_result = self.decimal_value * other.decimal_value
        return Base26(Base26.to_base26(decimal_result))

    def __repr__(self):
        return "Base26('%s')" % self.base26_value

    def __str__(self):
        return self.base26_value

    def __to_decimal(self):
        result = 0
        for i, number in enumerate(self.base26_value[::-1]):
            result += 26**i * string.ascii_uppercase.find(number)
        return result

    @classmethod
    def to_base26(cls, decimal):
        base26_string = ''
        while decimal != 0:
            remainder = decimal % 26
            decimal /= 26
            base26_string += string.ascii_uppercase[remainder]
        return base26_string[::-1]