# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 09:13:18 2019
infix2Postfix(infixexpr) is taken from the tutorial runestone academy
I added parChecker (code also taken from there)
and a function that checks that there are no consecutive operands without an operator
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

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        elif symbol==")":
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
            
        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False


def myisch(token):
    if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
        isch=True
    else:
        isch=False
        
    return isch


def InFixIsErr(infixexpr):
    iserr=False
    tokenList = infixexpr.split()
    lenTokenList=len(tokenList)
    for i in range(1, lenTokenList):
        token=tokenList[i]
        pretoken=tokenList[i-1]
        if (myisch(token) and myisch(pretoken)):
           iserr=True
        if ((token in "*/+-") and (pretoken in "*/+-")):
           iserr=True
    if not parChecker(infixexpr):
        iserr=True
    return iserr        
    
            
def infix2Postfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()
    if InFixIsErr(infixexpr):
        return print("error in expression")
    else:
        for token in tokenList:
            if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
                postfixList.append(token)
            elif token == '(':
                opStack.push(token)
            elif token == ')':
                topToken = opStack.pop()
                while topToken != '(':
                    postfixList.append(topToken)
                    topToken = opStack.pop()
            else:
                while (not opStack.isEmpty()) and \
                   (prec[opStack.peek()] >= prec[token]):
                      postfixList.append(opStack.pop())
                opStack.push(token)
    
        while not opStack.isEmpty():
            postfixList.append(opStack.pop())
        return " ".join(postfixList)


        
        
InFix1 = "A * B + C * D"
#print(InFixIsErr(InFix1))
print(infix2Postfix(InFix1))
#print(infix2Postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
