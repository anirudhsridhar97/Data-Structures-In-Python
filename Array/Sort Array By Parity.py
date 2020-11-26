# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 22:08:22 2020

@author: ANIRUDH
"""


"""
Given an array A of non-negative integers, return an array consisting of all the even elements of A, 
followed by all the odd elements of A.

You may return any answer array that satisfies this condition.


Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.


"""

def sortArrayByParity(A):
    
    i,j=0,len(A)-1
    
    while i<j:
        if A[i]%2 > A[j]%2:
            A[i],A[j]=A[j],A[i]
        if A[i]%2==0:
            i+=1
        if A[j]%2==1:
            j-=1
            
A=[3,1,2,4]
sortArrayByParity(A)

print(A)
"""
OR

return ([i for i in A if i%2==0] + [i for i in A if i%2==1])

"""
