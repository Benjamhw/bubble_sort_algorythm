import numpy as np
import copy as cp
import random

"""
Color:

1 - red
2 - green
3 - blue
4 - yellow


"""
tubesOriginal = np.array(
    [
        [2,1,4,4],[1,4,4,2],[2,3,1,3],
        [3,1,3,2],[0,0,0,0],[0,0,0,0]
    ]
)

tubes1 = cp.deepcopy(tubesOriginal)

moves = []

def solve(tubes):
    maxTries = 20000
    counter = 0
    nTubes = len(tubes)

    while not isDone(tubes) and counter < maxTries:
        counter += 1

        fromIndex = random.randint(0,nTubes-1)
        toIndex = random.randint(0,nTubes-1)

        if fromIndex == toIndex: continue

        fromTube = tubes[fromIndex]

        if tubeIsOneColor(fromTube):
            continue

        testMove = move(tubes, fromIndex, toIndex)

        if(testMove == True):
            moves.append([fromIndex,toIndex])
        
    print(len(moves))
    file = open("moves.txt", "w")

    for m in moves:
        file.write(str(m)+str("\n"))
    file.close()
    print(counter)


def isDone(tubes):
    for tube in tubes:
        if not tubeIsOneColor(tube):
            return False
    return True
            

def tubeIsEmpty(tube):
    for b in tube:
        if not b == 0:
            return False
    return True

def tubeIsOneColor(tube):
    c = tube[0]
    for b in tube:
        if not b == c:
            return False
    return True

def move(tubes, fromN:int, toN:int):
    """
    fromN = tube to grab from
    toN = tupe to add to
    """
    fromTube = tubes[fromN]
    toTube = tubes[toN]
    toEmpty:bool = False

    topFrom = np.where(fromTube>0)[0]
    topTo = np.where(toTube>0)[0]

    if len(topFrom) == 0:
        return False, "Error: From tube empty"
    if len(topTo) == 0:
        toEmpty = True
        topToIndex = 3
    else:  
        topToIndex = topTo[0]

    topFromIndex = topFrom[0]

    topFromBouble = fromTube[topFromIndex]
    topToBouble = toTube[topToIndex]

    if topToIndex == 0:
        return False, "Error: To tube full"

    if not topFromBouble == topToBouble:
        if not toEmpty:
            return False, "Error: Boubles don't match"

    """Set to tube"""
    if toEmpty:
        toTube[topToIndex] = topFromBouble
    else:
        toTube[topToIndex-1] = topFromBouble

    """Set from tube"""
    fromTube[topFromIndex] = 0

    
    return True


solve(tubes1)
#print(move(tubes1, 5,4))