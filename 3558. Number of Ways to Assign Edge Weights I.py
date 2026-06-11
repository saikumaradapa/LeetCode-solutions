from collections import deque
class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(edges) + 1

        # build adjacency list
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # BFS to find max depth from root (node 1)
        depth = [0] * (n + 1)
        visited = [False] * (n + 1)
        q = deque([1])
        visited[1] = True
        max_depth = 0
        while q:
            node = q.popleft()
            for adj in graph[node]:
                if not visited[adj]:
                    visited[adj] = True
                    depth[adj] = depth[node] + 1
                    max_depth = max(max_depth, depth[adj])
                    q.append(adj)

        # answer = 2^(max_depth - 1) mod MOD
        return pow(2, max_depth - 1, MOD)

'''
    find max depth d (edges from root to deepest node)
    each edge assigned 1 (odd) or 2 (even)
    sum is odd ↔ odd count of 1s among d edges
    count of subsets with odd size from d items = 2^(d-1)
    identity: C(d,1)+C(d,3)+C(d,5)+... = 2^(d-1)
    time complexity : O(n)
    space complexity : O(n)
'''
