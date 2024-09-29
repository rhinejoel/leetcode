class Solution:
    def removeNthFromEnd(self, head, n: int):

        # Need to do this in one pass
        # twopointers first = second + n

        first = head
        second = head

        for _ in range(n):
            first = first.next
        
        if first == None:
            return head.next

        while first.next:
            first = first.next
            second = second.next

        second.next = second.next.next
        return head