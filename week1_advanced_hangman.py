myAlphabet =("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")

word = "AlphaBlondie"

guessedWord = ["*"]*len(word)

attempts = 3

def myWordDict(word):
    myWordDict={}
    #traversing the word to build the word characters position dictionary
    for i, char in enumerate(word.lower()):
        #updating the character position list
        if char in myWordDict.keys():            
            myWordDict[char].append(i)
        #creating the character position list
        else:
            myWordDict[char]=[i]
    return myWordDict

myWordReference = myWordDict(word)
print("Welcome to the Hangman thrilling game.")
print("Try to guess this word.")
print("You have",attempts,"attempts.")
print("The more you have good guesses, the more attempts you get!")

def updateString(listWord, character, position):
    for index in position:
        listWord[index] = character
    return listWord

print(*guessedWord)
attempt = 0
while attempts !=0:
    character = input("Enter a character: ")
    attempt +=1
    try:
        if not(character.lower() in myAlphabet):
            print("The system detected that the character is invalid")            
            raise Exception("Sorry, You have to enter only 1 valid character")
    except Exception as e:
        print(e)
        continue
    else:
        if character in guessedWord:            
            print("Already guessed before!")
            attempts-=1
        
        elif character in myWordReference:
            guessedWord = updateString(guessedWord, character, myWordReference[character])
            print("Good guess!")
            attempts+=1
            
        else:
            print("Wrong guess!")
            attempts-=1
        print(*guessedWord)
        
    finally:
        if not("*" in guessedWord):
            print("Contraluation! You won")
            break
        elif attempts == 0:
            print("Sorry! You have no more attempts.")
            break
        else:            
            print("You still have",attempts,"attempts.")
            decision = input("Do you want to continue? Y // N: ")

            if decision.lower()=="n":
                break
            else:
                pass
   


print("The word to guess is")
print(word)
print("You made",attempt,"attempts.")