# Eulerian path problem | Hierholzer Algorithm | 332. Reconstruct Itinerary
# marked for revisit the approach
# O(nlogn) - time complexity 
# psudo code : https://youtu.be/8MpoO2zA2l4?si=563k7SsjwYiQCOt_

from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        # sort reverse so smallest is popped last
        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)

        route = []

        def dfs(node):
            while adj[node]:
                dfs(adj[node].pop())
            route.append(node)

        dfs("JFK")
        return route[::-1]

###############################################################################################################################

# TLE 

from collections import defaultdict

class Solution:
    def findItinerary(self, tickets):
        n = len(tickets)
        adj = defaultdict(list)
        
        tickets.sort()  # ensures lexical order
        
        for src, dst in tickets:
            adj[src].append(dst)
        
        used = defaultdict(int)  # how many edges used per node
        res = ["JFK"]

        def dfs(node):
            if len(res) == n + 1:
                return True
            
            if used[node] == len(adj[node]):
                return False
            
            for i in range(len(adj[node])):
                if i < used[node]:
                    continue
                
                used[node] += 1
                res.append(adj[node][i])
                
                if dfs(adj[node][i]):
                    return True
                
                used[node] -= 1
                res.pop()
            
            return False

        dfs("JFK")
        return res

''' backtracking | TLE
- Sort tickets lexicographically.
- Build adjacency list.
- Use DFS backtracking from "JFK".
- Track how many edges from each node are used.
- Stop when path length == n + 1.

Time Complexity:
- O(n log n) for sorting
- O(n!) worst case due to backtracking permutations

Space Complexity:
- O(n) for adjacency list
- O(n) recursion stack
- O(n) result storage

'''
