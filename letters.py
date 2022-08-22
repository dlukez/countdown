#!/usr/bin/env python3

import sys
import itertools

def non_local_hash(s):
    codes = [ord(c) for c in list(s)]
    product = codes[0]
    for x in codes[1:]:
        product *= x
    return product

input_word = sys.argv[1]
input_word = input_word.lower()

word_map = {}

input_length = len(input_word)
for i in range(5, input_length + 1):
    for x in itertools.permutations(input_word, i):
        word_map[non_local_hash(x)] = []

with open("words.txt", "r") as word_list:
    for word in word_list:
        word = word.strip().lower()
        word_hash = non_local_hash(word)
        if word_hash in word_map.keys():
            word_map[word_hash].append(word)


def check(option, reference):
    letters = list(reference)
    for x in option:
        if x not in letters:
            return False
        letters.remove(x)
    return True


keys = word_map.keys()
for k in keys:
    for word in word_map[k]:
        if check(word, input_word):
            print(word)

