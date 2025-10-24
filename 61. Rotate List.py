class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head :
            return head 
        length, tail = 1, head 
        while tail.next :
            length += 1
            tail = tail.next 
        k = k%length 
        # print(k, length)
        if k == 0 :
            return head 

        curr = head 
        for i in range(length-k-1) :
            curr = curr.next 
        newHead = curr.next 
        curr.next = None

        # print(curr.val)
        tail.next = head 
        return newHead 

    """ solution with linear time and constant space """
