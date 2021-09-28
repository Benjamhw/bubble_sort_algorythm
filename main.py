import numpy as np
import copy as cp
import random
import datetime
from tubes import tubesOriginal


def solve(tubes):  

    thistubes = cp.deepcopy(tubes)

    bestRun = 1000
    bestMoves = []
    badMoves = []
    totalMoves = 0
    successfulRuns = 0
    
    for i in range(50):
        moves = []
        maxTries = 1000
        counter = 0
        nTubes = len(thistubes)
        while not isDone(thistubes) and counter < maxTries:
            counter += 1

            fromIndex = random.randint(0,nTubes-1)
            
            toIndex = random.randint(0,nTubes-1)
            # inefficient?
            # if counter == 1: 
            #     toIndex = nTubes-1
            
            if fromIndex == toIndex: continue
            if not validateMove(thistubes, fromIndex, toIndex):
                continue

            fromTube = thistubes[fromIndex]

            if tubeIsOneColorFull(fromTube):
                continue

            if len(moves) > 0 and moves[-1][0] == toIndex and moves[-1][1] == fromIndex:
                continue

            testMove = move(thistubes, fromIndex, toIndex)

            if testMove == (True, False):
                moves.append([fromIndex,toIndex])
            elif testMove == (True, True):     #If flipped
                moves.append([toIndex, fromIndex])
        
        if(not isDone(thistubes)):
            #print("Could not solve.")
            thistubes = cp.deepcopy(tubes)
            badMoves.append(moves)              #Keep track of bad moves    
            continue

        successfulRuns += 1
        totalMoves += len(moves)
        thistubes = cp.deepcopy(tubes)

        if len(moves) < bestRun:
            bestRun = len(moves)
            bestMoves = moves

        

    file = open("moves.txt", "w")

    for m in bestMoves:
        file.write(str(m)+str("\n"))
    file.close()

    print("best: " + str(bestRun))
    #print("Avg.: " + str(totalMoves/successfulRuns))
    print("Successful.: " + str(successfulRuns))


def isDone(tubes):
    for tube in tubes:
        if not tubeIsOneColorFull(tube):
            return False
    return True

def validateMove(tubes, fromIndex, toIndex):
    if fromIndex == toIndex:
        return False

    fromTube = tubes[fromIndex]
    toTube = tubes[toIndex]

    if tubeIsOneColorFull(fromTube) \
            or tubeIsEmpty(fromTube) \
            or tubeIsFull(toTube):
        return False

    if tubeIsOneColor(fromTube) and tubeIsEmpty(toTube):
        return False

    return bubblesMatch(fromTube, toTube)
            

def tubeIsEmpty(tube):
    for b in tube:
        if not b == 0:
            return False
    return True

def tubeIsFull(tube):
    return not 0 in tube

def tubeIsOneColorFull(tube):
    c = tube[0]
    for b in tube:
        if not b == c:
            return False
    return True

def tubeIsOneColor(tube):
    c = tube[-1] #Find the color in the bottom
    for b in tube:
        if not b == c and not b == 0:
            return False
    return True

def bubblesMatch(fromTube, toTube):
    topFrom = np.where(fromTube>0)[0]
    topTo = np.where(toTube>0)[0]

    if tubeIsEmpty(toTube):
        return True

    topToIndex = topTo[0]
    topFromIndex = topFrom[0]

    return fromTube[topFromIndex] == toTube[topToIndex]

def tubeSize(tube):
    return len(np.where(tube>0)[0])

def move(tubes, fromN:int, toN:int):
    """
    fromN = tube to grab from
    toN = tupe to add to
    """

    fromTube = tubes[fromN]
    toTube = tubes[toN]
    flipped = False

    if tubeIsOneColor(fromTube) and tubeIsOneColor(toTube):
        if tubeSize(fromTube) > tubeSize(toTube) and not tubeIsEmpty(toTube):
            fromTube = tubes[toN]
            toTube = tubes[fromN]
            flipped = True

    toEmpty:bool = False

    topFrom = np.where(fromTube>0)[0]
    topTo = np.where(toTube>0)[0]

    if tubeIsEmpty(toTube):
        toEmpty = True
        topToIndex = 3
    else:  
        topToIndex = topTo[0]

    topFromIndex = topFrom[0]

    topFromBouble = fromTube[topFromIndex]

    """Set to tube"""
    if toEmpty:
        toTube[topToIndex] = topFromBouble
    else:
        toTube[topToIndex-1] = topFromBouble

    """Set from tube"""
    fromTube[topFromIndex] = 0

    
    return True, flipped

start = datetime.datetime.now()
solve(tubesOriginal)
end = datetime.datetime.now()
diff = end-start
print(diff.total_seconds())

# test = np.array([[0,1,1,1],[0,0,0,1]])
# print(move(test,1,0))
# print(test)

