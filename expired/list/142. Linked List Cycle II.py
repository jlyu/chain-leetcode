# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/linked-list-cycle-ii/

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
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

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None: return False
        fast = head
        slow = head

        while fast:
            if fast.next:
                fast = fast.next.next
                slow = slow.next
            else:
                return False

            if fast == slow: return fast

        return False
    """    
    def detectCycle(self, head):

        end = self.hasCycle(head)
        if end == False: return None

        current = head
        while current != end.next:
            meetEnd = False

            node = current.next
            while node:
                if node == current: return current
                
                if node == end:
                    if meetEnd:
                        if current == end: return current
                        else: break 
                    meetEnd = True

                node = node.next

            current = current.next
        return current
    """

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        end = self.hasCycle(head)
        if end == False: return None

        nodesInLoop = 1
        current = end
        while current.next != end:
            nodesInLoop += 1
            current = current.next

        fast = head
        for i in xrange(nodesInLoop):
            fast = fast.next

        slow = head
        while fast != slow:
            fast = fast.next
            slow = slow.next

        return fast



def testcase(input, m, n, output):
    ins = Solution()
    head = ins.createList(input)
    before = ins.showList(head)
    after = ins.showList(ins.reverseBetween(head, m, n))
    print "test: %s -> %s m=%s, n=%s\r\nrslt: %s -> %s" % (input, output, m, n, before, after)
    #assert (before == input)
    #assert (after == output)
    #print "...OK"
    print "-"*40



def unittest():
    pass




if __name__ == '__main__':
    unittest()

