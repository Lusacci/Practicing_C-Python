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
#Debugging
################################################################################

import pdb

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
###########
#Algorithms
###########

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

def sliding_Window(array : [], subarray_Window_Size : int ) -> int:
    #Aim for an O(n) solution using the comparison between a current subarray_window and previous one.
    #Methodology may need to include a window of varying size.... this means being able to use 2 for loops
    #that is still O(n) by only looping what you need and updating when you have to. 
    #First step should always be evaluating initial condition of the data you care about. 
    # - The size of the window here and what it could be to the whole data set. 
    # -- Bigger, equal, or less than the data. 
    # --- Techniques can be used upon evaluating current condition.
    #pdb.set_trace()
    if subarray_Window_Size >= len(array):
        #Just sum the whole thing and return, which is just O(n)
        for item in range(0, len(array), 1): 
            max_sum += array[item]
        return max_sum
    else:
        #Edge case where window size is less than total size, therefore you can split what you need to count. 
        subarray_Window_sum = 0
        for i in range(0, subarray_Window_Size, 1): 
            subarray_Window_sum += array[i] 
        print("The first for loop will only iterate to the end of the subarray window, which gives us: {subarray_Window_sum}")
        #Now count the rest of it after copying what ya have. (Count by 2s not 3s)
        updated_Window_sum = subarray_Window_sum 
        for j in range(subarray_Window_Size, len(array), 1): 
            # To count the remaining elements in the same set, try to break it down into moves. 
            # Slide the window past limit
            updated_Window_sum += array[j]
            # Remove last left limit.
            updated_Window_sum -= array[j - subarray_Window_Size]
            # So at this point, you not only updated the window, you 'counted' the move.
            if updated_Window_sum >= subarray_Window_sum:
                subarray_Window_sum = updated_Window_sum
        return subarray_Window_sum
    
#Main Method
def main() -> None: 
    # Do a range based for loop for object creation here. 
    # Tree?? / Map?? 
    print("___________________________________________________________________")
    print("Practicing Python coding Exercises to review on ChatGPT suggestion.")    
    print("___________________________________________________________________\n")
    test_case1 = [5, 2, -1, 0, 3]
    print(sliding_Window(test_case1, 3))

################################################################################
#Method Execution from Main.
################################################################################

if __name__ == "__main__": 
    main()
