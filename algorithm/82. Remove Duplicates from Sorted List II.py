# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
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
        while node is not None:
            result.append(node.val)
            node = node.next
        return result

    def deleteDuplicates_72ms(self, head):
        result = [ ]
        node = head
        while node is not None:
            result.append(node.val)
            node = node.next

        result = [x for x in result if result.count(x) == 1]
        print result

        node = ListNode(0)
        orig = ListNode(0)
        orig = node
        for i in result:
            node.next = ListNode(i)
            node = node.next
        return orig.next


    def nextNot(self, head, n):
        node = head
        if head is None: return head
        if node.next is None: return None

        while node.next is not None:
            if node.val == n:
                node = node.next
                if node.next is None:
                    if node.val == n:
                        return None
                    else:
                        return node
            else:
                print "return waitnode=", node.val
                return node
        print "??", self.showList(head)
        return node


    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head is None) or (head.next is None): return head

        orig = current = ListNode(0)
        orig.next = head
        node = head

        isRealHead = (head.val != head.next.val)

        while node is not None and node.next is not None:

            if node.next.val == node.val:
                waitnode = self.nextNot(node, node.val)

            else:
                waitnode = node.next

            if waitnode: print "waitnode=", waitnode.val

            while (waitnode is not None) and (waitnode.next is not None) and (waitnode.val == waitnode.next.val):
                waitnode = self.nextNot(waitnode, waitnode.val)
                if waitnode: print "get return waitnode=", waitnode.val, self.showList(waitnode)


            node.next = waitnode
            if waitnode: print "node.next = waitnode =", waitnode.val

            node = node.next
            if node: print "node = node.next =", node.val

        if isRealHead:
            return orig.next
        return orig.next.next







def testcase(input, output):
    ins = Solution()
    head = ins.createList(input)
    before = ins.showList(head)
    after = ins.showList(ins.deleteDuplicates(head))
    print "test: %s -> %s \r\nrslt: %s -> %s" % (input, output, before, after)
    #assert (before == input)
    #assert (after == output)
    #print "...OK"
    print "-"*40


def unittest():
    testcase(input=[1,2,3,3,4,4,5], output=[1,2,5])
    testcase(input=[1,1,1,2,3], output=[2,3])

    testcase(input=[], output=[])
    testcase(input=[1], output=[1])
    testcase(input=[1,1], output=[])
    testcase(input=[1,1,1,1], output=[])
    testcase(input=[1,1,1,1,2], output=[2])
    testcase(input=[1,1,2], output=[2])
    testcase(input=[1,1,2,3,3], output=[2])




if __name__ == '__main__':
    unittest()

