"""
Brainnest Python Training
April 2023
Adnane Habib
Team A6
"""
"""
Week 2 for_loop
1. Create a for loop that iterates through a list of strings and prints each string in uppercase.
"""
myStrings = ["Anaconda", "Vampire", "Loverly", "UPPER", "python", "java", "infographics"]
for word in myStrings: #traversing the list
    print(word.upper()) #.upper() method returns the string in upper case.

"""
Week 2 for_loop
2. Create a for loop that iterates through a list of numbers and prints the square of each number.
"""
import random #load random library to generate random numbers
M = 100 #range within which a random number will be generated
N = 15 #generating random list size
myList=[]
for i in range(N):
    myList.append(random.randint(0,M)) #generating random integers list

for i in myList:
    print("The square of",i, "is", pow(i,2)) #interating through the list and printing the square of each element

"""
Week 2 for_loop
3. Create a for loop that iterates through a list of dictionaries and prints the value of a specified key for each dictionary.
"""
myDict = {"banana": "1$", "apple": "2$", "kiwi": "4$", "pineapple": "6$", "avocado": "3.5"}
for keys, values in myDict.items():
    print("The price of",keys,"is",values)

"""
Week 2 for_loop
4. Create a for loop that iterates through a list of numbers and prints the largest number in the list.
"""
import random #load random library to generate random numbers
M = 100 #range within which a random number will be generated
N = 40 #generating random list size
myList=[]
for i in range(N):
    myList.append(random.randint(0,M)) #generating random integers list
largestNumber = myList[0] #initializing the parameter
for myNumber in myList:
    if (largestNumber<myNumber):
        largestNumber=myNumber
print("In the list of numbers")
print(*myList)
print("The largest number found is",largestNumber)

"""
Week 2 for_loop
5. Create a for loop that iterates through a list of lists and prints the sum of the elements in each sub-list.
"""
import random #load random library to generate random numbers
M = 100 #range within which a random number will be generated
N = 10 #generating random list size
P = 10 #setting the number of lists of lists
myList=[]
for i in range(P):
    myListTemp=[]
    for j in range(N):
        myListTemp.append(random.randint(0,M)) #generating random integers list
    myList.append(myListTemp) #appending the list into the list of lists
#print(myList) #printing the list of lists
myListSums=[]
for i in range(P):
    listSum=0
    for elements in myList[i]:#iterating through each list
        listSum+=elements #calculating the list sum
    myListSums.append(listSum) #building the list of lists sums
for i, list in enumerate(myList):
    print("the sum of the elements in ",*list )
    print("is",myListSums[i])
#print(*myListSums)

"""
End of file
Week 2 for_loop
"""

