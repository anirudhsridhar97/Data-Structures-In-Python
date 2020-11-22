# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 11:57:28 2020

@author: ANIRUDH
"""

"""
Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.


Example 1:

Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]

"""



"""
Explaination
-----------------
This algorithm goes backwards and applies correct shifting distance to every element.

1.Why backwards?
If we would start shifting from left to right, then we would be overwriting elements before 
we have had the chance to shift them,
that is why we go backwards instead.
We make sure we have shifted out an element before we shift another one into its original position.

2.What is the correct shift distance?
The duplication of a zero pushes all elements to the right of it by one.
This means also that every element is shifted to the right as many times as there are zeroes to the left of it.
E.g. in the array [1,0,2,0,3] , 1 will not move, 2 will shift one position and 3 will shift two positions.
As we go backwards, every time we bypass a zero (and duplicate it), the shift distance decreases for the 
elements we haven't shifted yet, because there is one less zero in front of them.

3.Why the < n checks?
Shifts push some of the elements out of the array. We do the < n checks to make sure 
we write down only elements that are shifted to a valid position inside the array and 
we ignore the ones falling off the end.


"""


def duplicateZeros(arr):
    zeros=arr.count(0)
    n=len(arr)
    for i in range(n-1,-1,-1):
        if i+zeros<n:
            arr[i+zeros]=arr[i]
        if arr[i]==0:
            zeros-=1
            if i+zeros<n:
                arr[i+zeros]=0
        
arr=[1,0,2,3,0,4,5,0]
duplicateZeros(arr)
print(arr)
