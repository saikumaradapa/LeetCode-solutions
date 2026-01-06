from collections import deque

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        level = 0
        max_sum = float('-inf')
        answer_level = 1

        while queue:
            level += 1
            level_sum = 0

            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                answer_level = level

        return answer_level

''' BFS
    time complexity : O(n)
    space complexity : O(w) - w max width of the tree
'''
