# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 22:48:09 2020

@author: ANIRUDH
"""


"""
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.


Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]


"""


def replaceElements(arr):
    
    m=-1
    i=len(arr)-1
    
    while i>=0:
        temp=arr[i]
        arr[i]=m
        
        if temp>m:
            m=temp
        i-=1
    return arr
arr = [17,18,5,4,6,1]
print(replaceElements(arr))