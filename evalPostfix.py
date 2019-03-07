# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 12:10:40 2019
Postfix evaluation = Postfix2Infix
@author: Navit
"""


class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)



def evalPostfix(postfixexpr):
    #ah, the differnce is that here we evaluate the values. not returning the expression. 
    operandStack = Stack()
    tokenList = postfixexpr.split()
    
    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        elif token in '*/+-':
            B=operandStack.pop()
            A=operandStack.pop()
            result = doMath(token,int(A),int(B))
            operandStack.push(result)
        return operandStack.pop()
    
def doMath(op,A,B):
    if op=="+":
        return A+B
    elif op=="-":
        return A-B
    elif op=="*":
        return A*B
    elif op=="/":
        return A/B
    else:
        return print("unexpected operator")
            
            
def evalPostfix_iserr(postfixexpr):
    # handling alphabet appearing
    #handling number of operands doesn't match number of operators
    iserr=False
    tokenList=postfixexpr.split()
    numbers=0
    opnum=0
    for token in tokenList:
        # handling alphabet appearing
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            iserr=True
        #handling number of operands doesn't match number of operators
        if token in "0123456789":
            numbers=numbers+1;
        elif token in "*/+-":
            opnum=opnum+1
    if opnum != numbers-1:
        iserr=True
        
    return iserr
    
    
    
    
