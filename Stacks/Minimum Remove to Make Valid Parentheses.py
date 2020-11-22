# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 22:25:23 2020

@author: ANIRUDH
"""

"""

Given a string s of '(' , ')' and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.

"""

"""
Approach To Solution

1. Convert string to list, because String is an immutable data structure in Python and it's much easier and memory-efficient to deal with a list for this task.
2. Iterate through list
3. Keep track of indices with open parentheses in the stack. In other words, when we come across open parenthesis we add an index to the stack.
4. When we come across close parenthesis we pop an element from the stack. If the stack is empty we replace current list element with an empty string
5. After iteration, we replace all indices we have in the stack with empty strings, because we don't have close parentheses for them.
6. Convert list to string and return

"""

def minRemoveToMakeValid(s):
    
    stack=[]
    s=list(s)
    
    for i,char in enumerate(s):
        if char=='(':
            stack.append(i)
        elif char==')':
            if stack:
                stack.pop()
            else:
                s[i]=''
    while stack:
        s[stack.pop()]=''
    return ''.join(s)

print(minRemoveToMakeValid("lee(t(c)o)de)"))



