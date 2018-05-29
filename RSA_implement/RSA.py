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

def getprime():
    #n = pow(2,512)+1
    #n =331172955124362089754565485563265540649
    #k =10

    while True:
        n = random.getrandbits(512)
        if miller_rabin(n, 20): continue
        else: 
            return n 
            break
   
        
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
    
def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi/e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        
        x = x2- temp1* x1
        y = d - temp1 * y1
        
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    
    if temp_phi == 1:
        return d + phi
        
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in xrange(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True
    
def generate_keypair(p, q):
    
    #n = pq
    n = p * q

    #Phi is the totient of n
    phi = (p-1) * (q-1)

    #Choose an integer e such that e and phi(n) are coprime
    e = 65537

    #Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    while g != 1:
        e = 65537
        g = gcd(e, phi)

    #Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)
    dp = d % (p-1)
    dq = d % (q-1)
    qinv = multiplicative_inverse(q, p)
    #Return public and private keypair
    #Public key is (e, n) and private key is (d, n)
    return ((d, n), (e, n), (dp, dq, qinv, p, q)) 
    
def encrypt(pk, plaintext):
    #Unpack the key into it's components
    key, n = pk
 
    #Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    #Return the array of bytes
    return cipher

def decrypt(pk, ciphertext, other):
    #Unpack the key into its components
    key, n = pk
    dp, dq, qinv, p, q = other
    #Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = []
    for char in ciphertext:
        m1 = pow(char, dp, p)
        m2 = pow(char, dq, q)
        tmp = (m1 - m2) * qinv
        tmp = tmp * q 
        result = tmp + m2
        plain.append(chr(int(result)))
    #plain = [(((qinv * ((char ** dp) % p - (char ** dq) % q)))*q)+((char ** dq) % q) for char in ciphertext]
    #Return the array of bytes as a string
    x = ''.join(plain)
    #print x 
    return x
    
if __name__ == "__main__":
    p = getprime()
    q = getprime()
    print ("p = "+"\n" + str(p)+"\n") 
    print ("q = "+"\n" + str(q)+"\n")
    public, private, other = generate_keypair(p, q)
    print ("public = "+"\n" + str(public)+"\n")
    print ("private = "+"\n" + str(private)+"\n")
    message = raw_input("Enter a message : ")
    encrypted_msg = encrypt(private, message)
    print ("encrypted_msg = "+"\n" + str(encrypted_msg)+"\n" )
    print decrypt(public, encrypted_msg, other)
    
    