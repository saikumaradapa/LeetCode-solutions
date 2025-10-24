# required optimal solution with constant space 

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        groupPrev = dummy 

        while True :
            kth = self.getKth(groupPrev, k)
            if not kth :
                break 
            groupNext = kth.next 

            prev, curr = kth.next, groupPrev.next 
            while curr != groupNext :
                temp = curr.next 
                curr.next = prev 
                prev = curr 
                curr = temp 
            temp = groupPrev.next 
            groupPrev.next = kth 
            groupPrev = temp 
        
        return dummy.next 

    def getKth(self, curr, k) :
        while curr and k > 0 :
            curr = curr.next 
            k -= 1
        return curr


''' time complexity : O(n)        
    space complexity : O(1)
'''




##############################################################################################################################################################
# taking individual groups into a arr and reversing 

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
      arr = []
      tail = None
      def reverse(h) :
        prev = None
        curr = h
        while curr :
          temp = curr.next 
          curr.next = prev 
          prev = curr 
          curr = temp
        return prev
      def kth(h, k):
          for i in range(1, k):
              if h.next:
                  h = h.next
              else:
                  return None
          return h

      if not kth(head, k) :
        return head
      temp = head 
      while temp :
        kthNode = kth(temp, k)
        if kthNode :
          next = kthNode.next 
          kthNode.next = None 
          temp = reverse(temp)
          arr.append(temp)
          temp = next 
        else :
          tail = temp 
          break 

      
      h = dummy = ListNode(0)
      for node in arr :
        dummy.next = node
        while dummy.next :
          dummy = dummy.next 
      if tail :
        dummy.next = tail 
      return h.next 

''' time complexity : O(n)
    space complexity : O(n)
'''

##############################################################################################################################################################
# converting linked list into arr and processing 

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        h = head 
        while h :
            arr.append(h.val)
            h = h.next 
        for i in range(0,len(arr), k) :
            if len(arr[i:i+k]) < k :
                break 
            else :
                temp = arr[i:i+k]            
                arr[i:i+k] = temp[::-1]
                print(arr)
        h = head 
        while h :
            h.val = arr.pop(0)
            h = h.next 
        return head  

''' time complexity : O(n)        
    space complexity : O(n)
''' 
