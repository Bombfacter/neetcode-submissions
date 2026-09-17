# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        head2 = slow.next
        slow.next = None
        
        prev = None
        current = head2

        while current is not None:
            nextPtr = current.next
            current.next = prev
            prev = current
            current = nextPtr

        p1= head
        p2 = prev
        

        while p2:
            next1 = p1.next
            next2 = p2.next

            p1.next = p2
            p2.next = next1

            p1 = next1
            p2 = next2

        







