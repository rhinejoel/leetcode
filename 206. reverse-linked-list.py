class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

class Solution:
    def reverseList(self, head):
        cur = head
        a = []

        # CREATE ARRAY FROM LINKED LIST
        if cur == None:
            return cur

        while cur != None:
            a.append(cur.val)
            cur = cur.next

        # REVERSE THE ARRAY
        r = []
        for i in range(len(a)-1, -1, -1):
            r.append(a[i])

        # CREATE LL FROM REV ARRAY
        cur = ListNode() # initialize the first object
        head = cur
        for i in range (len(r)):
            cur.val = r[i]
            if i == len(r)-1:
                cur.next = None
                return head
            else:
                cur.next = ListNode()
                cur = cur.next