import BigInt
from BigInt import mod_add
from BigInt import mod_mul


################################################################################
#############################   testbigint class   #############################
################################################################################
class TestBigInt:

    def __init__(self):

        #running these
        self.__testAdd__(2,3)
        self.__testAdd__(1,0)
        self.__testAdd__(2454434,49494393)
        self.__testAdd__(9999999,11111)
        
        self.__testMult__(2,3)
        self.__testMult__(1,0)
        self.__testMult__(242,430)
        self.__testMult__(999000,11332)
        
        self.__testMod__(2,3,12)
        self.__testMod__(12,10, 13)
        self.__testMod__(242,4390, 5)
        self.__testMod__(99534,13111, 232)

        return None

    # test my add function
    def __testAdd__(self, a, b):

        #declaring vars
        x = BigInt.BigInt(a)
        y = BigInt.BigInt(b)

        z = x.__add__(y)
        intSum = a + b
        
        #printing results
        print "\nAdding: " + str(a) + " + " + str(b)
        print "This: " + str(z) + " should equal: " + str(intSum)

        #checking results
        if intSum != int(z.__str__()):
            print ("test fail")
            

        return None
    
    #test my mult func
    def __testMult__(self, a, b):

        #declaring vars
        x = BigInt.BigInt(a)
        y = BigInt.BigInt(b)

        z = x.__mul__(y)
        intMult = a * b
        
        #printing results
        print "\nMultiplying: " + str(a) + " * " + str(b)
        print "This: " + str(z) + " should equal: " + str(intMult)

        # testing if correct values
        if intMult != int(z.__str__()):
            print ("test fail")
            

        return None
    
    #test my mod function
    def __testMod__(self, a, b, n):

        #declaring vars
        intMod=int(a+b) % n
        intMultMod=int(a*b) % n
        
        x = BigInt.BigInt(a)
        y = BigInt.BigInt(b)
        n = BigInt.BigInt(n)

        value=mod_add(x,y,n)
        valueMul=mod_mul(x,y,n)
        
        
        # testing functions for modMul and modAdd
        print "\nModding: (" + str(a) + " + " + str(b) + ") mod "+ str(n)
        print "This: " + str(value) + " should equal: " + str(intMod)
        
        print "\nModding: (" + str(a) + " * " + str(b) + ") mod "+ str(n)
        print "This: " + str(valueMul) + " should equal: " + str(intMultMod)

        # testing if correct value
        if intMod != int(value.__str__()):
            print ("test fail")
        if intMultMod != int(valueMul.__str__()):
            print ("test fail")
            

        return None


###############################################################################
##############################   Main Class   #################################
###############################################################################

if __name__ == '__main__':
    

    print "test"
    a = TestBigInt()
    
    
    