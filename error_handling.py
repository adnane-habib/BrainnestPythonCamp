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
End of file
Week 1 Error handling
"""