"""
Brainnest Python Training
April 2023
Adnane Habib
Team A6
"""
"""
Week 3 Euler_Project_2
1. Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

37107287533902102798797998220837590246510135740250 46376937677490009712648124896970078050417018260538 74324986199524741059474233309513058123726617309629 91942213363574161572522430563301811072406154908250 23067588207539346171171980310421047513778063246676 89261670696623633820136378418383684178734361726757 28112879812849979408065481931592621691275889832738 44274228917432520321923589422876796487670272189318 47451445736001306439091167216856844588711603153276 70386486105843025439939619828917593665686757934951 
62176457141856560629502157223196586755079324193331 64906352462741904929101432445813822663347944758178 92575867718337217661963751590579239728245598838407 58203565325359399008402633568948830189458628227828 80181199384826282014278194139940567587151170094390 35398664372827112653829987240784473053190104293586 86515506006295864861532075273371959191420517255829 71693888707715466499115593487603532921714970056938 
54370070576826684624621495650076471787294438377604 53282654108756828443191190634694037855217779295145 36123272525000296071075082563815656710885258350721 45876576172410976447339110607218265236877223636045 17423706905851860660448207621209813287860733969412 81142660418086830619328460811191061556940512689692 51934325451728388641918047049293215058642563049483 62467221648435076201727918039944693004732956340691 15732444386908125794514089057706229429197107928209 55037687525678773091862540744969844508330393682126 
18336384825330154686196124348767681297534375946515 80386287592878490201521685554828717201219257766954 78182833757993103614740356856449095527097864797581 16726320100436897842553539920931837441497806860984 48403098129077791799088218795327364475675590848030 87086987551392711854517078544161852424320693150332 59959406895756536782107074926966537676326235447210 69793950679652694742597709739166693763042633987085 
41052684708299085211399427365734116182760315001271 65378607361501080857009149939512557028198746004375 35829035317434717326932123578154982629742552737307 94953759765105305946966067683156574377167401875275 88902802571733229619176668713819931811048770190271 25267680276078003013678680992525463401061632866526 36270218540497705585629946580636237993140746255962 24074486908231174977792365466257246923322810917141 91430288197103288597806669760892938638285025333403 34413065578016127815921815005561868836468420090470 
23053081172816430487623791969842487255036638784583 11487696932154902810424020138335124462181441773470 63783299490636259666498587618221225225512486764533 67720186971698544312419572409913959008952310058822 95548255300263520781532296796249481641953868218774 76085327132285723110424803456124867697064507995236 37774242535411291684276865538926205024910326572967 23701913275725675285653248258265463092207058596522 
29798860272258331913126375147341994889534765745501 18495701454879288984856827726077713721403798879715 38298203783031473527721580348144513491373226651381 34829543829199918180278916522431027392251122869539 40957953066405232632538044100059654939159879593635 29746152185502371307642255121183693803580388584903 41698116222072977186158236678424689157993532961922 62467957194401269043877107275048102390895523597457 23189706772547915061505504953922979530901129967519 86188088225875314529584099251203829009407770775672 
11306739708304724483816533873502340845647058077308 82959174767140363198008187129011875491310547126581 97623331044818386269515456334926366572897563400500 42846280183517070527831839425882145521227251250327 55121603546981200581762165212827652751691296897789 32238195734329339946437501907836945765883352399886 75506164965184775180738168837861091527357929701337 62177842752192623401942399639168044983993173312731 
32924185707147349566916674687634660915035914677504 99518671430235219628894890102423325116913619626622 73267460800591547471830798392868535206946944540724 76841822524674417161514036427982273348055556214818 97142617910342598647204516893989422179826088076852 87783646182799346313767754307809363333018982642090 10848802521674670883215120185883543223812876952786 71329612474782464538636993009049310363619763878039 62184073572399794223406235393808339651327408011116 66627891981488087797941876876144230030984490851411 
60661826293682836764744779239180335110989069790714 85786944089552990653640447425576083659976645795096 66024396409905389607120198219976047599490197230297 64913982680032973156037120041377903785566085089252 16730939319872750275468906903707539413042652315011 94809377245048795150954100921645863754710598436791 78639167021187492431995700641917969777599028300699 15368713711936614952811305876380278410754449733078 
40789923115535562561142322423255033685442488917353 44889911501440648020369068063960672322193204149535 41503128880339536053299340368006977710650566631954 81234880673210146739058568557934581403627822703280 82616570773948327592232845941706525094512325230608 22918802058777319719839450180888072429661980811197 77158542502016545090413245809786882778948721859617 72107838435069186155435662884062257473692284509516 20849603980134001723930671666823555245252804609722 53503534226472524250874054075591789781264330331690
"""
print("Exercise 1")
print()
print()

