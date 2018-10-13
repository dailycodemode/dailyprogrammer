# DAILY CODE MODE
# def titlecase(sentence, exc):
#     answer = []
#     for word in sentence.split():
#         if word not in exc:
#             answer.append(word[0].upper() + word[1:].lower())
#         else:
#             answer.append(word.lower())
#     return " ".join(answer).capitalize()
#
# print(titlecase('the quick brown fox jumps over the lazy dog', ['jumps', 'the', 'over']))
#
#
# def titlecase(string, exceptions):
#     first = string.split()[0].capitalize() + " "
#     print(first)
#     def _capitalize(word):
#         if word.lower() not in exceptions:
#             return word.capitalize()
#         return word.lower()
#     return first + " ".join(_capitalize(word) for word in string.split()[1:])
#
# print(titlecase('the quick brown fox jumps over the lazy dog', exceptions))
# BREAKDOWN
# first = string.split()[0].capitalize() + " "
# Captialize capilaziles the first letter of a string so what the person has done above is split apart the sentence and taken the first word and capitalized iit
# string.split()[1:])
# This is splitting apart the whole sentence but not keeping the first word which he has earlier kept as 'first'
# He then sends each of those words as a generator into the inner function _capitalize and gives an if statement to determine whether to capitalize it or not
#
# Summary
# Capitalize is a much nicer way of getting the first capital than splitting apart the string. I like the given answer however I think it is overthought.
