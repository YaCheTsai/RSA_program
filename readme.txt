We found the PUBLIC KEY in pem format and Some Ciphers From ENTSCS, Please help us get the final flag
請看附檔pubkey.pem和cipher.txt

pem example 

30 81 9F 30 0D 06 09 2A  86 48 86 F7 0D 01 01 01
05 00 03 81 8D 00 30 81  89 02 81 81 00 AA 18 AB
A4 3B 50 DE EF 38 59 8F  AF 87 D2 AB 63 4E 45 71
C1 30 A9 BC A7 B8 78 26  74 14 FA AB 8B 47 1B D8
96 5F 5C 9F C3 81 84 85  EA F5 29 C2 62 46 F3 05
50 64 A8 DE 19 C8 C3 38  BE 54 96 CB AE B0 59 DC
0B 35 81 43 B4 4A 35 44  9E B2 64 11 31 21 A4 55
BD 7F DE 3F AC 91 9E 94  B5 6F B9 BB 4F 65 1C DB
23 EA D4 39 D6 CD 52 3E  B0 81 91 E7 5B 35 FD 13
A7 41 9B 30 90 F2 47 87  BD 4F 4E 19 67 02 03 01
00 01 

30 81 9F             ;30=SEQUENCE (0x9F = 159 bytes)
|  30 0D             ;30=SEQUENCE (0x0D = 13 bytes)
|  |  06 09          ;06=OBJECT_IDENTIFIER (0x09 = 9 bytes)
|  |  2A 86 48 86    ;Hex encoding of 1.2.840.113549.1.1
|  |  F7 0D 01 01 01
|  |  05 00          ;05=NULL (0 bytes)
|  03 81 8D 00       ;03=BIT STRING (0x8d = 141 bytes)
|  |  30 81 89       ;30=SEQUENCE (0x89 = 137 bytes)
|  |  |  02 81 81    ;02=INTEGER (0x81 = 129 bytes) the modulus
|  |  |  00          ;leading zero of INTEGER 
|  |  |  AA 18 AB A4 3B 50 DE EF  38 59 8F AF 87 D2 AB 63 
|  |  |  4E 45 71 C1 30 A9 BC A7  B8 78 26 74 14 FA AB 8B 
|  |  |  47 1B D8 96 5F 5C 9F C3  81 84 85 EA F5 29 C2 62 
|  |  |  46 F3 05 50 64 A8 DE 19  C8 C3 38 BE 54 96 CB AE 
|  |  |  B0 59 DC 0B 35 81 43 B4  4A 35 44 9E B2 64 11 31 
|  |  |  21 A4 55 BD 7F DE 3F AC  91 9E 94 B5 6F B9 BB 4F 
|  |  |  65 1C DB 23 EA D4 39 D6  CD 52 3E B0 81 91 E7 5B 
|  |  |  35 FD 13 A7 41 9B 30 90  F2 47 87 BD 4F 4E 19 67 
|  |  02 03          ;02=INTEGER (0x03 = 3 bytes) - the exponent
|  |  |  01 00 01    ;hex for 65537

so use this website https://holtstrom.com/michael/tools/hextopem.php
to get the Hexcode 

3035300D06092A864886F70D01010105000324003021021A00C0429FC69D3F623882FA5E5A99DA958315D7059D94ABCEC3BD0203000001
then analyze 

30 35
   30 0D
      06 09 
      2A 86 48 86 
      F7 0D 01 01 01
      05 00 
    03 24 00
       30 21
          02 1A0
          0C
          0429FC69D3F623882FA5E5A99DA958315D7059D94ABCEC3BD
        02 03
           00 00 01
           

u'll see that exponent == 1
so the ciphertext can convert to string directly
https://codebeautify.org/hex-string-converter

#================================================
#$%Programing_to_get_the_plaintext%$#
N=0xf9259752a03e2dca211fcbd7e035e229
e=0x10001
c1=0x44987b5d011fad957ede3362ce173275
c2=0x7463f38698290a6996c231ef85e830ab
c3=0x5b986aa33a62ade8eb1928df26cbaa47
#================================================

First step, trying to get p & q (N = p * q).
    u can use this website https://www.rapidtables.com/convert/number/decimal-to-hex.html to convert Decimal & Hex,
    and this one  http://www.wolframalpha.com/input/?i=331172955124362089754565485563265540649  to find N's quality factorization.
    finally u will get p & q

Second step useing FindElement.py to get N e d p q r 

Thrid step, useing MakePem.py to make private key 

step 4 Using RSAcryptosystem to load private key and decryt ciphertext. Note that ciphertext is decimal.

finally the result is :

ENTSCS{192.168.2.90~192.168.2.193.110}_Nice!!


Reference :

    https://crypto.stackexchange.com/questions/25498/how-to-create-a-pem-file-for-storing-an-rsa-key  : make pem
    https://en.wikipedia.org/wiki/RSA_(cryptosystem)
    https://gist.github.com/ofaurax/6103869014c246f962ab30a513fb5b49                                  :   find N e d p q r 
    http://studyraspberrypi.blogspot.tw/2016/01/encrypt-decrypt-string-with-rsa-public_18.html        : load pem & cryptosystem
    tools:
        http://www.wolframalpha.com/input/?i=331172955124362089754565485563265540649
        https://www.rapidtables.com/convert/number/decimal-to-hex.html
        https://codebeautify.org/hex-string-converter           
        https://holtstrom.com/michael/tools/hextopem.php           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           

