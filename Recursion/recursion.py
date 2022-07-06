"""
###### Tower of Hanoi 

we have three towers A B C. A is the source and C is the destination 
We have n disks on A and target is to send n disks from source(A) to destination(C)

rule : 
1. only one disk can be transferred in 1 step 
2. smaller disk are always kept on top of larger disk




       |         |        |                            |      |         |
     ||||||      |        |           ====>            |      |       ||||||
____||||||||_____|________|______                 _____|______|______||||||||_

    source    helper    destination

"""

# n disk given --> n-1 to helper --> last to destination --> n-1 to destion using source as helper 

def towerOfHanoi(n, source, helper, distination) : 
    
    # base case 
    if n ==1 : 
        print('transfer disk ', n, " from ", source, " to ", distination)
        return 
    
    towerOfHanoi(n-1, source, distination, helper)
    print('transfer disk ', n, " from ", source, " to ", distination)
    towerOfHanoi(n-1, helper, source, distination)

n = int(input())
towerOfHanoi(n, 'source', 'helper', 'distination')

# time Complexity : O(2^n - 1) = O(2^n)
# T(n) = 2T(n-1) + 1
# T(n-1) = 2T(n-2) + 1 
# T(n-2) = 2T(n-3) + 1 
# .
# .
# .
# T(1) = 1 



"""
###### Print a string in reverse 
"""

def printReverse(char, index) : 
    if (index == 0) : 
        print(char[index], end= '')
        return 
    
    print(char[index], end='')
    printReverse(char, index-1)

char = input()
printReverse(char, len(char)-1)

# time Complexity : O(N) --> len(string)



"""
###### find the first and last occurance of an element in string 
"""
first, last = -1, -1  

def findOccurance(string, index, element) : 
    global first, last 

    if index == len(string) : 
        print(first, last)
        return 

    currChar = string[index]
    if currChar == element : 
        if first == -1 : 
            first = index 
        else : 
            last = index 

    findOccurance(string, index+1, element)

string = input()
findOccurance(string, 0, 'a')

# time Complexity : O(N) --> len(string)




"""
###### check if an array is sorted strictly increasing  
"""

def isSorted(arr, index) : 

    if index == len(arr) - 1 : 
        return True

    if arr[index] < arr[index+1] : 
        return isSorted(arr, index+1)
    else : 
        return False 

arr = list(map(int, input().split()))
print(isSorted(arr, 0))

# time Complexity : O(N) --> len(arr)




"""
move all x to the end of the string 
"""

def moveAllX(string, index, count, newString) : 

    if index == len(string) : 
        for i in range(count) : 
            newString += 'x'
        
        print(newString)
        return

    currChar = string[index]
    if currChar == 'x' : 
        count += 1  
        moveAllX(string, index+1, count, newString)
    else : 
        newString += currChar
        moveAllX(string, index+1, count, newString)

string = input()
moveAllX(string, 0, 0, '')

# time Complexity : O(N + count) --> O(2N)



