"""
Brainnest Python Training
April 2023
Adnane Habib
Team A6
"""
"""
Week 4 sets
1. Given two sets A and B, write a function to return the symmetric difference between them as a new set. 
The symmetric difference is the set of elements that are in either A or B, but not in both.
"""
print("Exercise 1")
print()
print()

setA = {1, 2, 4, 6, 77, 89, 564}
setB = {-1, 2, 4, 6, 9, 89, 264}
print("Set A elements are",setA)
print("Set B elements are",setB)
unionAB = setA.union(setB)
#print("Union set of A and B elements are",unionAB)
intersectAB = setA.intersection(setB)
#print("Intersection set of A and B elements are",intersectAB)
diffA_B = setA.difference(setB)
#print("Set A minus B elements are",diffA_B)
diffB_A = setB.difference(setA)
#print("Set A minus B elements are",diffB_A)
symmetricDiffA_B = diffA_B.union(diffB_A)

print("Set of symmetric difference of A and B elements are",symmetricDiffA_B)
print()
print()
#{1, 564, 264, 9, 77, -1}

"""
Week 4 sets
2. Given a list of numbers, write a function to return a set of all prime numbers from the list..
"""
print("Exercise 2")
print()
print()

import random #load random library to generate random numbers
M = 100 #range within which a random number will be generated
N = 15 #generating random list size
mySet=set()
mySetOfPrimes=()
for i in range(N):
    mySet.add(random.randint(0,M)) #generating random integers set

print("The set of integers is")
print(mySet)

mySetOfPrimes = {2, 3, 5, 7, 11, 13}

for element in mySet:
    for prime in mySetOfPrimes:
        if element%prime==0:
            break
    else:
        mySetOfPrimes.add(element)#appends the number if prime
print()       
print("The resulting set of primes is")
print(mySetOfPrimes)

print()
print()
#{0, 32, 35, 36, 45, 79, 20, 21, 85, 24, 25, 59, 60, 30}
#{2, 3, 5, 7, 11, 13, 79, 59}

"""
Week 4 sets
3. Given a list of words, write a function to return a set of all anagrams in the list.
"""

print("Exercise 3")
print()
print()

from os.path import dirname, join
current_dir = dirname(__file__)
file_path = join(current_dir, "./common_words.txt")

myAnagramList =[]
checkedWordsSet = set()
mySetofWords = set()
try:
    with open(file_path) as commonWordFiles:#reading from a list of +4000 words
        for referenceWord in commonWordFiles:
            mySetofWords.add(referenceWord.strip('\n'))
except:
    print("ERROR reading \'common_words.txt\' file. make sure to copy the file common_words in the same directory.")

else:    
    for referenceWord in mySetofWords:#iterating the set of words

        if referenceWord in checkedWordsSet:
            continue
        runningSet={referenceWord}#creating a temporary set of reference word anagrams
        checkedWordsSet.add(referenceWord)#updating the list of checked words, to avoid double check
        for runningWord in mySetofWords:#traversing the list to check for anagrams
            if runningWord in checkedWordsSet:
                continue
            if sorted(referenceWord.lower())==sorted(runningWord.lower()):#checking anagrams
                runningSet.add(runningWord)#updating the set of word anagrams
                checkedWordsSet.add(runningWord)#updating the set of checked words
        myAnagramList.append(runningSet)#updating the list of sets of anagrams
            
    #print(myAnagramList)
    #print(checkedWordsSet)
    #print(mySetofWords)
    print("the sets of anagram words in the list of words provided are")
    print([myAnagram for myAnagram in myAnagramList if len(myAnagram)>1])

print()
print()
'''
[{'south', 'shout'}, {'eat', 'tea'}, {'steak', 'stake'}, {'eager', 'agree'}, {'last', 'salt'}, {'read', 'dare', 'dear'}, {'wake', 'weak'},
{'creation', 'reaction'}, {'region', 'ignore'}, {'art', 'rat'}, {'DNA', 'and'}, {'broad', 'board'}, {'marker', 'remark'}, {'pat', 'tap'},
{'waste', 'sweat'}, {'sacred', 'scared'}, {'feel', 'flee'}, {'form', 'from'}, {'skin', 'sink'}, {'conversation', 'conservation'}, {'nerve', 'never'},
{'hate', 'heat'}, {'live', 'evil'}, {'diet', 'edit', 'tide'}, {'fear', 'fare'}, {'danger', 'garden'}, {'generate', 'teenager'}, {'idea', 'aide'},
{'anger', 'range'}, {'terrain', 'trainer'}, {'phase', 'shape'}, {'sue', 'use'}, {'please', 'asleep'}, {'three', 'there'}, {'opt', 'top', 'pot'}, {'deal', 'lead'},
{'super', 'purse'}, {'meal', 'male'}, {'angel', 'angle'}, {'user', 'sure'}, {'item', 'time'}, {'thus', 'shut'}, {'net', 'ten'}, {'however', 'whoever'},
{'credit', 'direct'}, {'mean', 'name'}, {'horse', 'shore'}, {'eighth', 'height'}, {'dog', 'God'}, {'lamp', 'palm'}, {'leader', 'dealer'}, {'ah', 'ha'},
{'early', 'layer'}, {'gallery', 'largely'}, {'sale', 'seal'}, {'state', 'taste'}, {'marine', 'remain'}, {'mad', 'dam'}, {'pool', 'loop'}, {'foster', 'forest'},
{'trial', 'trail'}, {'review', 'viewer'}, {'lean', 'lane'}, {'now', 'own'}, {'recent', 'center'}, {'tear', 'rate'}, {'tough', 'ought'}, {'rare', 'rear'},
{'file', 'life'}, {'reverse', 'reserve'}, {'former', 'reform'}, {'dream', 'armed'}, {'being', 'begin'}, {'silence', 'license'}, {'arise', 'raise'},
{'rescue', 'secure'}, {'source', 'course'}, {'thing', 'night'}, {'care', 'race'}, {'slot', 'lots', 'lost'}, {'pit', 'tip'}, {'note', 'tone'}, {'blow', 'bowl'},
{'its', 'sit'}, {'stream', 'master'}, {'era', 'ear'}, {'permission', 'impression'}, {'teach', 'cheat'}, {'setting', 'testing'}, {'bread', 'beard'}, {'alter', 'later'},
{'hint', 'thin'}, {'shelf', 'flesh'}, {'quiet', 'quite'}, {'introduce', 'reduction'}, {'sole', 'lose'}, {'meat', 'mate', 'team'}, {'react', 'trace'}, {'could', 'cloud'},
{'heart', 'earth'}, {'spot', 'post', 'stop'}, {'shot', 'host'}, {'this', 'shit'}, {'grin', 'ring'}, {'worth', 'throw'}, {'sign', 'sing'}, {'tale', 'late'},
{'rebuild', 'builder'}, {'fiber', 'brief'}, {'these', 'sheet'}, {'plane', 'panel'}, {'least', 'steal'}, {'icon', 'coin'}, {'below', 'elbow'}, {'earn', 'near'},
{'sneak', 'snake'}, {'brake', 'break'}, {'east', 'seat'}, {'dad', 'add'}, {'silent', 'listen'}, {'drawer', 'reward'}, {'march', 'charm'}, {'green', 'genre'}, {'resist', 'sister'},
{'trap', 'part'}, {'bare', 'bear'}, {'gear', 'rage'}, {'cause', 'sauce'}, {'flow', 'wolf'}, {'how', 'who'}, {'expect', 'except'},
{'resign', 'singer'}, {'route', 'outer'}, {'war', 'raw'}, {'cat', 'act'}, {'leap', 'plea', 'pale'}]
'''

