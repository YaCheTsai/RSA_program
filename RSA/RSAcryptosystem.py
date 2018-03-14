import Crypto
from Crypto.PublicKey import RSA


public_key_string = open("pubkey.pem","r").read()
public_key = RSA.importKey(public_key_string)

private_key_string = open("privatekey.pem","r").read()
private_key = RSA.importKey(private_key_string)


message = "the example for Plaintext"

message1 = "The"
print public_key
print private_key
#Encrypt with public key
encrypted = public_key.encrypt(message, 32)


#Decrypt with private key
decrypted = private_key.decrypt(encrypted)

print encrypted
print decrypted