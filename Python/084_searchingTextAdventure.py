import random

pos = [random.randint(1,10), random.randint(1,10)]
treasure = [random.randint(1,10), random.randint(1,10)]

distance = ((pos[0] - treasure[0])**2) + ((pos[1] - treasure[1])**2)

move_dic = {"n":1, "s": -1, "e":1, "w": -1}
while distance != 0:
    move = input("Move where : ")

    if move in ["n", "s"]:
        pos[0] = pos[0] + move_dic[move]
    else:
        pos[1] = pos[1] + move_dic[move]

    distance = ((pos[0] - treasure[0])**2) + ((pos[1] - treasure[1])**2)
    print(distance)
print("victory")

# # Answer by Jazztoken
# import math
# import random
#
# max_x = 100
# max_y = 100
# treasure_coords = (random.randint(-1*(max_x), max_x), random.randint(-1*(max_y), max_y))
#
# def get_dist((x1, y1), (x2, y2)):
#     return round(abs(math.sqrt(float((((x2-x1)**2)+((y2-y1)**2))))), 2)
#
# while True:
#     movedict = {'north' : (treasure_coords[0], treasure_coords[1] + 1),
#             'n' : (treasure_coords[0], treasure_coords[1] + 1),
#             'east' : (treasure_coords[0] + 1, treasure_coords[1]),
#             'e' : (treasure_coords[0] + 1, treasure_coords[1]),
#             'south' : (treasure_coords[0], treasure_coords[1] - 1),
#             's' : (treasure_coords[0], treasure_coords[1] - 1),
#             'west' : (treasure_coords[0] - 1, treasure_coords[1]),
#             'w' : (treasure_coords[0] - 1, treasure_coords[1]),
#             }
#     if treasure_coords[0] == 0 and treasure_coords[1] == 0:
#         print 'You found treasure!'
#         break
#     else:
#         print 'There is nothing here.'
#         print 'Your dial reads ', get_dist((0, 0), treasure_coords)
#         move = False
#         while move not in movedict:
#             move = raw_input("Which direction do you move? ")
#         treasure_coords = movedict[move]

# SUMMARY
# Everyone  has the same answer for this one so no real awards. The only thing that I didn;t see much of (and which I didn't do myself was people define the range of their map and then allow the player to go beyond this point. It's a rarer in larger maps (just as it would be to do in real games as you are incentivized to stay in the main game) but it's something which I noticed.

