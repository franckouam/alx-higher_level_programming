#!/usr/bin/python3
for i in range(26, 0, -1):
    offset = 96 if i % 2 == 0 else 64
    print("{}".format(chr(offset+i)), end="")
