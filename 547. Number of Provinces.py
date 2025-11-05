# input : adjacency matrix representation 

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected) 
        visited = [0] * (n)

        def dfs(node) :
            visited[node] = 1
            for i in range(n) :
                if isConnected[node][i] == 1 and visited[i] == 0 :
                    dfs(i)
        res = 0
        for i in range(n) :
            if visited[i] == 0 :
                res += 1
                dfs(i)
        return res

''' time complexity : O(n^2)        
    space complexity : O(n)
'''

#############################################################################################################################################################################

