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
        
print("The list is\n",myList)
print("The sum of even elements in the list is:",totalEven(myList))

"""
Week 1
3. Write a program that prompts the user for their age and checks whether they are old enough to vote (i.e., 18 years old or older).
"""

print("Welcome to our e-voting system.") #greeting message
M = input("Kindly enter your age: ") #prompting user for their input
#M = "18"

#wrapping the code in try except to avoid program crashing if invlid entry
try: 
    N = int(M)
    #checking if age is legal
    if N>=18:
        print("You are eligible to vote.")
    #if age is not illegal, printing message
    elif N>=0:
        print("You are not eligible to vote.")
    #ensuring that the age entered is in a valid range
    else:
        print("Please enter a valid age.")
#throwing exception if unable to cast input to integer
except:
    print("The age input is expected to be a positive number.")
#code exit message
finally:
    print("Thank you for using our services. See you soon.")

"""
Week 1
4. Write a program that takes in a list of integers and returns the largest number in the list that is also divisible by 3.
"""
import random #load random library to generate random numbers
N = random.randint(1,100) #generating random list size

print(N)
myList=[]
for i in range(N):
    myList.append(random.randint(0,N)) #generating random integers list

def largest3Divisible(aList):
    #a function to traverse the list and return the largest element divisible by 3
    largestElement = float('-inf');#initiate the largest element to - infinity
    for element in aList:
        if element%3==0:#testing if the element is divisble by 3
            if largestElement<element:#testing if the element discovered is the largest
                largestElement=element #updating the largest element
    return largestElement
        
print("The list is\n",myList)
print("The lagest element divisible by 3 in the list is:",largest3Divisible(myList))

"""
Week 1
5. Write a program that prompts the user for a number and checks whether the number is a prime number (i.e., only divisible by 1 and itself).
"""
print("Welcome to our prime checking system.") #greeting message
M = input("Kindly enter a positive integer to check: ") #prompting user for their input
#M = "10" #existing for debugging purposes
try:
    N = int(M)

    def isPrime(N):
        
        if N ==0 or N==1 or N==2 or N==3: #eliminating for the first 4 integers
            return True
        else: #veryfying if the number is divising by any of the numbers below it
            for i in range(2,N//2): #we only check the first half
                if N%i==0:
                    flag = False; #breaking the loop if the number is a factor
                    break;
                else:
                    
                    flag = True
            return flag
    #print(N)
    print(f"is {N} a prime number?")
    print(isPrime(N))
#throwing exception if unable to cast input to integer
except:
    print("The input is expected to be a positive number.")
#code exit message
finally:
    print("Thank you for using our services. See you soon.")

"""
End of file
"""