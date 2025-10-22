class Solution:
    def getIntersectionNode(self, h1: ListNode, h2: ListNode) -> Optional[ListNode]:
    # optimal solution with O(4N)time and O(1)space
    # 1. find the lenght of both linked lists 
    # 2. move the head pointer of longer list with difference of lenghts 
    # 3. check the nodes of both lists parallelly if any node found common return that node
    
        ptr1, ptr2, len1, len2 = h1, h2, 0, 0

        while h1 : 
            len1 += 1
            h1 = h1.next
        while h2 :
            len2 += 1 
            h2 = h2.next 
        n = abs(len1-len2)

        if len1-len2 > 0 :
            while n > 0 :
                ptr1 = ptr1.next 
                n -= 1
        else : 
            while n > 0 :
                ptr2 = ptr2.next 
                n -= 1
        while ptr1 : 
            if ptr1 == ptr2 : 
                return ptr1 
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return 

########################################################################################################################################################

# above solution without finding the lenght of lists 
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1, l2 = headA, headB
        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1


########################################################################################################################################################


class Solution:
    def getIntersectionNode(self, h1: ListNode, h2: ListNode) -> Optional[ListNode]:
    # Take the nodes of list1 in hash table and start checking list2 nodes in the hash table O(N)space and O(N)time
        list = set()
        while h1 : 
            list.add(h1)
            h1 = h1.next 
        print([x.val for x in list])
        while h2 and list :
            if h2 in list :
                return h2
            h2 = h2.next
        return 


########################################################################################################################################################


# TLE   with list 
class Solution:
    def getIntersectionNode(self, h1: ListNode, h2: ListNode) -> Optional[ListNode]:
    
    # Take the nodes of list1 in hash table and start checking list2 nodes in the hash table 
        list = []
        while h1 : 
            list.append(h1)
            h1 = h1.next 
        print([x.val for x in list])
        while h2 and list :
            if h2 in list :
                return h2
            h2 = h2.next
        return 
