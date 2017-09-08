"""
CS 141 Project 1

Your Name: Nathanial Hapeman
Your Student ID: 860 885262
Revision history:    ?
"""
import sys
import math
#import time  # used for testing and seeing recursive steps
from copy import  deepcopy

################################################################################
##########################   class helper functions   ##########################   
################################################################################
   

# I figure why create a bunch of class objects recursively when you can take 
# the important part (the array) and just work with those and minimize the 
# overhead for creating another object. So these functions just reduce the used
# memory and even make my functions faster since it takes time to declare a
# new class object

################################################################################
# used to multiply arrays with one value
def times( arrX, arrY ):
    product=arrX[0]*arrY[0]
    return [product / 10, product % 10]
    
################################################################################
#returns the sum of self and other for arrays only
def addArrs(arr1,arr2):
    
    # reverse so not appending onto front of array. rather back
    arr1.reverse()
    arr2.reverse()
    
    #apply summation from smallest to largest integer. Carry sum
    #this method minimizes runtime by adding only necessary #'s
    if len(arr1) >= len(arr2):
        returnThis=deepcopy(arr1)
        for digit in range(len(arr2)):
            tempNum=returnThis[digit]+arr2[digit]
            if tempNum > 9 and len(returnThis) -1 !=digit :    
                returnThis[digit+1]+=1
            elif tempNum > 9:
                returnThis.append(1)
            returnThis[digit]= tempNum%10
        lastDig=len(arr2)
        while len(returnThis) > lastDig and returnThis[lastDig] == 10:
            returnThis[lastDig]=0
            if len(returnThis)-1 == lastDig:
                returnThis.append(1)
            else:
                returnThis[lastDig+1]+=1
            lastDig+=1
    #apply summation from smallest to largest integer. Carry sum 
    #this method minimizes runtime by adding only necessary #'s     
    else:
        returnThis=deepcopy(arr2)
        for digit in range(len(arr1)):
            tempNum=returnThis[digit]+arr1[digit]
            if tempNum > 9 and len(returnThis) -1 !=digit :
                returnThis[digit+1]+=1
            elif tempNum > 9:
                returnThis.append(1)
            returnThis[digit]= tempNum%10
        lastDig=len(arr1)
        while len(returnThis) > lastDig and returnThis[lastDig] == 10:
            returnThis[lastDig]=0
            if len(returnThis)-1 == lastDig:
                returnThis.append(1)
            else:
                returnThis[lastDig+1]+=1
            lastDig+=1
        
            
    # reverse back to normal state
    arr1.reverse()
    arr2.reverse()
    returnThis.reverse()
    
    #return sum
    return returnThis
################################################################################
# used to subtract arrays

def subArrs(arr1, arr2):
    # first of all arr1 is presumed to be larger than arr2
    # so the result when subtracting arr1- arr2 will be positive

    

    # getting rid of leading zeros for arr2
    l1=0
    for l1 in range(len(arr2)):
        if(arr2[l1]!=0):
            break
    arr2=[arr2[i+ l1] for i in range(len(arr2)-l1)]

    
    # make copy of arr1 and return it
    returnMe=deepcopy(arr1)
    
    # reverse it for increase array functionality
    returnMe.reverse()
    arr2.reverse()
    for i in range(len(arr2)):
        temp=returnMe[i]-arr2[i]
        if temp < 0:
            returnMe[i]=temp+10
            itt=i+1
            # this is for the carry!
            while True:
                tempCurry=returnMe[itt]-1
                if tempCurry < 0:
                    returnMe[itt]=9
                else:
                    returnMe[itt]-=1
                    break
                itt+=1
        else:
            returnMe[i]=temp
    
    # reverse it back for regular functioning
    returnMe.reverse()
    arr2.reverse()
    
    return returnMe

