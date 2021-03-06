# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 19:37:22 2020

@author: ANIRUDH
"""


"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]


"""



def merge(nums1, m, nums2, n):
    
    count=m+n-1
    m-=1
    n-=1
    
    
    while(m>=0 and n>=0):
        if nums1[m]>nums2[n]:
            nums1[count]=nums1[m]
            count-=1
            m-=1
        else:
            nums1[count]=nums2[n]
            count-=1
            n-=1
    while n>=0:
        nums1[count]=nums2[n]
        count-=1
        n-=1
  
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
merge(nums1,3,nums2,3)
print(nums1)