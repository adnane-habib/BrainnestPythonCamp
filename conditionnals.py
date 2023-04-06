def isPalindrome(word):
    #a function accepting a string checking that the string is a plaindrome
    for i, character in enumerate(word):
        #using enumerate to traverse the word through the character
        # and resevrseely using negative indexing
        if (character!=word[-i-1]):
        #check if a charcter is different from its symmetric and return false
            #print(character) #debugging purposes
            #print(word[-i-1]) #debugging purposes
            return False
        """
#this part was present for debugging
        else:
            print("I am in the else loop")
            flag = True #if the 
    print("I am in the existing the for loop")
    """
    return True

word = input("Enter a word: ")#reqeusting to input a string from the user
#print(isPalindrome("HelloolleH"))
print("\n")
print(word,"is a palindrome?\n",isPalindrome("HelloolleH"))
