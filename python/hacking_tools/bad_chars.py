# script to generate all the characters on the ascii table to test for bad chars in a buffer overflow

for i in range(0, 256):
    char = hex(i).replace("0x", '\\x')
    print(char, end='')
