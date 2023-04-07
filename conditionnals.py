"""
Week 1
Exercise 1
Write a program that prompts the user for a string and checks whether the string is a palindrome (i.e., the string reads the same forward and backward).
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
Exercise 1
Write a program that prompts the user for a string and checks whether the string is a palindrome (i.e., the string reads the same forward and backward).
"""