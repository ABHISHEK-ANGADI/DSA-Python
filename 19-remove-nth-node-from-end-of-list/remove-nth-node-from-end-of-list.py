# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # curr = head
        # l = 0
        # while curr:
        #     curr = curr.next
        #     l += 1

        # if l == n:
        #     return head.next
        
       
        # curr = head
        # for i in range(l-n-1):
        #     curr = curr.next
        
        # curr.next = curr.next.next
        # return head

        fast = head
        slow = head

        for i in range(n):
            fast = fast.next
        
        if fast == None:
            head = head.next
            return head

        while fast.next != None:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next

        return head


        