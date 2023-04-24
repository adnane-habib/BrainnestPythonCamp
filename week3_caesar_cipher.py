"""
Brainnest Python Training
April 2023
Adnane Habib
Team A6
"""
"""
Week 3 caesar cypher
'''
'''
The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. It 
encrypts letters by shifting them over by a 
certain number of places in the alphabet. We 
call the length of shift the key. For example, if the 
key is 3, then A becomes D, B becomes E, C becomes 
F, and so on. To decrypt the message, you must shift 
the encrypted letters in the opposite direction. This 
program lets the user encrypt and decrypt messages 
according to this algorithm.

When you run the code, the output will look like this:

Do you want to (e)ncrypt or (d)ecrypt?
> e
Please enter the key (0 to 25) to use.
> 4
Enter the message to encrypt.
> Meet me by the rose bushes tonight.
QIIX QI FC XLI VSWI FYWLIW XSRMKLX.


Do you want to (e)ncrypt or (d)ecrypt?
> d
Please enter the key (0 to 26) to use.
> 4
Enter the message to decrypt.
> QIIX QI FC XLI VSWI FYWLIW XSRMKLX.
MEET ME BY THE ROSE BUSHES TONIGHT.
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

if __name__=='__main__':
    print("\n\n\n")
    
    print("---------------------------------------")
    print("---------------------------------------")
    print("Welcome to the Caesar cipher encryptor")
    print("---------------------------------------")
    print("---------------------------------------")
    print("-------Adnane Habib April 2023---------")
    print("\n\n\n")
    choice = ""
    while True:
        #menu choices
        choice = input("select an option from the following menu\n"
                   "1. (E)ncryption\n"
                   "2. (D)ncryption\n"
                   "3. (Q)uit\n\n")
        #encryption option
        if choice.lower()=="e":
            (word, key, direction) = userInput("encrypt")
            try: #capturing invalid choices
                int(key)
                int(direction)
                if direction!=0 and direction!=1:
                    raise Exception ("Invalid Direction")
            except Exception as e:
                print(myException)
                continue
            else: #processing valid entrise and priting result
                print("\n\n\n")
                print("Your encrypted message is\n")
                print(encryptor(word, key, direction))
                print("---------------------------------------")
                print("\n\n\n")
    
        #decryption option        
        elif choice.lower()=="d":
            (word, key, direction) = userInput("decrypt")
            try: #capturing invalid choices
                int(key)
                int(direction)
                if direction!=0 and direction!=1:
                    raise Exception ("Invalid Direction")
            except Exception as e:
                print(myException)
                continue
            else: #processing valid entrise and priting result
                print("\n\n\n")
                print("Your decrypted message is\n")
                print(decryptor(word, key, direction))
                print("---------------------------------------")
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
Week 2 caesar cypher
"""