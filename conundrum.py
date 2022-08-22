#!/usr/bin/env python3

import sys

def non_local_hash(s):
    codes = [ord(c) for c in list(s)]
    product = codes[0]
    for x in codes[1:]:
        product *= x
    return product

def check(option, reference):
    letters = list(reference)
    for x in option:
        if x not in letters:
            return False
        letters.remove(x)
    return True

input_word = sys.argv[1]
input_word = input_word.lower()
input_hash = non_local_hash(input_word)

print(input_hash)

filename = "words-" + str(len(input_word)) + ".txt"
with open(filename, "r") as word_list:
    for word in word_list:
        word = word.strip().lower()
        word_hash = non_local_hash(word)
        if word_hash == input_hash and check(word, input_word):
            print(word)