mySum = sum([int(number) for number in "37107287533902102798797998220837590246510135740250 46376937677490009712648124896970078050417018260538 74324986199524741059474233309513058123726617309629 91942213363574161572522430563301811072406154908250 23067588207539346171171980310421047513778063246676 89261670696623633820136378418383684178734361726757 28112879812849979408065481931592621691275889832738 44274228917432520321923589422876796487670272189318 47451445736001306439091167216856844588711603153276 70386486105843025439939619828917593665686757934951 62176457141856560629502157223196586755079324193331 64906352462741904929101432445813822663347944758178 92575867718337217661963751590579239728245598838407 58203565325359399008402633568948830189458628227828 80181199384826282014278194139940567587151170094390 35398664372827112653829987240784473053190104293586 86515506006295864861532075273371959191420517255829 71693888707715466499115593487603532921714970056938 54370070576826684624621495650076471787294438377604 53282654108756828443191190634694037855217779295145 36123272525000296071075082563815656710885258350721 45876576172410976447339110607218265236877223636045 17423706905851860660448207621209813287860733969412 81142660418086830619328460811191061556940512689692 51934325451728388641918047049293215058642563049483 62467221648435076201727918039944693004732956340691 15732444386908125794514089057706229429197107928209 55037687525678773091862540744969844508330393682126 18336384825330154686196124348767681297534375946515 80386287592878490201521685554828717201219257766954 78182833757993103614740356856449095527097864797581 16726320100436897842553539920931837441497806860984 48403098129077791799088218795327364475675590848030 87086987551392711854517078544161852424320693150332 59959406895756536782107074926966537676326235447210 69793950679652694742597709739166693763042633987085 41052684708299085211399427365734116182760315001271 65378607361501080857009149939512557028198746004375 35829035317434717326932123578154982629742552737307 94953759765105305946966067683156574377167401875275 88902802571733229619176668713819931811048770190271 25267680276078003013678680992525463401061632866526 36270218540497705585629946580636237993140746255962 24074486908231174977792365466257246923322810917141 91430288197103288597806669760892938638285025333403 34413065578016127815921815005561868836468420090470 23053081172816430487623791969842487255036638784583 11487696932154902810424020138335124462181441773470 63783299490636259666498587618221225225512486764533 67720186971698544312419572409913959008952310058822 95548255300263520781532296796249481641953868218774 76085327132285723110424803456124867697064507995236 37774242535411291684276865538926205024910326572967 23701913275725675285653248258265463092207058596522 29798860272258331913126375147341994889534765745501 18495701454879288984856827726077713721403798879715 38298203783031473527721580348144513491373226651381 34829543829199918180278916522431027392251122869539 40957953066405232632538044100059654939159879593635 29746152185502371307642255121183693803580388584903 41698116222072977186158236678424689157993532961922 62467957194401269043877107275048102390895523597457 23189706772547915061505504953922979530901129967519 86188088225875314529584099251203829009407770775672 11306739708304724483816533873502340845647058077308 82959174767140363198008187129011875491310547126581 97623331044818386269515456334926366572897563400500 42846280183517070527831839425882145521227251250327 55121603546981200581762165212827652751691296897789 32238195734329339946437501907836945765883352399886 75506164965184775180738168837861091527357929701337 62177842752192623401942399639168044983993173312731 32924185707147349566916674687634660915035914677504 99518671430235219628894890102423325116913619626622 73267460800591547471830798392868535206946944540724 76841822524674417161514036427982273348055556214818 97142617910342598647204516893989422179826088076852 87783646182799346313767754307809363333018982642090 10848802521674670883215120185883543223812876952786 71329612474782464538636993009049310363619763878039 62184073572399794223406235393808339651327408011116 66627891981488087797941876876144230030984490851411 60661826293682836764744779239180335110989069790714 85786944089552990653640447425576083659976645795096 66024396409905389607120198219976047599490197230297 64913982680032973156037120041377903785566085089252 16730939319872750275468906903707539413042652315011 94809377245048795150954100921645863754710598436791 78639167021187492431995700641917969777599028300699 15368713711936614952811305876380278410754449733078 40789923115535562561142322423255033685442488917353 44889911501440648020369068063960672322193204149535 41503128880339536053299340368006977710650566631954 81234880673210146739058568557934581403627822703280 82616570773948327592232845941706525094512325230608 22918802058777319719839450180888072429661980811197 77158542502016545090413245809786882778948721859617 72107838435069186155435662884062257473692284509516 20849603980134001723930671666823555245252804609722 53503534226472524250874054075591789781264330331690".split()])
#we need to slice all the 100 50 digits numbers and then calculate their sum.
#For this purpose, we re using a list comprehension.
#Then we convert the sum into a string a slice it (firt 10 digits or last 10 digits).
print("The sum of the 100 50 digits numbers is:",mySum)
print("The first 10 digits of the sum of the 100 50 digits numbers is:",str(mySum)[0:10])
print("The last 10 digits of the sum of the 100 50 digits numbers is:",str(mySum)[-10:])

