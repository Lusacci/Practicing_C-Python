# Purpose of this massive Python Practice File is to remember
# Python specific Data Structures Implementations and capabilities
# To solve interview level algorithm questions. 
# Will be partitioned into seperate files when deemed necessary
import os, subprocess, sys
class JTObject: 
    def __init__(self, id = int) -> None: 
        #Define member variables to initialize on object creation. 
        #Define an empty set of children that can be populated later.
        self.children = {}
        self.id = id

def main(): 
    # Do a range based for loop for object creation here. 
    # Tree?? / Map?? 
    print("Practicing Python coding Exercises to review on ChatGPT suggestion.")    
    print("___________________________________________________________________")
    for x in range(100): 
        new_Object = JTObject(x)
        print(f"Object creation in progress... {new_Object.id} ")

#Method Execution from Main.
if __name__ == "__main__": 
    main()
