#!/usr/bin/env python3
from insecure_hash import hash_string
from Crypto.Cipher import AES
import os

def find_collision(message):
    # Your solution.
    key = os.urandom(16)  # Generates a random 16-byte key
    hash_value = hash_string(message) # hash of message
    cipher = AES.new(key) #  creates an instance of the AES cipher
    result = cipher.encrypt(hash_value) # encrypts the hash value
    result = result + key # Append the original key to the encrypted result. This addition of the key further modifies the encrypted result
    return result # Returns the modified result (which is the encrypted hash value plus the key) as bytes using the default UTF-8 encoding.



if __name__ == '__main__':
    message = "aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbb".encode()
    print("Hash of %s is %s" % (message, hash_string(message)))
    collision = find_collision(message)
    print("Hash of %s is %s" % (collision, hash_string(collision)))
