class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s,f = head,head 
        while f and f.next :
            s = s.next 
            f = f.next.next 
            if s == f :
                s = head 
                while s != f :
                    s,f =s.next, f.next 
                return s
        return None

''' time complexity : O(n)
    space complexity : O(1)
'''
