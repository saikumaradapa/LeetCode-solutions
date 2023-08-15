class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left, right = ListNode(),ListNode()
        l,r = left, right 
        while head :
            if head.val < x :
                left.next = head
                left = left.next 
            else :
                right.next = head
                right = right.next 
            head = head.next 
        right.next = None
        left.next = r.next
        return l.next 

''' time complexity : O(n)
    space complexity : O(1)
'''
