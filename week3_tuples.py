"""
Brainnest Python Training
April 2023
Adnane Habib
Team A6
"""
"""
Week 3 Tuples
1.Write a function to find the most common elements in a tuple.
"""
#defining the tuple
myTuple=(1, "banana", "cloud", 1, 2 , 3, 1, "banana", "0", 0, "1", "banana", "banana")
myDict={}
maxValue = 0
maxKey = 0
#traversing the tuple
for element in myTuple:
    #Building occurence histogram
    if element in myDict.keys():
        myDict[element]+=1 
    else:
        myDict[element]=1
    #Detecting the largest frequency
    if (maxValue<myDict[element]):
        maxValue=myDict[element]
        maxKey = element
if __name__=='__main__':
    print("Exercise 1")
    print()
    print(myDict)
    print("The most common element is", maxKey)
    print("It is repeated", maxValue, "times.")
    print()
    print()

"""
Week 3 Tuples
2. Write a function to check if a given tuple is a palindrome, meaning the elements are the same in reverse order.
"""
def tupleIsPalindromFrequency(myTuple):    

    #catching if argument is not a tuple
    try:
        if (not(type(myTuple) is tuple)):
            raise Exception("Sorry, argument must be a tuple.")

    except Exception as e:
        print(e)
        print("Invalid entry")
        return False
        
    else:
        print("Is the tuple a plaindrom?")
        myList = list(myTuple)
        myReversedList = list(myTuple)
        myReversedList.reverse()
        print(myReversedList == myList)
        return myReversedList == myList


if __name__=='__main__':
    print("Exercise 2")
    print()
    print()
    #testing invalid plaindrom tuple
    myTuple=(1, "banana", "cloud", 1, 2 , 3, 1, "banana", "0", 0, "1", "banana", "banana")
    print(myTuple)
    print()
    print()
    tupleIsPalindromFrequency(myTuple)
    print()
    print()
    #testing valid plaindrom tuple
    myTuple=(1, "banana", "cloud", "cloud", "banana", 1)
    print(myTuple)
    print()
    print()
    tupleIsPalindromFrequency(myTuple)
    print()
    print()

"""
Week 3 Tuples
3. Write a function to find the frequency of elements in a tuple, and return a dictionary mapping each element to its frequency.
"""

def tupleFrequency(myTuple):    
    myDict={}
    maxValue = 0
    maxKey = 0
    #catching if argument is not a tuple
    try:
        if (not(type(myTuple) is tuple)):
            raise Exception("Sorry, argument must be a tuple.")

    except Exception as e:
        print(e)
        
    else:
        #traversing the tuple
        for element in myTuple:
            #Building occurence histogram
            if element in myDict.keys():
                myDict[element]+=1 
            else:
                myDict[element]=1
            #Detecting the largest frequency
            if (maxValue<myDict[element]):
                maxValue=myDict[element]
                maxKey = element
        
    finally:
        return myDict
    
if __name__=='__main__':
    print("Exercise 3")
    print()
    myTuple=(1, "banana", "cloud", 1, 2 , 3, 1, "banana", "0", 0, "1", "banana", "banana")
    print(myTuple)
    print("Returning elements frequency")
    print(tupleFrequency(myTuple))
    print()
    print(5)
    print("Returning elements frequency")
    print(tupleFrequency(5))
    print()
    print()


"""
Week 3 Tuples
4. Write a function that takes a tuple as an argument and returns a new tuple with only the even elements from the original tuple.
"""
if __name__=='__main__':
    print("Exercise 4")
    print()
    myTuple=(1, "banana", "cloud", 1, 2 , 3, 1, "banana", "0", 0, "1", "banana", "banana")
    myEvenTuple = tuple(list(myTuple)[::2]) #casting the tuple into a list, iterating the even elements, and casting back as a new tuple
    print(myTuple)
    print("Returning even elements")
    print(myEvenTuple)
    print()
    print()

"""
Week 3 Tuples
5. Write a function to find all unique elements in a tuple and return them in a new tuple.
"""
if __name__=='__main__':
    print("Exercise 5")
    print()
    myTuple=(1, "banana", "cloud", 1, 2 , 3, 1, "banana", "0", 0, "1", "banana", "banana")
    myUniqueElementTuple = tuple(set(myTuple)) #casting the tuple into a set, and casting back as a new tuple
    print(myTuple)
    print("Returning unique elements")
    print(myUniqueElementTuple)
    print()
    print()
    
"""
End of file
Week 3 Tuples
"""