"""
Week 4 sets
4. Given a list of sets, write a function to return the Cartesian product of all sets in the list.
"""
print("Exercise 4")
print()
print()

import itertools
setA = set('adnanehabib')
setB = set(list(range(10)))
setC = {True, False}
print("The sets elements are")
print(setA)
print(setB)
print(setC)
print()
myListSets = [setA, setB, setC]
myCartezianProduct = itertools.product(*myListSets)


myCartezianSet=set()
for element in myCartezianProduct:
    myCartezianSet.add(element)

print("The cartezian product of the sets is")
print(myCartezianSet)
print()
print()
'''
{('a', 3, False), ('e', 5, False), ('n', 5, True), ('b', 8, True), ('n', 6, True),('h', 9, False), ('d', 2, False), ('a', 0, False), ('i', 0, True), ('d', 1, False),
('h', 7, False), ('i', 9, True), ('e', 8, True), ('h', 0, False), ('b', 4, True),('b', 3, True), ('a', 8, True), ('e', 2, True), ('i', 7, False), ('n', 0, False),
('a', 2, True), ('e', 4, True), ('a', 5, True), ('e', 7, True), ('i', 2, False), ('n', 7, False), ('h', 8, True), ('d', 3, True), ('d', 4, True), ('i', 1, False),
('h', 6, True), ('h', 5, True), ('b', 1, False), ('b', 2, False), ('h', 3, True), ('d', 8, True), ('n', 8, True), ('b', 7, False), ('a', 7, False), ('e', 1, False),
('n', 1, True), ('n', 2, True), ('d', 6, False), ('a', 4, False), ('e', 6, False), ('i', 3, True), ('i', 4, True), ('d', 5, False), ('a', 1, False), ('n', 4, True),
('d', 0, False), ('b', 9, True), ('h', 4, False), ('b', 0, True), ('h', 1, False), ('i', 8, True), ('h', 2, False), ('d', 9, False), ('e', 9, True), ('n', 9, False),
('b', 6, True), ('b', 5, True), ('a', 6, True), ('e', 0, True), ('a', 9, True), ('e', 3, True), ('i', 6, False), ('n', 3, False), ('d', 7, True), ('i', 5, False),
('n', 6, False), ('a', 0, True), ('a', 3, True), ('e', 5, True), ('i', 0, False), ('n', 5, False), ('d', 1, True), ('b', 8, False), ('h', 9, True), ('d', 2, True),
('h', 0, True), ('h', 7, True), ('i', 9, False), ('b', 3, False), ('e', 8, False), ('b', 4, False), ('a', 8, False), ('e', 2, False), ('i', 7, True), ('a', 5, False),
('e', 7, False), ('n', 7, True), ('n', 0, True), ('d', 4, False), ('a', 2, False), ('e', 4, False), ('i', 1, True), ('i', 2, True), ('h', 8, False), ('d', 3, False),
('h', 5, False), ('h', 6, False), ('b', 2, True), ('h', 3, False), ('b', 1, True), ('d', 8, False), ('n', 8, False), ('b', 7, True), ('n', 2, False), ('a', 4, True),
('e', 6, True), ('a', 7, True), ('e', 1, True), ('i', 4, False), ('n', 1, False), ('d', 5, True), ('d', 6, True), ('i', 3, False), ('n', 4, False), ('b', 9, False),
('a', 1, True), ('h', 4, True), ('d', 0, True), ('i', 8, False), ('h', 2, True), ('b', 0, False), ('e', 9, False), ('h', 1, True), ('d', 9, True), ('n', 9, True),
('b', 5, False), ('a', 9, False), ('b', 6, False), ('e', 3, False), ('n', 3, True), ('a', 6, False), ('e', 0, False), ('i', 5, True), ('i', 6, True), ('d', 7, False)}
'''

"""
End of file
Week 4 sets
"""

