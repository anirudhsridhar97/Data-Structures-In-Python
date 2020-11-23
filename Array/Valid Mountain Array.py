# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 22:01:29 2020

@author: ANIRUDH
"""


"""
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < A[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]


Example 1:

Input: arr = [2,1]
Output: false
Example 2:

Input: arr = [3,5,5]
Output: false
Example 3:

Input: arr = [0,3,2,1]
Output: true
 


"""
def validMountainArray(arr):
    
    if not arr:
        return False
    
    first=0
    last=len(arr)-1    
    peak=max(arr)
    peakAt=arr.index(peak)
        
    if peakAt==first or peakAt==last: #Peak Cannot be first or last
        return False
    
    while first<peakAt: #making sure going up is OK
        if arr[first]>=arr[first+1]:
            return False
        first+=1
    
    while last>peakAt: #making sure going down is OK
        if arr[last]>=arr[last-1]:
            return False
        last-=1

    return True
arr=[1,2,3,4,3,2,1]
print(validMountainArray(arr))