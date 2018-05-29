from random import randrange
import random
import math

def miller_rabin(n, k):

    if n == 2 or n % 2 == 0:
        return True
    if not n & 1:
        return False

    def check(a, s, d, n):
        x = pow(a, d, n)
        if x == 1:
            return True
        for i in xrange(s - 1):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return x == n - 1

    s = 0
    d = n - 1
    count = 0
    
    while d % 2 == 0:
        d >>= 1
        s += 1
    
    for i in xrange(k):
        a = randrange(2, n - 1)
        if not check(a, s, d, n):
            count+=1
        
  
    return True if count == k else False
    
#n = pow(2,512)+1
#n =331172955124362089754565485563265540649
#n =18177862711867466423
#k =10



e = input("input error rate : ")

k = math.log(e,0.25)
while True:
    n = random.getrandbits(512)
    if miller_rabin(n, int(k)): continue
    else: 
        print (str(n) + " is prime numbers ") 
        break
        
n = input("input number: ")
e = input("input error rate : ")
k = math.log(e,0.25)

if miller_rabin(n, int(k)):
    print (str(n) + " is not prime numbers ")
else: 
    print (str(n) + " is prime numbers ") 



    
    

