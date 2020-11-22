# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 21:53:12 2020

@author: ANIRUDH
"""

"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.


"""


def evalRPN(tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        expr=['+','*','-','/']
        stack=[]
        for i in tokens:
                if i not in expr:
                    stack.append(int(i))
                else:
                    r= stack.pop() 
                    l=stack.pop()
                    if i=='+':
                        stack.append(l+r)   
                    elif i=='-':
                        stack.append(l-r)
                    
                    elif i=='*':
                        stack.append(l*r)
                    
                    elif i=='/':
                        stack.append(int(l/r))
        return stack.pop()
print(evalRPN( ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))