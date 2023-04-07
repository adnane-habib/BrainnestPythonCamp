"""
Brainnest Python Training
April 2023
Adnane Habib
Team A6
"""
"""
Week 1
1. Write a program that prompts the user for a string and checks whether the string is a palindrome (i.e., the string reads the same forward and backward).
"""
def isPalindrome(word):
    #a function accepting a string checking that the string is a plaindrome
    for i, character in enumerate(word):
        #using enumerate to traverse the word through the character
        # and resevrseely using negative indexing
        #print(character) #debugging purposes
        #print(word[-i-1])#debugging purposes
        if (character!=word[-i-1]):
        #check if a charcter is different from its symmetric and return false
            #print(character) #debugging purposes
            #print(word[-i-1]) #debugging purposes
            #print("I am in the if loop")
            flag = False
            break #to exit the function without checking all the characters
#        """
#this part was present for debugging
        else:
            #print("I am in the else loop")
            flag = True #if the plaindrome is true
    #print("I am exiting the for loop")#for debugging purposes
#    """
    return flag

word = input("Enter a word: ")#reqeusting to input a string from the user
print("\n")
print(word,"is a palindrome?\n",isPalindrome(word))

"""
Week 1
Exercise 2
2. Write a program that takes in a list of integers and returns the sum of all 
"""
import random #load random library to generate random numbers
N = random.randint(1,100) #generating random list size
N=10
print(N)
myList=[]
for i in range(N):
    myList.append(random.randint(0,N)) #generating random integers list

def totalEven(aList):
    #a function to traverse the list and return the sum of all even integers
    sum = 0;
    for element in aList:
        if element%2==0:#testing if the element is even
            sum+=element #adding the element to the sume if even
    return sum
        
print(myList)
print(totalEven(myList))
