# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur = list1
        a=[]
        while cur:
            a.append(cur.val)
            if cur.next != None: cur = cur.next
            else: break
        cur = list2
        while cur:
            a.append(cur.val)
            if cur.next != None: cur = cur.next
            else: break
        a.sort()
        if len(a)>0:
            head = ListNode(a[0])
            tail = head
            for i in range (1, len(a)):
                tail.next = ListNode(a[i])
                tail = tail.next

            return head  