print()
print()
#5537376230
"""
Week 3 Euler_Project_2
2. 
The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even) n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence: 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), 
it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million..
"""
print("Exercise 2")
print()
print()


def collatz_sequence(n): #a function returning the collatz sequence for a specific number
    collatz = lambda i: i//2 if i%2==0 else 3*i+1 #lambda function to calculate the next number
    nbr = 1
    myList=[n]
    while n!=1:
        #print(n)
        n = collatz(n)
        myList.append(n)
        nbr+=1
    #print(n)
    return myList, nbr

def collatz_dict(n): # a dictionary of all colatz sequence for numbers below 1000000

    myDict={1:[1]}

    for i in range(2,n+1):
        if i in myDict.keys():
            continue
        else:
            myDict[i]=collatz_sequence(i)[0]
                       
    return myDict

def largestSequence(myDict): # function skimming through a dictionary to detext the largest list
    largestSequence = 0
    largestSequenceIndex = 0
    
    for key, value in myDict.items():
        if largestSequence<len(value):
            largestSequence, largestSequenceIndex=len(value), key
    return largestSequence, largestSequenceIndex         
    
    

myDict = collatz_dict(1000000)
print(largestSequence(myDict))#a tuple returning the largest collatz sequence length and its starting number

print()
print()
#837799

"""
Week 3 Euler_Project_2
3. 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?
"""
print("Exerise 3")
print()
#using list comprehension and casting
sum([int(i) for i in str(pow(2,1000))])
    
