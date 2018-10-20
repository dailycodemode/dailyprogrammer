# import math
# letter_to_number = {}
# number_to_letter = {}
#
# base_num = ord('a')
#
# for x in range(26):
#     letter_to_number[chr(x + base_num) ] =  str(x)
#     number_to_letter[str(x)] = chr(x + base_num)
#
# word1 = "scghj"
# word2 = "cba"
#
# # print(letter_to_number)
# word1_int = ""
# for char in word1:
#     word1_int = word1_int + letter_to_number[char]
#
# word2_int = ""
# for char in word2:
#     word2_int = word2_int + letter_to_number[char]
#
# final_num = int(word1_int) * int(word2_int)
# final_num_list = list(str(final_num))
#
# answer = ""
# while len(final_num_list) > 0:
#     print(final_num_list[-1])
#
#     if len(final_num_list) > 1 and final_num_list[-2] + final_num_list[-1] in number_to_letter:
#         answer = number_to_letter[final_num_list[-2] + final_num_list[-1]] + answer
#         del final_num_list[-1]
#         del final_num_list[-1]
#     else:
#         print(final_num_list[-1])
#         print(number_to_letter[final_num_list[-1]])
#         answer =  number_to_letter[final_num_list[-1]] + answer
#         del final_num_list[-1]

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



print(Base26('CSGHJ') * Base26('CBA'))


# BREAKDOWN
# Lots to go through here.

# Commentary
# I really didn't like this challenge. Not for anything to do with the challenge but rather that I spent quite a while trying to fiugre out an elegant solution
# and in the end I just had to brute force my way through it all. And that's not cricket.