# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 19:13:21 2020

@author: ANIRUDH
"""

"""
Given a sorted array nums, remove the duplicates in-place such that each element appears 
only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input array 
in-place with O(1) extra memory.

Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means a modification to the 
input array will be known to the caller as well.

Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2]
Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2 
respectively. It doesn't matter what you leave beyond the returned length.

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4]
Explanation: Your function should return length = 5, with the first five elements of nums 
being modified to 0, 1, 2, 3, and 4 respectively. It doesn't matter what values are set beyond the returned length.
 

"""


def removeDuplicates( nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        newtail=0
        for i in range(1,len(nums)):
            if nums[i]!=nums[newtail]:
                newtail+=1
                nums[newtail]=nums[i]
        return newtail+1
nums = [1,1,2]
removeDuplicates(nums)
print(nums)