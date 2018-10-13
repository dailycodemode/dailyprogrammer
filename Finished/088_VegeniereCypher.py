# DAILY CODE MODE
# def Vegeniere_encrypt(message, cypher, toEncrypt):
#     import math
#
#     alp = 'abcdefghijklmnopqrstuvwxyz'
#     message = message.lower()
#     cypher = cypher.lower()
#
#     ext = math.ceil(len(message) / len(cypher))
#     cypher_ext = cypher * ext
#     cypher_ext = cypher_ext[: len(message)]
#
#     ans = []
#     for i in range(len(message)):
#         if toEncrypt == True:
#             ans.append(alp[(alp.find(message[i]) + alp.find(cypher_ext[i])) % 26])
#         else:
#             ans.append(alp[(alp.find(message[i]) - alp.find(cypher_ext[i])) % 26])
#
#     return "".join(ans).upper()
#
# print(Vegeniere_encrypt('THECAKEISALIE', 'GLADOS', True))
# print(Vegeniere_encrypt('ZSEFOCKTSDZAK', 'GLADOS', False))
#
#
# Answer uncredited
# import string
#
# def encrypt(word, key, encode=True):
#     code = [(k, v) for k, v in enumerate(string.ascii_uppercase)]
#     key_values = [code[x][0] for y in key for x in range(26) if y == code[x][1]]
#     word_values = [code[x][0] for y in word for x in range(26) if y == code[x][1]]
#
#     if encode==True:
#         sums = [key_values[i % len(key_values)] + word_values[i] for i in range(len(word_values))]
#         for n, i in enumerate(sums):
#           if i > 25:
#             sums[n] -= 26
#
#         return "".join([b[1] for a in sums for b in code if a==b[0]])
#
#       else:
#         sums = [ word_values[i] - key_values[i % len(key_values)] for i in range(len(word_values))]
#
#         for n, i in enumerate(sums):
#           if i < 0:
#             sums[n] += 26
#
#         return "".join([b[1] for a in sums for b in code if a==b[0]])
#
# code = [(k, v) for k, v in enumerate(string.ascii_uppercase)]
# key_values = [code[x][0] for y in key for x in range(26) if y == code[x][1]]
# word_values = [code[x][0] for y in word for x in range(26) if y == code[x][1]]
#
# I think this is a bit of overkill. WHat is happening is that he is breaking apart the code into an enumerated list with an index. Then he goes on to check what value these should all have
# It works but there's a lot of wasted time due to the nested iteration
#
# key_values[i % len(key_values)]
# This part is getting the same value where the encrypt would be. ice way to use it.
#
# Summary
# I like my answer and find it a lot easaier to ead as compared to the given answer.