# DAILY CODE MODE
# def runLengthEncdoing(sen):
#     answer = []
#     for i in range(len(sen)):
#         if sen[i] == sen[i - 1]:
#
#             answer = answer[:-1] + [[answer[-1][0] + 1, sen[i]]]
#         else:
#             answer.append([1,sen[i]])
#     return answer
#
# print(runLengthEncdoing("Heeeeelllllooooo nurse!"))
#
# def runLengthDecoding(array):
#     answer = ""
#     for arr in array:
#         answer = answer + (arr[1] * arr[0])
#     return answer
#
# print(runLengthDecoding([[1, 'H'], [5, 'e'], [5, 'l'], [5, 'o'], [1, ' '], [1, 'n'], [1, 'u'], [1, 'r'], [1, 's'], [1, 'e'], [1, '!']]))
#
# Answer by joboscribe
# def runl_encode(somejunk):
#     out = []
#     for letter in somejunk:
#         if len(out)==0:
#             out.append([1,letter])
#         elif letter == out[len(out)-1][1]:
#             out[len(out)-1][1] +=1
#         else:
#             out.append([1,letter])
#     return out
#
# def runl_decode(morejunk):
#     out =''
#     for pair in morejunk:
#         out = out + pair[1]*pair[0]
#     return out
#
# SUMMARY
# Answers are very similar, the only differnece is that the first if statement in runl_encode is not necessary seeing as all out statements will be initially empty so it will immediatly go to the else staement.
#
