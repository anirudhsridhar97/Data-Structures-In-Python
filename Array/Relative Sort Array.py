# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 22:20:35 2020

@author: ANIRUDH
"""


"""

Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  
Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.

 
Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]

"""

def relativeSortArray(arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        res1=[]
        res2=[]
        for i in arr2:
            if i in arr1:
                x=arr1.count(i)
                res1+=[i]*x

        for i in arr1:
            if i not in arr2:
                
                res2.append(i)
        res2.sort()
        return res1+res2
arr1 = [2,3,1,3,2,4,6,7,9,2,19] 
arr2 = [2,1,4,3,9,6]
print(relativeSortArray(arr1,arr2))