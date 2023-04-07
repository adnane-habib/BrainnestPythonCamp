"""
Brainnest Python Training
April 2023
Adnane Habib
Team A6
"""
"""
Week 1 Error handling
1. Write a function that takes a list of integers as an argument, and returns the sum of the integers. 
   Use a try-except block to catch any ValueError exceptions that may be raised when attempting to convert a string to an integer..
"""
print("Welcome to our magic calculator system.") #greeting message
myList =[] #creating an empty list
word = "start"#initiating a variable that stores the entries
while word !="END":#setting a key word to stop accepting entries
    #prompting the user for entries
    word = input("Enter the next number, or press END to end the input: ")
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
End of file
Week 1 Error handling
"""