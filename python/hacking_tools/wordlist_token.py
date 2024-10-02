#!/usr/bin/python3
import sys
import itertools

# list of chars and digits
upper_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"

def generate_tokens(pattern):
    # prepare the token space with the pattern received
    token_space = []

    for char in pattern:
        if char == "X":
            token_space.append(upper_chars)
        elif char == "0":
            token_space.append(digits)
        else:
            print("Invalid character in pattern, use only X or 0")
            sys.exit()
    
    # generate all combinations
    for combo in itertools.product(*token_space):
        print("".join(combo))

try:
    pattern = sys.argv[1]
    generate_tokens(pattern)
except:
    print("Usage: ./wordlist_token.py [pattern]")
    print("pattern: X - letter; 0 - number")
    sys.exit()

