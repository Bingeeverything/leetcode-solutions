import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        
        current = head
        while current.next:
            new_mode = ListNode(math.gcd(current.val, current.next.val))
            new_mode.next = current.next
            current.next = new_mode
            current = new_mode.next
        
        return head