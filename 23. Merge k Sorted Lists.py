import heapq

###############################################################################
# Approach 1: Min-Heap (Priority Queue)
# Time: O(N log k)
# Space: O(k)
###############################################################################
class SolutionHeap:
    def mergeKLists(self, lists):
        min_heap = []
        for idx, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, idx, node))
        
        dummy = ListNode(-1)
        curr = dummy
        counter = len(lists)
        while min_heap:
            _, _, min_node = heapq.heappop(min_heap)
            curr.next = min_node
            curr = curr.next
            if min_node.next:
                heapq.heappush(min_heap, (min_node.next.val, counter, min_node.next))
                counter += 1
        return dummy.next

###############################################################################
# Approach 2: Sequential Pairwise Merge
# Time: O(N * k)
# Space: O(1)
###############################################################################
class SolutionSequential:
    def mergeKLists(self, lists):
        if not lists:
            return None

        curr = lists[0]
        for next_list in lists[1:]:
            curr = self.merge(curr, next_list)
        
        return curr
    
    def merge(self, h1, h2):
        curr = dummy = ListNode(-1)
        while h1 and h2:
            if h1.val <= h2.val:
                curr.next = h1
                h1 = h1.next
            else:
                curr.next = h2
                h2 = h2.next
            curr = curr.next
        if h1:
            curr.next = h1
        if h2:
            curr.next = h2
        return dummy.next

###############################################################################
# Approach 3: Flatten to Array, Sort, Rebuild
# Time: O(N log N)
# Space: O(N)
###############################################################################
class SolutionArraySort:
    def mergeKLists(self, lists):
        arr = []
        for node in lists:
            while node:
                arr.append(node.val)
                node = node.next
        arr.sort()
        dummy = ListNode(-1)
        curr = dummy
        for val in arr:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next
