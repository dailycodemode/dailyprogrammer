# DAILY CODE MODE
# morse = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..".split()
# alpB = "abcdefghijklmnopqrstuvwxyz"
#
# sentence = "hi therea"
#
# def morseTranslator(sentence, toMorse):
#     answer = ""
#     if toMorse == True:
#         for c in sentence:
#             if c.lower() >= "a" and c.lower() <= "z":
#                 answer = answer + morse[alpB.index(c)] + " "
#             elif c.lower() == " ":
#                 answer = answer + " "
#     else:
#         liner = sentence.split(" ")
#         for c in sentence.split(" "):
#             if c == "":
#                 answer = answer + " "
#             else:
#                 answer = answer + alpB[morse.index(str(c))]
#     return answer.strip()
#
# print(morseTranslator(".... ..  - .... . .-. . .-", toMorse = False))
#
# Answer by kevwillia
# import re
#
# a2m = {
#     'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.',
#     'f':'..-.','g':'--.','h':'....','i':'..','j':'.---',
#     'k':'-.-','l':'.-..','m':'--','n':'-.','o':'---',
#     'p':'.--.','q':'--.-','r':'.-.','s':'...','t':'-',
#     'u':'..-','v':'...-','w':'.--','x':'-..-','y':'--.-',
#     'z':'--..','1':'.----','2':'..---','3':'...--','4':'....-',
#     '5':'.....','6':'-....','7':'--...','8':'---..','9':'----.',
#     '0':'-----',',':'--..--','.':'.-.-.-','?':'..--..','/':'-..-.',
#     '-':'-....-','(':'-.--.-',')':'-.--.-',' ':'','':' '
#     }
#
# m2a = dict((v,k) for k, v in a2m.items())
# m2a['  '] = ' '
#
# s = input('-->').lower()
#
# def encode(s): return ' '.join(a2m[x] for x in s)
# def decode(s): return ''.join(m2a[x] for x in re.findall(r'[.-]+|  ', s))
#
#
# e = encode(s)
# print(e)
# d = decode(e)
# print(d)
#
# BREAKDOWN
# m2a = dict((v,k) for k, v in a2m.items())
# This is a handy of reversing a dictionarys items with it's keys by swapping over the keys and values and storing them into a list
#
# SUMMARY
# I like these type of answers and they are very neat. If I was to do this profestionally then I may do it as it was done in this answer however, writing out the dictionarys are so boring and time-consuming that I usually just get the index instead out of a string.
