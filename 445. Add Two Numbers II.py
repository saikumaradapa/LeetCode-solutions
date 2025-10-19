class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        time complexity : O(max(n, m))
        space complexity : O(n) used to store the result 
        """
      
        def reverseList(node):
            prev = None 
            while node:
                nextNode = node.next 
                node.next = prev 
                prev = node
                node = nextNode 
            return prev 

        l3, l4 = reverseList(l1), reverseList(l2)

        curr = dummy = ListNode(0) 
        carry = 0

        while l3 or l4 or carry:
            a = l3.val if l3 else 0 
            b = l4.val if l4 else 0 

            sum = (a + b + carry) % 10 
            carry = (a + b + carry) // 10
            curr.next = ListNode(sum)

            l3 = l3.next if l3 else None 
            l4 = l4.next if l4 else None 
            curr = curr.next 
        return reverseList(dummy.next)
