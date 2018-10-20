# # DAILY CODE MODE
# symbols = ["Ac","Ag","Al","Am","Ar","As","At","Au","B","Ba","Be","Bh","Bi",
#        "Bk","Br","C","Ca","Cd","Ce","Cf","Cl","Cm","Cn","Co","Cr","Cs",
#        "Cu","Db","Ds","Dy","Er","Es","Eu","F","Fe","Fl","Fm","Fr","Ga",
#        "Gd","Ge","H","He","Hf","Hg","Ho","Hs","I","In","Ir","K","Kr","La",
#        "Li","Lr","Lu","Lv","Md","Mg","Mn","Mo","Mt","N","Na","Nb","Nd","Ne",
#        "Ni","No","Np","O","Os","P","Pa","Pb","Pd","Pm","Po","Pr","Pt","Pu",
#        "Ra","Rb","Re","Rf","Rg","Rh","Rn","Ru","S","Sb","Sc","Se","Sg","Si","Sm",
#        "Sn","Sr","Ta","Tb","Tc","Te","Th","Ti","Tl","Tm","U","Uuo","Uup","Uus","Uut",
#        "V","W","Xe","Y","Yb","Zn","Zr"]
#
# def BreakingBadTitle(name):
#     import random
#
#     n_symbols = []
#     while len(symbols) > 0:
#         i = random.randint(0, len(symbols) - 1)
#         n_symbols.append(symbols.pop(symbols.index(symbols[i])))
#     for c in n_symbols:
#         if name.lower().find(c.lower()) > -1:
#             return name.replace(c.lower(), "[" + c + "]")
#
# print(BreakingBadTitle("Daily Code Mode"))
#
# # Answer uncredited
# Symbols = ["Ac","Ag","Al","Am","Ar","As","At","Au","B","Ba","Be","Bh","Bi",
#        "Bk","Br","C","Ca","Cd","Ce","Cf","Cl","Cm","Cn","Co","Cr","Cs",
#        "Cu","Db","Ds","Dy","Er","Es","Eu","F","Fe","Fl","Fm","Fr","Ga",
#        "Gd","Ge","H","He","Hf","Hg","Ho","Hs","I","In","Ir","K","Kr","La",
#        "Li","Lr","Lu","Lv","Md","Mg","Mn","Mo","Mt","N","Na","Nb","Nd","Ne",
#        "Ni","No","Np","O","Os","P","Pa","Pb","Pd","Pm","Po","Pr","Pt","Pu",
#        "Ra","Rb","Re","Rf","Rg","Rh","Rn","Ru","S","Sb","Sc","Se","Sg","Si","Sm",
#        "Sn","Sr","Ta","Tb","Tc","Te","Th","Ti","Tl","Tm","U","Uuo","Uup","Uus","Uut",
#        "V","W","Xe","Y","Yb","Zn","Zr"]
# Word = input("Word: ")
# for i in range(len(Symbols)):
#     WordCheck = Word.lower()
#     if Symbols[i].lower() in WordCheck:
#         SymText = "[" + Symbols[i] + "]"
#         WordSy = Word.replace(Symbols[i].lower(), SymText)
#         print(WordSy)
#
# SUMMARY
# My answer is a little messy as I created a secondary list of randomized elements. By doing this I was able to check whether the element exist and then return a string with a single change for each 'element'. The answer does not do this, instead, it just replaces everything that could be an element with a string
# I also took the list from the answer for lazieness reasons.