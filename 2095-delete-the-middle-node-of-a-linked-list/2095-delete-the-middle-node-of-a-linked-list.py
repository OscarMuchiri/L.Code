class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        slow, fast = head, head
        while fast and fast.next:
            prev = slow             # Tracks the node before `slow`
            slow = slow.next        # Lands on the middle node
            fast = fast.next.next   # Moves twice as fast as `slow`

        prev.next = slow.next  #prev.next.next
        return head