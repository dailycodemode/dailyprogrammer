# # DAILY CODE MODE
# import math
#
# def code(line, key):
#     sentence = line
#     if len(sentence) % key != 0:
#         sentence = sentence + (key - (len(sentence) % key)) * 'x'
#     sentence = sentence.replace(" ", "_")
#
#     split_list = []
#     answer = ""
#     for k in range(key):
#         for i in range(math.ceil(len(sentence)/ key)):
#             answer = answer + sentence[i*key: i*key+key][k]
#
#     return(answer)
#
# print(code("The cake is a lie!!", 3))
#
# def decode(line, key):
#     split_list = [x for x in line]
#     answer = ""
#
#     for i in range(math.ceil(len(line) / key)):
#         for k in range(key):
#             if (i  +  k*math.ceil(len(line) / key)) < len(line):
#                 answer = answer + line[i  +  k*math.ceil(len(line) / key)]
#
#     return answer
# print(decode("T_kiaihces_eea__l", 3))
#
#
# # Answer by SwimmingPastaDivil
# import random
# msg = 'Cake is a lie'
# col = 3
#
# codedText = ""
#
# # to calculate how many random chars to add at the end.
#
# if len(msg)%col == 0:
#     row = len(msg)//col
# else:
#     row = len(msg)//col+ 1
# newLen = row * col #new message length
# ltext = list(msg)
#
# while len(ltext) < newLen:
#     ltext.append(random.choice('abcdefghijklmnopqrstuvwxyz'))
#
# def encode(col):
#     ntext = []
#     for i in range(col):
#         for j in range(i,newLen,col):
#             ntext.append(ltext[j])
#     global codedText
#     codedText = "".join(ntext)
#     print(codedText)
#
#
#
# def decode(row):
#     dtext = []
#     for i in range(row):
#         for j in range(i,newLen,row):
#             dtext.append(codedText[j])
#     print("".join(dtext))
#
#
#
# encode(col)
# decode(row)
#
# BReakdown
#  //
# This is floor division which acts in the same way as int( 10/3)
# (random.choice('abcdefghijklmnopqrstuvwxyz'))
# this is a method from the random library which returns a random choice from the list choices given
# global codedText
# the use of global is used when you want to change a variable outside the scope of a function instead of just access it
# This is one thing that I really don't like about python. Having private variables is really handy and controls the scope of the data nicely.
#
# range(i,newLen,col):
# the range generator takes three main paratmeters. The first is necessary but the other two are optional
# range([start], stop[, step])
#
# Summary
# Both answers are quite similar however the given answer is neater I think. This problem took me ages to get hte decode working hence why it has taken so long to put up an answer. Nice to finally get around to it