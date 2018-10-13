T = [[7, 6, 5, 4, 3, 2, 1], [], []]
source = 0; spare = 1; destination = 2; lastPlayedNum = 0;
lastplayedPos = source

def moveNext(lastPlayed, secondMove):
    choices = [0,1,2]
    choices.pop(lastPlayed)
    if T[choices[0]][-1] < T[choices[1]][-1]:
        place = [0,1,2].index(choices[0])
    elif T[choices[0]][-1] > T[choices[1]][-1]:
        place = [0, 1, 2].index(choices[1])
    if secondMove == True:
        choices.pop(place)
        return choices[0]
    return place

def moveWhere(lastPlayed, secondMove):
    choices = [0,1,2]
    choices.pop(lastPlayed)
    if T[choices[0]][-1] < T[choices[1]][-1]: # and T[choices[0]][-1] > T[lastPlayed][-1]:
        place = [0,1,2].index(choices[0])
    elif T[choices[0]][-1] > T[choices[1]][-1]: # and T[choices[1]][-1] > T[lastPlayed][-1]:
        place = [0, 1, 2].index(choices[1])
    if T[choices[0]][-1] < T[lastPlayed][-1] or T[choices[1]][-1] < T[lastPlayed][-1]:
        pass
    if secondMove == True:
        choices.pop(place)
        return choices[0]
    return place

while len(T[0]) != 0:
    base = T[0][-1]
    if base % 2 !=0:   # uneven
        lastPlayedNum = T[source].pop()
        T[spare].append(lastPlayedNum)
        lastPlayedPos = spare
        secondMove = True
        while sum(range(base+1)) != sum(T[spare]):
            z_toMove = moveNext(lastPlayedPos, False)
            z_moveWhere = moveWhere(z_toMove, secondMove)
            secondMove = False
            lastPlayedNum = T[z_toMove].pop()
            T[z_moveWhere].append(lastPlayedNum)
            lastPlayedPos = z_moveWhere
    else:
        lastPlayedNum = T[source].pop()
        T[destination].append(lastPlayedNum)
        lastPlayedPos = destination
        secondMove = False
        while sum(range(base+1)) != sum(T[destination]):
            z_toMove = moveNext(lastPlayedPos, False)
            z_moveWhere = moveWhere(z_toMove, secondMove)
            lastPlayedNum = T[z_toMove].pop()
            T[z_moveWhere].append(lastPlayedNum)
            lastPlayedPos = z_moveWhere



# def hanoi(n=3, src='Source', dest='Destination', spare='Spare'):
#     if n > 0:
#         hanoi(n-1, src, spare, dest)
#         print('Move from %s to %s' % (src, dest))
#         hanoi(n-1, spare, dest, src)
#
# hanoi(n = 8)