################################################################################
def aModN(a,n):
    
    # declaring vars
    nTimes= BigInt(str(n))
    lastN=BigInt(0)
    #incrementing n till exceeds a
    while nTimes <= a:
        lastN = nTimes
        nTimes=nTimes+n
        
    # getting remainder
    nTimes.number=subArrs(a.number , lastN.number )
    
    # getting rid of leading zeros
    l1=0
    for l1 in range(len(nTimes.number)):
        if(nTimes.number[l1]!=0):
            break
    temp1=[nTimes.number[i+ l1] for i in range(len(nTimes.number)-l1)]
    #set number to modified return vector
    nTimes.number=temp1
    
        
    return nTimes

#computes a+b (mod n)
def mod_add(a,b,n):  
    # these functions are easy when you implemented
    # the basic mod operator on the bigint class
    tempA=aModN(a,n)
    tempB=aModN(b,n)
    sum = tempB+tempA
    tempC=aModN(sum, n)
    
    return tempC
    


#computes ab (mod n)
def mod_mul(a,b,n):
    # these functions are easy when you implemented
    # the basic mod operator on the bigint class
    tempA=aModN(a,n)
    tempB=aModN(b,n)
    sum = tempB*tempA
    tempC=aModN(sum, n)
    
    return tempC

#computes a^b (mod n)
def mod_exp(a,b,n):
    pass

############################################# one of my error checks 
def testIfNeg(x):
        if x < 0:
            raise ValueError, "I do not handle negative numbers!"
        return x
    
# the recursive part of the multiplication algorithm
def karatsuba(arrX, arrY):
    
    
    # which array is larger?
    lenSelf = len(arrX)
    lenOther = len(arrY)
    length = max(lenSelf, lenOther)
    
    # if you dont pad the vectors to the same length you will end up
    # having a vector with empty elements that gets passed recursively and
    #causes an infinite loop
    
    # make arrays same length and only pad to array that needs it
    if lenSelf < lenOther:
        arrX=  [0 for _ in range(len(arrX) , length)] + arrX
    else:
        arrY=  [0 for _ in range(len(arrY) , length)] + arrY
        
    # this is my base case
    if lenSelf ==1 and lenOther == 1:
        return times(arrX, arrY)
    
    
    # Split arrays for recursion
    halfLen = (length + 1) / 2
    arrX1 = arrX[ : halfLen]
    arrX2 = arrX[halfLen : ]
    arrY1 = arrY[  : halfLen]
    arrY2 = arrY[ halfLen :  ]


    # z0 = p0 || z2 = p2 ||  z1 = p1 - p0 - p2.
    z0 = karatsuba(arrX1, arrY1)
    z2 = karatsuba(arrX2, arrY2)
    p1 = karatsuba(addArrs(arrX1, arrX2), addArrs(arrY1, arrY2))
    z1 = subArrs(p1, addArrs(z0, z2))
    

    # From these results, compute z0 b^(2m) + z1 b^m + z2.  We separate out
    # each of these operations.
    z0prod = z0 + [0 for _ in range(0, 2 * length/2)]
    z1prod = z1 + [0 for _ in range(0, length/2)]
    z2prod = z2

    return addArrs(addArrs(z0prod, z1prod), z2prod)

