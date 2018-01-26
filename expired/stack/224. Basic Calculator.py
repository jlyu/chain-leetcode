# -*- coding: utf-8 -*-
import time
"""
https://leetcode.com/problems/basic-calculator/

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23
Note: Do not use the eval built-in library function.
"""

class Solution(object):

    def cal(self, s):
        if s.strip().isdigit() or s.strip()[1:].isdigit(): return int(s)
        s = s.replace("--", "+");
        s = s.replace("++", "+");
        s = s.replace("-+", "-");
        s = s.replace("+-", "-");


        lhs, ops, rhs, nextops = None, None, None, None
        for d in s:
            if d == ' ': continue

            if ops is None and d not in "+-": lhs = (lhs or '') + d


            if d in "+-":
                if ops is None: ops = d
                elif ops and rhs is None:
                    if d == ops == '-': ops = '+'
                    elif d == '-' and ops == '+': rhs = '-'
                else:
                    nextops = d
                #print "+-", d, ops, nextops
                continue

            if nextops:
                #print"  >>>>",d, lhs, ops, rhs, nextops
                if ops == "+": lhs = str(int(lhs) + int(rhs))
                if ops == "-": lhs = str(int(lhs) - int(rhs))
                ops = nextops
                nextops = None
                rhs = None

            if nextops is None and ops:
                #print "  rhs >>>", rhs, d
                rhs = (rhs or '') + d


            #print "loop==", d, lhs, ops, rhs, nextops

        if lhs and ops and rhs:
            #print "final:",lhs, ops, rhs, nextops
            if ops == "+": lhs = str(int(lhs) + int(rhs))
            if ops == "-": lhs = str(int(lhs) - int(rhs))

        return lhs


    def calculate(self, s):
        if s.strip().isdigit() or s.strip()[1:].isdigit(): return int(s)
        if "(" not in s: return int(self.cal(s))

        stack = []
        for i, d in enumerate(s):
            if d == ' ': continue
            if d != ")": stack.append(d)
            if d == ')':
                #print "stack=",stack,
                substr, n = '', None
                while stack and n != '(':
                    n = stack.pop()

                    if n == '(':
                        r = str(int(self.cal(substr)))  # -![::-1]
                        #print "substr=", substr, "return=", r, ''.join(stack)

                        stack.append(r)
                        break

                    substr = n + substr

        #print "fin stack=", stack
        return int(self.cal(''.join(stack)))



def testcase(input,expected):
    ins = Solution()
    output = ins.calculate(input)
    if len(input) < 150:
        print "in: %s,  expected: %s,  out: %s" % (input,  expected, output),
    if expected == output:
        print "...OK"
    else:
        print "...NG"
    print "-"*40


def unittest():
    i1 = "5+3-4-(1+2-7+(10-1+3+5+(3-0+(8-(3+(8-(10-(6-10-8-7+(0+0+7)-10+5-3-2+(9+0+(7+(2-(2-(9)-2+5+4+2+(2+9+1+5+5-8-9-2-9+1+0)-(5-(9)-(0-(7+9)+(10+(6-4+6))+0-2+(10+7+(8+(7-(8-(3)+(2)+(10-6+10-(2)-7-(2)+(3+(8))+(1-3-8)+6-(4+1)+(6))+6-(1)-(10+(4)+(8)+(5+(0))+(3-(6))-(9)-(4)+(2))))))-1)))+(9+6)+(0))))+3-(1))+(7))))))))"

    testcase(input="(1+(4+5+2)-3)+(6+8)", expected=23)
    testcase(input=" 2-1 + 2 ", expected=3)
    testcase(input="1 + 1", expected=2)
    testcase(input="(1-(3-4))", expected=2)
    testcase(input="(5-(1+(5)))", expected=-1)
    testcase(input="2147483647", expected=2147483647)
    testcase(input="-2147483647", expected=-2147483647)
    testcase(input=" -30", expected=-30)
    testcase(input="1-11", expected=-10)
    testcase(input=" 2-1 + 2 ", expected=3)
    testcase(input="8+4-1+8-10", expected=9)
    testcase(input="2-4-(8+2-6+(8+4-(1)+8-10))", expected=-15)
    testcase(input="4+-1", expected=3)
    testcase(input="1-(2+3-(4+(5-(1-(2+4-(5+6))))))", expected=-1)
    testcase(input="9-4--3+8--2-1", expected=17)
    testcase(input="1-(3+5-2+(3+19-(3-1-4+(9-4-(4-(1+(3)-2)-5)+8-(3-5)-1)-4)-5)-4+3-9)-4-(3+2-5)-10", expected=-15)
    testcase(input="10+8", expected=18)
    testcase(input=i1, expected=-35)


if __name__ == '__main__':
    start = time.time()
    unittest()
    print "run time:", time.time() - start

