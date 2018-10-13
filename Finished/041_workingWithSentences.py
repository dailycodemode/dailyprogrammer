# import re
#
# text = "Shylock speech"
# sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)
#
# sorted_sentences = sorted(sentences, key =len)
#
# print(len(sorted_sentences), "   ", sorted_sentences[-1])
#
# for sentence in sentences:
#     sortedwords = list(sentence.split())
#     if len(sortedwords) > 4:
#         print(" ".join(sortedwords))
#
# # Answer by Err_Eek
# text = "..."
#
# rank = [ s.split(" ") for s in text.replace('?','.').replace('!','.').split(".") ]
#
# rank.sort(key=lambda x: len(x), reverse=True)
#
# # BREAKDOWN
# here's a dirty little secret about this website. Have the answers
# are malgimations of what I've found on sourceforge which is the
# best internet site ever. I take a lot of code but I don't really
# go into it too far. Some of these things are enormous and a
# fleeting knowledge can get you quite far but in the fairness of
# this blog actually making me a better  programmer, I will be
# explaining regular expressions tomorrow.
#
# The answer did something rather clever here. What he is doing
# in the first spot
# text.replace('?','.').replace('!','.').split(".")
# is converting all the endings to a full stop i.e. the same ending
#  and then splitting up his sentences if he finds a full stop. Sneaky.
# [ s.split(" ") for s in list_of_sentneces
# He then takes each sentence in the list and splits them into sublists
#
# rank.sort(key=lambda x: len(x), reverse=True)
# This lambda function organizes the list based on
# the length with the longest going first
#
# print("%d : %s."%(len(rank[0]),' '.join(rank[0])))
# Finally he just prints out the first entry
# in his list and joins up the associated word.
#
# # Summary
# I like the given answer quite a bit although because of its
# conscieness. My own, I'm so so on due to it's blunt answering