###############################################################################
#############################   BigInt Class   ################################
###############################################################################
class BigInt:
    ###########################################################
    # constructs a new BigInt objects for integer x
    def __init__(self, x=0):
        #test if number is negative. make positive if so
        try:
            testIfNeg(x)
        except ValueError:
            print "\nERROR: DON'T ENTER NEGATIVE NUMBERS!"
            print "I made " + str(x) + " positive\n"
            x=x*-1
        #turn number into array
        self.number= []
        for digit in str(x):
            self.number.append(int(digit))
        self.value=x;
        #don't need return value
        return None
    
    ###########################################################
    def __str__(self):
        # returns the string representation of a BigInt number            
        return ( ''.join(str(digit) for digit in self.number) )

    # returns a negative integer if self < other, zero if self ==
    # other, a positive integer if self > other
    
    ###########################################################
    def __cmp__(self, other):
         
        # this try catch checks for negative number is subtract
        # negative number means other > self
        try:
            getThisValue= subArrs(self.number, other.number)
        except IndexError:
            return -1
        
        
        # getting rid of leading zeros for self
        l1=0
        for i in range(len(getThisValue)):
            if(getThisValue[i]==0):
                l1+=1
            
        # testing if numbers are equal
        if l1 == len(getThisValue):
            return 0
        
        return 1
        
        
    ###########################################################  
    #returns the sum of self and other
    def __add__(self, other):
        #error catching wrong classs
        try:
            if not isinstance(other, BigInt):
                raise RuntimeError( 'I only handle BigInts')
        except RuntimeError:
            print "Error: You entered the wrong class.. exiting"
            sys.exit(0)
        
        # reverse so not appending onto front of array. rather back
        self.number.reverse()
        other.number.reverse()
        
        #apply summation from smallest to largest integer. Carry sum
        #this method minimizes runtime by adding only necessary #'s
        if len(self.number) >= len(other.number):
            returnThis=deepcopy(self)
            for digit in range(len(other.number)):
                tempNum=returnThis.number[digit]+other.number[digit]
                if tempNum > 9 and len(returnThis.number) -1 !=digit :    
                    returnThis.number[digit+1]+=1
                elif tempNum > 9:
                    returnThis.number.append(1)
                returnThis.number[digit]= tempNum%10
            lastDig=len(other.number)
            while len(returnThis.number) > lastDig and returnThis.number[lastDig] == 10:
                returnThis.number[lastDig]=0
                if len(returnThis.number)-1 == lastDig:
                    returnThis.number.append(1)
                else:
                    returnThis.number[lastDig+1]+=1
                lastDig+=1
        #apply summation from smallest to largest integer. Carry sum 
        #this method minimizes runtime by adding only necessary #'s     
        else:
            returnThis=deepcopy(other)
            for digit in range(len(self.number)):
                tempNum=returnThis.number[digit]+self.number[digit]
                if tempNum > 9 and len(returnThis.number) -1 !=digit :
                    returnThis.number[digit+1]+=1
                elif tempNum > 9:
                    returnThis.number.append(1)
                returnThis.number[digit]= tempNum%10
            lastDig=len(self.number)
            while len(returnThis.number) > lastDig and returnThis.number[lastDig] == 10:
                returnThis.number[lastDig]=0
                if len(returnThis.number)-1 == lastDig:
                    returnThis.number.append(1)
                else:
                    returnThis.number[lastDig+1]+=1
                lastDig+=1
            
                
        # reverse back to normal state
        self.number.reverse()
        other.number.reverse()
        returnThis.number.reverse()
        
        #return sum
        return returnThis
    
    ###########################################################
    # this serves as a mask for a bit operation
    def makeZero(self):
        self.number[0]=0
        return None
        
    ###########################################################
    # makes multiplication possible for bigint class  
    def __mul__(self, other):
        
        
        # first pad numbers
        num1= pow(2, math.ceil(math.log(len(self.number),2)))
        num2= pow(2, math.ceil(math.log(len(other.number),2)))
        padBy= max(num1, num2)
        
        pad=BigInt(int(pow(10,padBy-1)))
        pad.makeZero() 
        newNum1=self + pad
        newNum2= other + pad
        answer=karatsuba( newNum1.number, newNum2.number)
        

        # getting rid of leading zeros
        l1=0
        for l1 in range(len(answer)):
            if(answer[l1]!=0):
                break
        temp1=[answer[i+ l1] for i in range(len(answer)-l1)]
        temp1=''.join(str(digit) for digit in temp1)
        
        
        returnThis=BigInt(temp1) 
        
            
        return returnThis

###############################################################################
#####################   Large Factorial number Gen.   #########################
###############################################################################

def fact(n):
    
    # the definition of factorial to compare results
    
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)
        
        

        
        
        
        
        
        
