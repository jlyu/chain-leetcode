# -*- coding: utf-8 -*-
import time
"""
https://leetcode.com/problems/simplify-path/

Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
"""

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        """
        if path == '/': return path

        for char in path:


        stack = []
        filename = ''
        for char in path:
            if char == '/':
                if '..' in filename:
                    if stack: stack.pop()
                else:
                    if '.' not in filename and filename != '/':
                        stack.append(filename)
                print filename
                filename =''

            filename += char

        s = ""
        for p in stack:
            s += p

        return s or '/'
        """

        stack = []
        for p in [ p for p in path.split("/") if p and p not in "." ]:
            if p == "..":
                if stack: stack.pop()
            else:
                stack.append(p)
        return '/' + "/".join(stack)









def testcase(input, expected):
    ins = Solution()
    output = ins.simplifyPath(input)

    print "in: %s,  expected: %s,  out: %s" % (input, expected, output)

    #assert (before == input)
    #assert (after == output)
    print "-"*40





def unittest():
    testcase(input="/home/", expected="/home")
    testcase(input="/a/./b/../../c/", expected="/c")
    testcase(input="/", expected="/")
    testcase(input="/..aa/...hidden/", expected="/..aa/...hidden") #?
    testcase(input="/home//foo/", expected="/home/foo")
    testcase(input="/../", expected="/")









if __name__ == '__main__':
    start = time.time()
    unittest()
    print "run time:", time.time() - start

