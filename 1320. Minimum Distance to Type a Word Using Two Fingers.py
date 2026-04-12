from functools import lru_cache

class Solution:
    def minimumDistance(self, word: str) -> int:
        # Map each character to its keyboard coordinates
        def get_position(char):
            index = ord(char) - ord('A')
            return (index // 6, index % 6)

        # Manhattan distance between two positions
        def distance(p1, p2):
            if p1 is None:
                return 0  # free initial placement
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        n = len(word)

        @lru_cache(None)
        def dfs(index, finger1_pos, finger2_pos):
            # Base case
            if index == n:
                return 0

            current_pos = get_position(word[index])

            # Option 1: Use finger 1
            cost_using_f1 = distance(finger1_pos, current_pos) + dfs(index + 1, current_pos, finger2_pos)

            # Option 2: Use finger 2
            cost_using_f2 = distance(finger2_pos, current_pos) + dfs(index + 1, finger1_pos, current_pos)

            return min(cost_using_f1, cost_using_f2)

        return dfs(0, None, None)


"""     memorization solution 
        What is lru_cache:
        --------------
        - Automatically caches results of dfs states
        - Avoids recomputation of identical states
        - Converts exponential recursion → polynomial time
        - Requires all arguments to be hashable (tuples / None used)

        time complexity: O(n * 27 * 27) ≈ O(n)

        Space Complexity:
        -----------------
        - Memoization cache: O(n * 26 * 26)
        - Recursion stack: O(n)

        Overall: O(n * 26 * 26)

"""
