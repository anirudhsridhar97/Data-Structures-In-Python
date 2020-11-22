# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 13:05:43 2020

@author: ANIRUDH
"""


"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1)Open brackets must be closed by the same type of brackets.
2)Open brackets must be closed in the correct order.


"""


def isValid(s):
    
    
    dict={'}':'{','[':']',')':'('}
    stack=[]
    for i in s:
        #Add to Stack If its an Open Bracket
        if i in dict.values():
            stack.append(i)
        #If its closing bracket    
        elif i in dict.keys():
            #Check if stack is empty and check whether opening bracket for corresponding closing bracket from dictionary is  equal to item from top of stack
            if stack==[] or dict[i]!=stack.pop():
                return False
        else:
            return False
    
    return stack==[]
       
s="({})"     
print(isValid(s))
