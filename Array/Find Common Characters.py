# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 22:13:07 2020

@author: ANIRUDH
"""

"""
Given an array A of strings made only from lowercase letters, return a list of 
all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]

"""


def commonChars(A):
    if len(A)<2:
        return A
    alist=set(A[0])
    res=[]
    for char in alist:
        n=min([a_word.count(char) for a_word in A])
        if n:
            res+=[char]*n
    return res
A=["bella","label","roller"]
print(commonChars(A))
