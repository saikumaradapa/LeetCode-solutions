class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left = moves.count('L')
        right = moves.count('R')
        free = moves.count('_')

        return abs(right - left) + free
        
''' count fixed movements and flexible moves
    use all '_' in direction that maximizes distance
    time complexity : O(n)
    space complexity : O(1)
'''
