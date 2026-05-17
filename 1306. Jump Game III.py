class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = [False] * n
        queue = [start]
        visited[start] = True
        while queue:
            i = queue.pop()
            if arr[i] == 0:
                return True
            for nxt in (i + arr[i], i - arr[i]):
                if 0 <= nxt < n and not visited[nxt]:
                    visited[nxt] = True
                    queue.append(nxt)
        return False

'''
    BFS/DFS from start, visit reachable indices
    return True if any reachable index has value 0
    iterative avoids recursion limit issues
    time complexity : O(n)
    space complexity : O(n)
'''
