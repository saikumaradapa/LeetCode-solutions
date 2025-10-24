class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # 1. take the values in the both lists 
    # 2. sort them 
    # 3. make a new linked list with these values 
        list = []
        while list1 :
            list.append(list1.val)
            list1 = list1.next
        while list2 :
            list.append(list2.val)
            list2 = list2.next
        list = sorted(list)
        if not list :
            return 
        # print(list)
        head = ListNode(list.pop())
        # return head
        while list :
            temp = ListNode(list.pop())
            temp.next = head
            head = temp 
        return head
        
############################################################################################################################################################## 
        
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    # use the property of sorted lists 
    # solution with O(1) space complexity 
        dummy = curr = ListNode(-1)
        while l1 and l2 :
            if l1.val < l2.val :
                curr.next = l1
                l1 = l1.next
            else :
                curr.next = l2 
                l2 = l2.next
            curr = curr.next 
        if l1 :
                curr.next  = l1
        if l2 :
                curr.next = l2
                
        return dummy.next
