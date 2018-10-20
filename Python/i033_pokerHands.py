# cards = ("A","K","Q","J","T","9","8","7","6","5","4","3","2")
# suits = ("S","H","D","C")
#
# hand = set()
#
# import random
#
# while len(hand) < 5:
#     card = cards[(random.randint(1, len(cards))) - 1]
#     suit = suits[(random.randint(1, len(suits))) - 1]
#     hand.add(card + suit)
#
# suits = ([x[1] for x in hand])
# ranks = ([x[0] for x in hand])
# if suits.count(suits[0]) == 5:print("flush")
# if len(set(ranks)) == 4: print("two pair")
# if len(set(ranks)) == 3 and set(sorted(ranks[0:])) or set(sorted(ranks[2:])) == 1: print("threes")
# elif len(set(ranks)) == 3 : print("two kind")
# if len(set(ranks)) == 2: print("fours")
#
#
#
#
#
