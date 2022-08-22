#!/usr/bin/env python3

import sys
import itertools

numbers = [int(x) for x in sys.argv[1:7]]
target = int(sys.argv[7])

print("Numbers to use: {}".format(" ".join([str(x) for x in numbers])))
print("Target result : {}".format(target))


class add():
    def __init__(self, a, b):
         self.a = a
         self.b = b
         self.value = a + b
    def __str__(self):
        return "{} + {} = {}".format(self.a, self.b, self.value)


class subtract():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.value = a - b
    def __str__(self):
        return "{} - {} = {}".format(self.a, self.b, self.value)


class multiply():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.value = a * b
    def __str__(self):
        return "{} * {} = {}".format(self.a, self.b, self.value)


class divide():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.value = a / b if b != 0 else 0.0
        if self.value.is_integer():
            self.value = int(self.value)
        else:
            self.value = 0
    def __str__(self):
        return "{} / {} = {}".format(self.a, self.b, self.value)


operations = [add, subtract, multiply, divide]

final = None

def do(numbers, previous):
    global final
    for i,v in enumerate(numbers):
        remaining = numbers[:i] + numbers[i+1:]
        for ii,vv in enumerate(remaining):
            if final is not None and len(previous) + 1 >= len(final):
                break
            remaining_inner = remaining[:ii] + remaining[ii+1:]
            for op in operations:
                result = op(v, vv)
                progress = previous + [result]
                if result.value < 1:
                    continue
                if result.value == target:
                    final = progress
                    return True
                if do([result.value] + remaining_inner, progress):
                    break

do(numbers, [])

if final is not None:
    print("")
    print("\n".join([str(x) for x in final]))

