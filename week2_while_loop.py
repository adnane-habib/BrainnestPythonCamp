"""
Brainnest Python Training
April 2023
Adnane Habib
Team A6
"""
"""
Week 2 while_loop
1. Create a while loop that repeatedly takes user input and adds the input to a list until the user enters "done".
"""
running_total = 0
running_index = 0
def entryCheck(dataEntry): #function checking if entry == done
    try:
        if (dataEntry.lower() =="done"):
            return True
        else:
            return False
    except:
        return False


flag = True
while flag: # while loop to prompt user for entries
    dataEntry = input("Enter a number or done to stop: ")
    if (entryCheck (dataEntry)): #catching if entry is not a number
        flag = False;
        break;
    else:
        try:
            running_total +=int(dataEntry)
        except Exception as e:
            print("Invalid entry. You have to enter a number or done to end the sequence.")
        else:
            running_index+=1
            print("Currently performed",running_index,"entries.") #displays running sum
            print("Running sum ",running_total)#display sequence running length
        
print("\n\n")
print("Overall sum is",running_total) #displays total sum
print("It is the sum of",running_index,"entries.") #display sequence length

"""
Week 2 while_loop
2. Create a while loop that generates random numbers and adds them to a list until the sum of all numbers in the list is greater than 100.
"""
import random #load random library to generate random numbers
M = 20 #range within which a random number will be generated
myList=[]
runningSum = 0
while runningSum<=100: #continuing the generation of random numbers until the condition is met
    n = random.randint(0,M) #generating a random number
    myList.append(n) #appending the number to the list to store it for future display
    runningSum += n #updating the running sum
print("You have reached 100. The sum of the random numbers generated is",runningSum)
print("The list of random numbers is:")
print(*myList)

"""
Week 2 while_loop
3. Create a while loop that repeatedly takes user input and appends it to a list, but only if the input is a unique string.
"""
def entryCheck(dataEntry): #function checking if entry == done
    try:
        if (dataEntry.lower() =="done"):
            return True
        else:
            return False
    except:
        return False
myList=[]

flag = True
while flag: # while loop to prompt user for entries
    dataEntry = input("Enter a new string, or done to stop")
    if (entryCheck (dataEntry)): #catching if entry is not a number
        print("Thank you for using our system.")
        flag = False;
        break;
    elif (dataEntry in myList): #considering if the string is unique 
        print(dataEntry,"has already been entered.")
        
    else:
        print(dataEntry,"is a new entry. It will be added to the list. The list contains now:")
        myList.append(dataEntry)
        print(*myList)
        print()
        
print("\n\n")
print("Overall elements of the list are: ") 
print(*myList) #displays the list elements

"""
Week 2 while_loop
4. Create a while loop that repeatedly takes user input and appends it to a list, but only if the input is a number greater than 10.
"""
def entryCheck(dataEntry): #function checking if entry == done
    try:
        if (dataEntry.lower() =="done"):
            return True
        else:
            return False
    except:
        return False

myList=[]
flag = True

while flag: # while loop to prompt user for entries
    dataEntry = input("Enter a number or done to stop: ")
    if (entryCheck (dataEntry)): #catching if entry is not a number
        flag = False;
        break;
    else:
        try:
            if (int(dataEntry)>10): # testing of the entry is a number greateer than 10
                myList.append(int(dataEntry))
        except Exception as e:
            print("Invalid entry. You have to enter a number or done to end the sequence.")

       
print("\n\n")
print("Overall elements of the list are: ") 
print(*myList) #displays the list elements


"""
Week 2 while_loop
5. Create a while loop that repeatedly takes user input and keeps track of the highest number entered until the user enters "done".
"""
import math
def entryCheck(dataEntry): #function checking if entry == done
    try:
        if (dataEntry.lower() =="done"):
            return True
        else:
            return False
    except:
        return False

myList=[]
myLargest = -math.inf #considering minus infinity to initialize the largest number.
flag = True
while flag: # while loop to prompt user for entries
    dataEntry = input("Enter a number or done to stop: ")
    if (entryCheck (dataEntry)): #catching if entry is not a number
        flag = False;
        break;
    else:
        try:
            if (myLargest <int(dataEntry)):
                myLargest =int(dataEntry)
            myList.append(int(dataEntry))
        except Exception as e:
            print("Invalid entry. You have to enter a number or done to end the sequence.")
        else:
            running_index+=1
            print("Currently the largest number is",myLargest) #displays the current largest number
            
        
print("\n\n")
print("Overall largest number is",myLargest) #displays the largest entry
print("The overall sequence entered is:") 
print(*myList)#display overall sequence

"""
End of file
Week 2 while_loop
"""

