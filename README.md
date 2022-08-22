# countdown
Solutions for Countdown / Letters and Numbers problems.

Faster than Susie Dent!™

## Conundrums

This problem is a simple anagram problem. This script will only work for input words of 8 or 9 characters.

```Usage
> ./conundrum.py limpaunt
platinum
```

## Letters

This problem requires the player to find the longest word possible with the given set of letters.
From an algorithm point of view this was interesting to solve as we need a solution that can process
a dictionary and find valid answers within the time limit (30 seconds). Most often, a word cannot
be made with all the letters so we must look for the longest word we can find using any subset of the
letters.

This solution simply uses multiplication to create a hash of an input word, with the intention of having
hash collisions consisting of any word containing the same letters (even if in a different order). I've
used python for this as it supports arbitrarily large integers.

```Usage
> ./letters.py apftleaot
plate
petal
pleat
paleo
...
```

## Numbers

A brute-force solution that attempts any combination of addition, subtraction, multiplication and division
to try to get to the target number. The algorithm will stop once it finds a solution and won't attempt
to find solutions that yield a close result (players in the game can win points by getting close to the target
number).

```Usage
> ./numbers.py 25 6 9 8 5 2 717
Numbers to use: 25 6 9 8 5 2
Target number: 717

25 + 6 = 31
31 * 8 = 248
248 - 9 = 239
5 - 2 = 3
3 * 239 = 717
```
