"""
Yazan Bawaqna
CS-152 B
Lab 06
November 1st 2022
This program is a demonstartion of a simple optimizing function.
It will allow us to see on how varying the parameters changes the management strategies.
"""
#imports
import random


mylist = [1, 2, 3 , 4, 5, 6, 7]
value = 5

def searchSortedList( mylist, value ):
    """ input: mylist(list of the data to be optimized) and value(to compare the data to)
    output: Found status and """
    # assign to the variable done, the value False
    Done = False
    # assign to the variable found, the value False
    Found = False
    # assign to the variable count, the value 0
    Count = 0
    # assign to the variable maxIdx, the one less than the length of mylist
    MaxIdx = len(mylist) -1 
    
    # assign to the variable minIdx, the value 0
    MinIdx = 0
    i = 0
    # start a while loop that executes while done is not True
    while Done is False: 
        # increment count (which keeps track of how many times the loop executes
        i = i + 1
        # assign to testIndex the average of maxIdx and minIdx (use integer math)
        testIndex = (MaxIdx - MinIdx)/2
        # if the myList value at testIndex is less than value
        if testIndex < value:
            # assign to minIdx the value testIndex + 1
            MinIdx = testIndex + 1
        # elif the myList value at testIndex is greater than value
        elif testIndex < value:
            # assign to maxIdx the value testIndex - 1
            MaxIdx = testIndex - 1
        # else
        else:
            # set done to True
            Done = True
            # set found to True
            Found = True   
            # if maxIdx is less than minIdx
            if MaxIdx > MinIdx:
                # set done to True
                Done = True
                # set found to False
                Found = False
    #return (Found, Count)
    return (Found, Count)
print(searchSortedList(mylist, value))


def test():
    a = []
    N = 10**6
    i = 0
    for i in range(N):
        i = i + 1
        a.append( random.randint(0,N) )
        a.append(42)
        a.sort()
        print(searchSortedList( a, 42 ))
if __name__ == "__main__":
    test()
