from collections import Counter
import numpy as np
from copy import copy, deepcopy
import random
import datetime
from tubes import tubesOriginal


def solve(tubes):  

    thistubes = deepcopy(tubes)

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
            thistubes = deepcopy(tubes)
            badMoves.append(moves)              #Keep track of bad moves    
            continue

        successfulRuns += 1
        totalMoves += len(moves)
        thistubes = deepcopy(tubes)

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


def solveRecursive(tubes):
    thistubes = deepcopy(tubes)
    tubesIt = range(len(thistubes))
    counter = 0
    allSuccessfulMoves = []
    done = False

    def solve(innertubes, innermoves, fromIndex, toIndex):
        nonlocal done
        #Safety net for stack overflow
        nonlocal counter
        counter += 1
        if counter > 40000: 
            return
        #BASE
        if isDone(innertubes):
            done = True
            if len(allSuccessfulMoves) == 0 \
                    or len(allSuccessfulMoves[-1]) > len(innermoves):
                allSuccessfulMoves.append(innermoves)
            return

        if (len(innermoves) > 0 and isReversed(innermoves[-1], [fromIndex,toIndex])) \
                or not validateMove(innertubes,fromIndex,toIndex) \
                or inInfiniteLoop(innermoves): 
            return

        
        tubes1 = copy(innertubes)
        moves1 = copy(innermoves)
        
        testMove = move(tubes1, fromIndex, toIndex)
        if testMove[1]:
            moves1.append((toIndex, fromIndex))
        else:
            moves1.append((fromIndex, toIndex))


        if len(allSuccessfulMoves) > 0 \
                and len(moves1) > len(allSuccessfulMoves[-1]):
            return
        

        # RECURSION
        # for all possible moves at current stage
        for i in tubesIt:
            for j in tubesIt:
                if i == j: continue
                solve(tubes1,moves1,i,j)

    for i in tubesIt:
        for j in tubesIt:
            if i == j: continue
            counter = 0
            solve(tubes,[],i,j)
            done = False
    

    file = open("moves.txt", "w")
    if(len(allSuccessfulMoves)>0):
        for m in allSuccessfulMoves[-1]:
            file.write(str(m)+str("\n"))
    file.close()

    


def isDone(tubes):
    for tube in tubes:
        if not tubeIsOneColorFull(tube):
            return False
    return True

def validateMove(tubes, fromIndex, toIndex):
    if fromIndex == toIndex:
        return False

    fromTube = tubes[fromIndex]
    if tubeIsOneColorFull(fromTube) \
            or tubeIsEmpty(fromTube) \
            or tubeIsAlmostFull(fromTube):
        return False

    toTube = tubes[toIndex]
    if tubeIsFull(toTube):
        return False

    if tubeIsOneColor(fromTube) and tubeIsEmpty(toTube):
        return False

    return bubblesMatch(fromTube, toTube)

def isReversed(lastMove, thisMove):
    return lastMove[0] == thisMove[1] \
        and lastMove[1] == thisMove[0]

def tubeIsEmpty(tube):
    for b in tube:
        if not b == 0:
            return False
    return True

def tubeIsFull(tube):
    return not 0 in tube

def tubeIsAlmostFull(tube):
    return tube[0] == 0 \
        and tube[1] == tube[2] == tube[3] != 0

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

def inInfiniteLoop(moves):
    if len(moves) == 0: return False
    lastMove = moves[-1]
    count = moves.count(lastMove)
    if(count > 5): return True
    return False

def inInfiniteLoop2(moves): #Does not work for 3-36
    if len(moves) < 8: return False
    lastMoves = moves[-4:]
    prevMoves = moves[-8:-4]
    return lastMoves == prevMoves

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
solveRecursive(tubesOriginal)
end = datetime.datetime.now()
diff = end-start
print(diff.total_seconds())