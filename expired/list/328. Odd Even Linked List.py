# -*- coding: utf-8 -*-
import time
"""
https://leetcode.com/problems/odd-even-linked-list/

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input. 
The first node is considered odd, the second node even and so on ...
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

    def showList(self, node):
        #print node
        result = []
        while node:
            result.append(node.val)
            node = node.next

        return result

    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None: return head
        
        odd = head
        even = head.next
        node = odd
        evenhead = even

        getEven = False

        while odd or even:
            if odd.next is None or odd.next.next is None:
                odd.next = evenhead 
                getEven = True

            if odd.next and not getEven:
                odd.next = odd.next.next
                odd = odd.next

            if even.next is None or even.next.next is None:
                if not getEven: 
                    odd.next = evenhead
                even.next = None
                #print node
                #print evenhead
                return node


            if even.next:
                even.next = even.next.next
                even = even.next

        return node



def testcase(input, output):
    ins = Solution()
    head = ins.createList(input)
    
    before = ins.showList(head)
    after = ins.showList(ins.oddEvenList(head))
    print "in: %s          out: %s" % (input,  output)
    print "  : %s             : %s" % (before, after)
    #assert (before == input)
    #assert (after == output)
    #print "...OK"
    print "-"*40





def unittest():
    
    testcase(input=[1,2,3,4,5,6,7,8], output=[1,3,5,7,2,4,6,8])
    testcase(input=[ ], output=[ ])
    testcase(input=[2], output=[2])
    testcase(input=[1,2], output=[1,2])
    testcase(input=[1,2,3], output=[1,3,2])

    



if __name__ == '__main__':
    start = time.time()
    unittest()
    print "run time:", time.time() - start

