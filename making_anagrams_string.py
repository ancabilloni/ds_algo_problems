#!/bin/python3

import math
import os
import random
import re
import sys

"""
[Source: Hackerrank. Category: String manipulation. Difficulty: Easy]
Problem Description: Given two strings a & b. Find the minimum deletions to make two strings anagram of each other.

For example: a = cde, b = dcf. To make a & b anagrams, e is removed from a, and f is removed from b => 2 deletions.

First solution:
- Store letter of each string with its frequency in a hashtable.
- Compare if there is any common string, and compare frequency of matching letters
- Delete unmatched string, and extra letters
- Return the number of deletions
- Complexity: 0(m+n) time, and O(1) space

Second solution:
- create two fixed 26 letters arrays for a and b
- add add frequency to the index of the character
- deletion is the sum of differences from both array's values at each index
- Complexity: O(m+n) time, and O(1) space
- Pros: shorter and cleaner codes compare to the first solution
"""

# Complete the makeAnagram function below.
def makeAnagram1(a, b):
    """ First solution, using hashtable """
    del_count = 0
    a_map = {}
    for c in a: # O(n) with n is the length of |a|
        a_map.setdefault(c, 0)
        a_map[c] += 1

    b_map = {}
    for c in b: #O(m) with m is the length of |b|
        b_map.setdefault(c, 0)
        b_map[c] += 1

    for k in a_map: # O(n)
        if k in b:
            del_count += abs(a_map[k] - b_map[k])
        else:
            del_count += a_map[k]

    for k in b_map: # O(m)
        if k not in a:
            del_count += b_map[k]
    return del_count 

def makeAnagram2(a, b):
    """ Second solution, using array size 26 indexing a-z """
    a_arr = [0]*26
    b_arr = [0]*26
    del_counts = 0
    for c in a:
        a_arr[ord(c) - ord('a')] += 1

    for c in b:
        b_arr[ord(c) - ord('a')] += 1

    for i in range(26):
        del_counts += abs(a_arr[i] - b_arr[i])

    return del_counts
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram2(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
