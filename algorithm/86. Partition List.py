# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/partition-list/

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))


class Solution(object):
    def createList(self, start, size):
        head = ListNode(start)
        node = head
        for i in range(1, size):
            newNode = ListNode(head.val + i)
            node.next = newNode
            node = newNode
        return head

    def createList(self, l):
        head = ListNode(0)
        node = head
        for x in l:
            newNode = ListNode(x)
            node.next = newNode
            node = newNode
        return head.next

    def printList(self, node):
        while node is not None:
            print node.val,
            node = node.next
            if node is not None: print " -> ",
        print

    def showList(self, node):
        #print node
        result = []
        while node:
            result.append(node.val)
            node = node.next

        return result

    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None: return head

        lessDummy, moreDummy = ListNode(None), ListNode(None)
        less, more = lessDummy, moreDummy
        current = head

        while current:
            #print "loop: current.val(%s)  x(%s)" %(current.val, x)
            if current.val < x:
                less.next = current #ListNode(current.val)
                #print "less.next = current =", less.next.val
                less = less.next
                #print "less->", self.showList(lessDummy), less.val
            else:
                more.next = current #ListNode(current.val)
                more = more.next
                #print "more->", self.showList(moreDummy), more.val

            current = current.next
            #if current is None: break

            #print "current->", lessDummy
            #print " "

        #print "less=", less.val
        less.next = moreDummy.next
        #print "less.next=moreDummy.next.next=", less.next.val,moreDummy.next.next.val
        more.next = None

        return lessDummy.next



def testcase(input, x, output):
    ins = Solution()
    head = ins.createList(input)
    before = ins.showList(head)
    after = ins.showList(ins.partition(head, x))
    print "test: %s -> %s x=%s\r\nrslt: %s -> %s" % (input, output, x, before, after)
    #assert (before == input)
    #assert (after == output)
    #print "...OK"
    print "-"*40



def unittest():
    testcase(input=[1, 4, 3, 2, 5, 2], x=3, output=[1, 2,2, 4, 3, 5])
    testcase(input=[ ], x=4, output=[ ])
    testcase(input=[1], x=4, output=[1])
    testcase(input=[1,2,3], x=4, output=[1,2,3])
    testcase(input=[5,6,7], x=4, output=[5,6,7])
    testcase(input=[5,1,7], x=4, output=[1,5,7])
    testcase(input=[5,1,7], x=0, output=[5,1,7])
    #testcase(input=[1,1,2], output=[1,2])
    #testcase(input=[1,1,2,3,3], output=[1,2,3])
    #testcase(input=[1,2,2,3,3], output=[1,2,3])
    #testcase(input=[1,1,1], output=[1])
    #testcase(input=[1,2,3], output=[1,2,3])



if __name__ == '__main__':
    unittest()

