################################################################################
# Purpose of this massive Python Practice File is to remember
# Python specific Data Structures Implementations and capabilities
# To solve interview level algorithm questions. 
# Will be partitioned into seperate files when deemed necessary
################################################################################
#Imports
################################################################################

import os, subprocess, sys

################################################################################
# Classes
################################################################################

class JTObject: 
    def __init__(self, id = int) -> None: 
        #Define member variables to initialize on object creation. 
        #Define an empty set of children that can be populated later.
        self.children = {}
        self.id = id

################################################################################
#Methods w/o classes
################################################################################

#Sorting
def twoPointer(array : []) -> int:
    # Two Pointer Method to tackle Two Sum Problem. 
    # Two Sum - Find the sum of the largest 2 pairs in array. 
    # O(n) should be possible with Two Pointer...
    # Algorithm Steps 
    # 1.) Initialize Pointers at opposite ends of array, sum two elements together
    # - Represents the First Pair
    # 2.) Compare this current sum with the target, move the right pointer backwards.
    # - Assumed inside O(n) loop at this point. 
    # 3.) Compare current_sum with the target. Current_sum < target (Hint?) 
    for i in range(0, len(array), 1): 
        pointLeft = i 
        pointRight = len(array) - 1 
        currSum = array[pointLeft] + array[pointRight]
        if currSum > array[i]: 
            pointRight-=1
        elif currSum < array[i]:
            currSum = array[i]
            pointLeft+=1
        else: 
            return 0
    return currSum 

#Main Method
def main() -> None: 
    # Do a range based for loop for object creation here. 
    # Tree?? / Map?? 
    print("Practicing Python coding Exercises to review on ChatGPT suggestion.")    
    print("___________________________________________________________________")
    #for x in range(100): 
        #new_Object = JTObject(x)
        #print(f"Object creation in progress... {new_Object.id} ")
    nums = [0, 1, 2, 2, 0, 1, 2]
    print(twoPointer(nums))

################################################################################
#Method Execution from Main.
################################################################################

if __name__ == "__main__": 
    main()
