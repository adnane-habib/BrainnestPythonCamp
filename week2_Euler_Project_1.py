"""
Brainnest Python Training
April 2023
Adnane Habib
Team A6
"""
"""
Week 2 Euler_Project_1
1. If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
print("Exerise 1")
print()

if __name__ == '__main__':
    N = 1000;
    sum1000 = 0
    for i in range(N):
        if (i%3==0 or i%5==0 ):
            #print(i)
            sum1000 = sum1000+i 
            #print(i)
    print("The sum of all the multiples of 3 or 5 below 1000 is")
    print(sum1000)
    
print()
print()
#233168
"""
Week 2 Euler_Project_1
2. Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""
print("Exerise 2")
print()

def fibo(n): #fibonacci sequece recursive function
    if n<=0:
        return 0
    if n ==1:
        return 1
    if n ==2:
        return 2
    if n >2:
        return fibo(n-1)+fibo(n-2);
    else:
        return 0
if __name__ == '__main__':
    n = 0
    myFiboSum = 0
    flag = True
    myFibo=fibo(n)
    while flag:
        lastFibo = myFibo
        myFibo = fibo(n)
        if myFibo>=400000:
            flag = False
            continue
        elif myFibo%2==0:
            myFiboSum = myFiboSum+myFibo
        n=n+1
    print("We have reached the",n,"term. The corresponding series term is",lastFibo)
    print("The sum of the even-valued terms of Fibonacci sequence not exceededing 4 million is",myFiboSum)
    
print()
print()
#257114
"""
Week 2 Euler_Project_1
3. The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
print("Exerise 3")
print()

import math
if __name__ == '__main__':
    referenceNumber = 600851475143
    myUpperLimit = math.sqrt(referenceNumber)
    #using the same approach to resolve #9
    #we only need to consider numbers below square root of 600851475143
    myPrimes = [2, 3, 5, 7, 11, 13]
    index = 7
    number = 15
    N = myUpperLimit
    #suMyPrimes = sum(myPrimes)
    while number<=N:
        if referenceNumber%number==0:#we only consider those numbers that are factors of 600851475143
            for prime in myPrimes:
                if number%prime==0:
                    break
            else:
                myPrimes.append(number)#appends the number if prime
                index+=1
                 
        number+=2
    print(f"The largest primefactor of {referenceNumber} is")
    print(myPrimes[-1])
    
print()
print()
#6857
"""
Week 2 Euler_Project_1
4. A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
print("Exerise 4")
print()

def isPalindrom(number):
    paddedNumber = str(number)
    for i in range(len(paddedNumber)//2):
        if paddedNumber[i]!=paddedNumber[len(paddedNumber)-1-i]:
            return 0
    return 1

if __name__ == '__main__':
    maxRange = 999
    minRange = 100
    sumPalindroms = 0
    myList=[]
    for i in range(minRange,maxRange+1):
        for j in range(i,maxRange+1):
            number = i*j
            sumPalindroms += isPalindrom(number)
            myList.append(number*isPalindrom(number))
            
    """        
    sumPalindroms1 = 0
    myList1=[]
    for number in range(minRange*minRange,(maxRange+1)*(maxRange+1)):
        sumPalindroms1 += isPalindrom(number)
        myList1.append(number*isPalindrom(number))
    
    print("The total of plaindrom numbers between 10000 and 1000000 is:") #for debuging purposes
    print(sumPalindroms1)
    """
    print("The total of plaindrom numbers that are a product of 3 digit numbers is:")
    print(sumPalindroms)

    #print("1001 is plaindrom?",isPalindrom(1001))
    
print()
print()
#1239

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
    while index<N:
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
#104729

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

