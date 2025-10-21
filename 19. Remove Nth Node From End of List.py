# 1. Brute force approach  

class SolutionCount:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Time Complexity: O(2n)
        Space Complexity: O(1)
        """
        count = 0 
        curr = head
        while curr:
            count += 1
            curr = curr.next
        
        dummy = ListNode(-1, head)
        curr = dummy
        for _ in range(count - n):
            curr = curr.next
        
        curr.next = curr.next.next
        return dummy.next

################################################################################################################################################################

# 2. Optimal approach 

class SolutionTwoPointer:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        - Slow and Fast pointer approach 
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        dummy = ListNode(-1, head)
        slow = fast = dummy

        for _ in range(n):
            fast = fast.next 
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return dummy.next
