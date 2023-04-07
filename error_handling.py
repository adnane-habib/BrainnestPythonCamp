"""
Brainnest Python Training
April 2023
Adnane Habib
Team A6
"""
"""
Week 1 Error handling
1. Write a function that takes a list of integers as an argument, and returns the sum of the integers. 
   Use a try-except block to catch any ValueError exceptions that may be raised when attempting to convert a string to an integer.
"""
print("Welcome to our magic calculator system.") #greeting message
myList =[] #creating an empty list
word = "start"#initiating a variable that stores the entries
while word !="END":#setting a key word to stop accepting entries
    #prompting the user for entries
    word = input("Enter the next number, or type END to end the input: ")
    #appending the entry to the list
    myList.append(word)
myList.pop(-1) #popping the "END" keyword
print("This is the list of elements you have entered:")
print(myList)
#trying to cast the elements and catching any invalid entry
try:
    sum = 0
    for element in myList: #traversing the elements of the list
        sum+=int(element)
    print("The sum of the elements is:",sum)
except:
    print("At least one of the elements entered is not a valid number.")
#code exit message
finally:
    print("Thank you for using our services. See you soon.")


"""
Week 1 Error handling
2. Write a function that takes a filename as an argument, and attempts to open the file. 
   Use a try-except block to catch any FileNotFoundError exceptions that may be raised when attempting to open the file. 
   If the file is successfully opened, the function should return the contents of the file.
"""

print("Welcome to our magic file reading system.") #greeting message
#Prompting user to enter file name
myFile = input("Enter the file you wish to open: ")
#print("You have enetered ",myFile) #for debugging purposes
#Testing of the file can open
try:
    #opening the file for read
    reader = open(myFile,'r')
    print("Succesfully opened the file.\n\n")
#Catching file not found error
except FileNotFoundError as e:
    print('File does not exist:', e)
#Catching other type of errors
except Exception as e:
    print('An error occured: ', e)
#Processing the file data
else:    
    # for loop to skim through the file
    for line in reader:
        #print(reader.readline())
        print(line) #printing the line
    reader.close()#closing the file
#code exit message
finally:
    print("\n\nThank you for using our services. See you soon.")

"""
Week 1 Error handling
3. Write a function that takes a list of strings as an argument, and returns a new list containing only the strings that can be successfully converted to a float. 
   Use a try-except block to catch any ValueError exceptions that may be raised when attempting to convert a string to a float.
"""
myList = ["1", "2", "2.5", "four", "5.0"] #input list

def myListFLoatConversion(myList):
    #function definition
    myListFloat=[]#initiating empty list for floats
    print("You have entered")
    print(myList)
    #traversing the list 
    for element in myList:
        #testing if the element is a float and appending it
        try:
            myListFloat.append(float(element))
    #notigying that the element is not a float
        except:
            print(element,"is not a valid float")
    return myListFloat
print("Converted float")
#calling the function and printing the float elements
print(myListFLoatConversion(myList))

"""
Week 1 Error handling
4. Write a function that takes a list of dictionaries as an argument, and returns the value of a specified key from each dictionary. 
   Use a try-except block to catch any KeyError exceptions that may be raised when attempting to access a key that does not exist in a dictionary.
"""
def myDictValues(myDict, myKey):
    #function definition
    myListofValues=[]#initiating empty list for values

    
    #traversing the list 
    for myDict in mydicts:
        #testing if the element is a float and appending it
        try:
            myListofValues.append(myDict[myKey])
    #notigying that the element is not a float
        except KeyError as e:
            print("Key not found in one of the dictionires", e)
    return myListofValues


#defining a valid key
myKey = "banana"

#building list of dictionaries
dict1 = {"banana":11, "apple": 12, "orange":13}
dict2 = {"banana":21, "mango": 22, "orange":23}
dict3 = {"banana":31, "plum": 32, "mango":33}
mydicts=[dict1, dict2, dict3]
print("Let us look the values corresponding to",myKey)
#calling the function and printing the found elements
print(myDictValues(mydicts, myKey))

#defining a invalid key
myKey = 11
print("Let us look the values corresponding to",myKey)
#calling the function and printing the found elements
print(myDictValues(mydicts, myKey))

"""
Week 1 Error handling
5. Write a function that takes a list of integers as an argument, and returns the largest integer in the list. 
   Use a try-except block to catch any ValueError exceptions that may be raised when attempting to compare elements that are not integers.
"""
#declaring the list
myList = [1, -50, "1", 2, 55, 201, "One", -99]

def largestInteger(aList):
    #a function to traverse the list and return the largest element divisible by 3
    largestElement = float('-inf');#initiate the largest element to - infinity
    for element in aList:
        try:
            if largestElement<int(element):#testing if the element discovered is the largest
                largestElement=element #updating the largest element
        except ValueError as e:
            print("Value error, not an integer",e)
        
    return largestElement

#printing the list of elements        
print("The list is\n",myList)
#printing the function result
print("The lagest element in the list is:",largestInteger(myList))

"""
End of file
Week 1 Error handling
"""