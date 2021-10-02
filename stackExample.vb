|2| |1| |2|
|1| |4| |3|
|4| |4| |1|
|4| |2| |3|

|3| |0| |0|
|1| |0| |0|
|3| |0| |0|
|2| |0| |0|

STACK:

Funk(0,1) return
Funk(0,2) return
...
Funk(0,4) move(0,4)
 Funk(0,1) return
 Funk(0,2) return
 ...
 Funk(0,5) move(0,5)
  Funk(0,1) return
  Funk(0,2) return
  ...
  Funk(1,5) move(1,5)
   Funk(0,1) move(0,1)
    Funk(0,1) return
    ...
    Funk(1,0) return RC
    ...
    Funk(2,4) move(2,4)
     ...
     Funk(1,0) move(1,0)
      Funk(0,1) return RC
      Funk(1,0) move(1,0)
       Funk(1,0) move(1,0)
        ...
        Funk(1,4) move(1,4)
         Funk(2,1) move(2,1)
          Funk(2,5) move(2,5)
           Funk(1,2) move(1,2)
            Funk(3,4) move(3,4)
             Funk(3,5) move(3,5)
              Funk(3,1) move(3,1)  
               Funk(1,2) move(1,2) 3->1 , 1->2 unød
                Funk(3,1) move(3,1)
                 Funk(1,4) move(1,4) -> unød
                  ...
                  Funk(0,1) return isDone()!
                 Funk(0,1) return isDone()
                ...return
               ...return
              ...return
             ...return
            ...return
           ...return
          ...return
         ...return
        ...return
       ...return
      ...return
     ...return
    ...return
   ...return
  ...return
 ...return
...return

           
|4| |0| |3|
|4| |0| |3|
|4| |0| |3|
|4| |0| |3|

|0| |2| |1|
|0| |2| |1|
|0| |2| |1|
|0| |2| |1|
       

[
    [1,5,6,7],[3,4,7,1],[2,3,5,7],[8,6,6,5],[5,8,8,3],[9,2,9,4],
    [7,6,9,3],[8,2,2,1],[9,4,1,4],[0,0,0,0],[0,0,0,0]
]



|0| |3| |2| |0| |8| |9|
|0| |4| |3| |6| |8| |2|
|7| |7| |5| |6| |8| |9|
|7| |1| |7| |5| |3| |4|

|6| |8| |9| |0| |0|
|6| |2| |4| |0| |0|
|9| |2| |1| |0| |5|
|3| |1| |4| |1| |5|

Funk(1,9)
 Funk(1,10)
  Funk(4,10)
   Funk(3,4)
    Funk(0,3)
     Funk(6,0)
      Funk(3,6) 
       ...
       return no more moves
       Må gå tilbake til forrige stage..

     

   





Without reverse check:

Funk(0,1) return
Funk(0,2) return
...
Funk(0,4) move(0,4)
  Funk(0,1) return
  Funk(0,2) return
  ...
  Funk(0,5) move(0,5)
    Funk(0,1) return
    Funk(0,2) return
    ...
    Funk(1,5) move(1,5)
      Funk(0,1) move(0,1)
        Funk(0,1) return
        ...
        Funk(1,0) move(1,0)???
          Funk(0,1) move(0,1)???
            STACK OVERFLOW !!!
  
  
  
  