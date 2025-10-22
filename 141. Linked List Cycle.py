class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # take slow, fast pointers and move slow by one and fast by two positions 
        # if any loop existed in the linked list, the two pointers will definetly meet 
        # solution with O(N)time and O(1)space #
        slow, fast = head, head
        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next 
            if slow == fast :
                return True  
        return False 
        
########################################################################################################################################################        
        
        
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # solution with O(N)time and O(N)space #
        # stores the nodes of list in stack if any node came again means loop existed in the linked list 
        stack = []
        while head : 
            stack.append(head)
            head = head.next
            if head in stack : return True 
            
        return False 
