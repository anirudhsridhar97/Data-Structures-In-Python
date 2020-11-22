# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 19:35:31 2020

@author: ANIRUDH
"""


"""
Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

More formally check if there exists two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]

Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.
Example 2:

Input: arr = [7,1,14,11]
Output: true
Explanation: N = 14 is the double of M = 7,that is, 14 = 2 * 7.
Example 3:

Input: arr = [3,1,7,11]
Output: false
Explanation: In this case does not exist N and M, such that N = 2 * M.


"""

def checkIfExist(arr):
    zerocnt=arr.count(0)
    if zerocnt>1:
        return True
    squares=[i*2 for i in arr]
    for i in squares:
        if i in arr and i!=0:
            return True
    return False
arr=[10,2,5,3]
print(checkIfExist(arr))