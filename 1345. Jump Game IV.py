class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0

        indexi = defaultdict(list)
        for i in range(n):
            indexi[arr[i]].append(i)

        q = deque([0])
        visited = [False] * n
        visited[0] = True
        ans = 0

        while q:
            ans += 1
            for _ in range(len(q)):
                idx = q.popleft()

                if idx > 0 and not visited[idx - 1]:
                    if idx - 1 == n - 1:
                        return ans
                    visited[idx - 1] = True
                    q.append(idx - 1)

                if idx < n - 1 and not visited[idx + 1]:
                    if idx + 1 == n - 1:
                        return ans
                    visited[idx + 1] = True
                    q.append(idx + 1)

                for nei in indexi[arr[idx]]:
                    if not visited[nei]:
                        if nei == n - 1:
                            return ans
                        visited[nei] = True
                        q.append(nei)

                # KEY: clear the group so we never iterate it again
                indexi[arr[idx]] = []

        return -1

'''
    BFS level by level
    after visiting all indices with same value, clear that group
    this ensures each index is processed at most once
    without clearing: worst case O(n^2) (e.g. all same values)
    with clearing: O(n) total since each group is iterated exactly once
    time complexity : O(n)
    space complexity : O(n)
'''
