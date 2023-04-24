"""
Brainnest Python Training
April 2023
Adnane Habib
Team A6
"""
"""
Week 3 caesar cracker
'''
'''
This program can hack messages encrypted 
with the Caesar cipher from the previous project, even 
if you don’t know the key. There are only 26 
possible keys for the Caesar cipher, so a computer can easily try all possible decryptions and display the results to the user. In cryptography, we call 
this technique a brute-force attack.
'''
"""

#functions for encrypting and decrypting message
#user can choose the encryption key (0~26)
#and the encryption direction (left or right)

def encryptor(word, key = 0, direction = 0):#encrpytion function
    alphabet='abcdefghijklmnopqrstuvwxyz'#alphabet list
    mylist=range(26)#indices list
    mydict=dict(zip(alphabet,mylist))#alphabet dictionary
    encryptedWord = ""
    
    try:
        indexShift = int(key)#ensuring key is valid
        if direction==0:#shifting key based on direction
            pass
        else :
            indexShift = 26-indexShift        
    except :
        print("Invalid shifting key")
        return word
    else:
        #detecting the new letter based on the current letter and the shift key
        #detecting the existing key, capturing its index, shifting the index with the key
        #detecting the new letter based on the new key and appending it to the word
        for letter in word.lower():
        #if a special character, it will not change
            if letter in mydict.keys():
                encryptedWord+=(alphabet[(mydict[letter]+indexShift)%26]).upper()
            else:
                encryptedWord+=letter.upper()
        return encryptedWord
    

def decryptor(encryptedWord, key, direction = 0):
    #decryption is a simple encryption in the other direction
    return encryptor(encryptedWord, 26-key, 0)

def userInput(option):
    #function to manage user input, word, key, direction
    word = input(f"Enter the word to {option}:\n")
    key = int(input ("Enter the key:\n"))
    direction = int(input("Enter the encryption direction \n(0) for right and(1) for left\n"))             
                
    return (word, key, direction)
"""
#block for testing purposes only
word = "Meet me by the rose bushes tonight."
key = 4
direction = 0

encryptedWord = encryptor(word, key, direction)
print(word)
print(encryptedWord)
decryptedWord = decryptor(encryptedWord, key, direction)
print(decryptedWord)
"""
myException = "Keys must be between 0 and 25,\n"+"Direction must be 0 for right and 1 for left."
#standard error message
N = 26
if __name__=='__main__':
    print("\n\n\n")
    
    print("---------------------------------------")
    print("---------------------------------------")
    print("-Welcome to the Caesar cipher cracker--")
    print("---------------------------------------")
    print("---------------------------------------")
    print("-------Adnane Habib April 2023---------")
    print("\n\n\n")
    choice = ""
    while True:
        #menu choices
        choice = input("select an option from the following menu\n"
                   "1. (C)racking\n"
                   "2. (Q)uit\n\n")
        #cracking option
        if choice.lower()=="c":
            word = input("Enter the code you wish to crack:\n")
            print("Brute force cracking\n\n")
            for i in range(N):
                print("Trial #",i+1)
                print(encryptor(word, i, 0))   
            print("\n\n\n")

        #exit option        
        elif choice.lower()=="q":
            break
        #invalid entry handling
        else:
            print("Please enter a valid choice\n\n")
    #Greeting message
    print("\n\n\n")
    print("---------------------------------------")
    print("Thank you for using our services.")
    print("---------------------------------------")
    print("---------------------------------------")
    print("-------Adnane Habib April 2023---------")
    
 

"""
End of file
Week 2 caesar cracker
"""