print()
print()
#1366
"""
Week 3 Euler_Project_2
4. If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
"""
    print("Exerise 4")
    print()

    mydict={'one':182, 'two':181, 'three':181,'four':181, 'five':181, 'six':181, 'seven':181, 'eight':181,'nine':181,
        'ten':10, 'eleven':10, 'twelve':10, 'thirteen':10, 'fourteen':10, 'fifteen':10, 'sixteen':10, 'seventeen':10, 'eighteen':10, 'nineteen':10,
        'twenty':100, 'thirty':100, 'forty':100, 'fifty':100, 'sixty':100, 'seventy':100, 'eighty':100, 'ninety':100,
        'and':891, 'hundred': 900, 'thousand':1}
    sumLetters = 0
    for key, value in mydict.items():
        sumLetters += len(key)*value
    print(sumLetters)
    print()
    print()
    #21124


"""
Week 2 Euler_Project_1
5. 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
print("Exerise 5")
print()

if __name__ == '__main__':
    myFactors = [7, 9, 11, 13, 15, 16, 17, 19, 20]#list of non-common factors

    i=20
    print("Let's find the number that is evenly divisible by")
    print(*myFactors)
    while True:
        i+=20 #since 20 is the largest factor, we can hop by 20
        for element in myFactors:
            if i%element!=0:
                break
        else:
            print("It is",i)
            break

    print("let us check it out.")
    for j in range(1,21): #this is a code for testing purposes
        print(f"{i} dividing by {j} is",i/j)
        
print()
print()
#232792560

"""
Week 2 Euler_Project_1
6. The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is, 3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
print("Exerise 6")
print()

N = 11
print(f"Let's first test for {N-1}")
#using list comphrenesion for the power 2 sum and the sum of power 2
print(pow(sum([i for i in range(N)]),2)-sum([pow(i,2) for i in range(N)]))
N = 101
print(f"Now let's do it for {N-1}")
print(pow(sum([i for i in range(N)]),2)-sum([pow(i,2) for i in range(N)]))

print()
print()
#25164150
            

"""
Week 2 Euler_Project_1
7. By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?
"""
print("Exerise 7")
print()

if __name__ == '__main__':
    myPrimes = [2, 3, 5, 7, 11, 13]
    index = 7
    number = 15
    N = 10001
    while index<=N:
        for prime in myPrimes:
            if number%prime==0:
                break
        else:
            myPrimes.append(number)#appends the number if prime
            index+=1
        number+=2
    print(f"The {index}st prime number is")
    print(myPrimes[-1])
    
print()
print()
#104743

"""
Week 2 Euler_Project_1
8. A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.
"""
print("Exerise 8")
print()

#Using a+b+c=1000 and a^2+b^2=c^2
#we can find out that a.b=(a+b-500)*1000.
#Hence, we need only to iterate a and b and check
# when this equality is met.
flag = False
for a in range(1,500):#since a+b+c=1000, therefore a<500
    for b in range(a, 500):#since a+b+c = 1000, therefore b<500
        if a*b==1000*(a+b-500):
            flag = True #to help us exit the outer loop
            break #first break to exist the inner loop
    if flag:#flag to exist the outer loop
            break
        
print("we found a=",a)
print("we found b=",b)
c = 1000-(a+b)
print("we found c",c)

print(f"a^2 ({a*a}) + b^2 ({b*b}) is equal to c^2 ({c*c})")
print()
print("The product of abc is",a*b*c)

print()
print()
#31875000

"""
Week 2 Euler_Project_1
9. The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""
print("Exerise 9")
print()

if __name__ == '__main__':
    myPrimes = [2, 3, 5, 7, 11, 13]
    index = 7
    number = 15
    N = 2000000
    suMyPrimes = sum(myPrimes)
    while number<=N:
        for prime in myPrimes:
            if number%prime==0:
                break
        else:
            myPrimes.append(number)#appends the number if prime
            index+=1
            suMyPrimes +=number 
        number+=2
    print(f"The sum of prime numbers beloww {N} is")
    print(suMyPrimes)
    
print()
print()
#142913828922

"""
Week 2 Euler_Project_1
10. The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""
print("Exerise 10")
print()

if __name__ == '__main__':
    pass

print()
print()
#

"""
End of file
Week 2 Euler_Project_1
"""

