
[2,1,4,4],[1,4,4,2],[2,3,1,3],
[3,1,3,2],[0,0,0,0],[0,0,0,0]

|2| |1| |2|
|1| |4| |3|
|4| |4| |1|
|4| |2| |3|

|3| |0| |0|
|1| |0| |0|
|3| |0| |0|
|2| |0| |0|


legg til index av fulle tubes i en liste?
exclude tuber med kun tre like baller som from?



Funk(from, to){
    if(isDone()) return
    if(lastMove = -lastMove) return
    if(from = 3full) return
    for(i in [x for x in range(6) if x != from])
        for(i in [x for x in range(6) if x != to]){ 
            if( isDone() or not move(from,to) ) {
                return
            }
            else {
                Funk()
            }
        }
    
}


for(i in range(nTubes)){
    Funk()
}


BASE:

    1. no possible moves
    2. isDone()


Starter på tube 1
