#!/bin/python3

import math
import os
import random
import re
import sys

"""
[Source: Hackerrank. Category: Sorting. Difficulty: Hard]
Problem Description: Counting inversions for arr[]. The elements at indices i, j (where i < j).
arr[i] > arr[j] forms an inversion. Count the number of swaps with the adjacent elements to sort the array.

Solution: implement merge sort, and keep track of swap at each recursion.
Example: [7,5,1] -> [1,7,5], 2 swaps -> [1,5,7], 1 swaps => Total 3 swaps/inversions
Complexity O(nlogn)
"""

def countInversions(arr):
    """ Main """
    array, swaps = mergeSort(arr)
    return swaps

def mergeSort(array):
    """ Recursive merge sort """
    n = len(array)
    mid_i = n//2
    if mid_i == 0:
        return array, 0
    leftArr, swap_L = mergeSort(array[0:mid_i])
    rightArr, swap_R = mergeSort(array[mid_i:n])
    return mergeHaves(leftArr, rightArr, swap_L, swap_R)

def mergeHaves(leftArr, rightArr, swap_L, swap_R):
    """ Sort two sorted halves of an array """
    nL = len(leftArr)
    nR = len(rightArr)
    i, j = 0, 0
    array = []
    swaps = 0
    while i < nL and j < nR:
        if leftArr[i] <= rightArr[j]:
            array.append(leftArr[i])
            i += 1
        else:
            array.append(rightArr[j])
            j += 1
            swaps += nL - i
    
    array += leftArr[i:nL] + rightArr[j:nR]
    return array, swaps + swap_L + swap_R

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
