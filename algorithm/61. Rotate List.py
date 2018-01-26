# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/rotate-list/

Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


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
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result


    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None: return head
        if k<=0: return head

        listLength = 0

        fast = head

        for i in xrange(1, k):
            listLength += 1
            fast = fast.next  #####
            if fast is None:
                print "real k=", k % listLength
                print "head=", head.val
                return self.rotateRight(head, (k % listLength))


        slow = ListNode(0)
        slow.next = head
        #fast = fast.next
        if fast: print "slow %s = fast %s" % (slow.val, fast.val)

        while fast:
            if fast.next is None:
                if head == fast or head == slow.next:
                    return head
                #    newHead = slow
                #    slow.next = head
                #    head.next = None
                #    return newHead

                newHead = slow.next
                print "newHead = slow = %s" % (slow.next.val)

                fast.next = head
                print "fast.next = head = %s" % (head.val)

                #slow.next = head
                #print "slow.next = head = %s" % (head.val)

                #fast.next = None# tail
                #head.next = None
                slow.next = None


                print "newHead= %s, oldHead= %s" % (newHead.val, head.val)
                return newHead

            slow = slow.next
            fast = fast.next
            if fast: print "loop slow %s = fast %s" % (slow.val, fast.val)

        return head


def testcase(input, k, output):
    ins = Solution()
    head = ins.createList(input)
    before = ins.showList(head)
    after = ins.showList(ins.rotateRight(head, k))
    print "test: %s -> %s, K=%s \r\nrslt: %s -> %s" % (input, output, k, before, after)
    #assert (before == input)
    #assert (after == output)
    #print "...OK"
    print "-"*40



def unittest():
    #testcase(input=[], k=1, output=[])
    #testcase(input=[1], k=1, output=[1])
    #testcase(input=[1,2], k=1, output=[2,1])
    #testcase(input=[1,2], k=0, output=[1,2])
    #testcase(input=[1,2], k=3, output=[2,1])
    testcase(input=[1,2], k=2, output=[1,2])

    #testcase(input=[1,2,3], k=2, output=[2,3,1])
    #testcase(input=[1,2,3], k=2000000000, output=[2,3,1])

    #testcase(input=[1,2,3,4,5], k=2, output=[4,5,1,2,3])
    #testcase(input=[1,2,3,4,5,6,7,8,9], k=4, output=[6,7,8,9,1,2,3,4,5])
    #testcase(input=[1,2,3,4,5,6,7,8,9], k=10, output=[9,1,2,3,4,5,6,7,8])



if __name__ == '__main__':
    unittest()

