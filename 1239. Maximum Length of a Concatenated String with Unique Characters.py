class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        visit = [0] * 26

        def overlap(word):
            seen = set()
            for ch in word:
                if ch in seen or visit[ord(ch) - ord('a')] == 1:
                    return True
                seen.add(ch)
            return False

        def dfs(i):
            if i == n:
                return sum(visit)

            # exclude
            res = dfs(i + 1)

            # include
            if not overlap(arr[i]):
                for ch in arr[i]:
                    visit[ord(ch) - ord('a')] = 1

                res = max(res, dfs(i + 1))

                for ch in arr[i]:
                    visit[ord(ch) - ord('a')] = 0

            return res

        return dfs(0)

  ''' backtraing 
      time complexity : O(26 * 2 ^ n)
      space complexity : O(n)
'''


#########################################################################################################################################

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        masks = []

        for word in arr:
            mask = 0
            for ch in word:
                bit = 1 << (ord(ch) - ord('a'))
                if mask & bit:
                    mask = 0
                    break
                mask |= bit
            if mask:
                masks.append(mask)

        def dfs(i, curr_mask):
            if i == len(masks):
                return bin(curr_mask).count('1')

            res = dfs(i+1, curr_mask)

            if curr_mask & masks[i] == 0:
                res = max(res, dfs(i+1, curr_mask | masks[i]))

            return res

        return dfs(0, 0)


''' Backtracking + Bitmask Technique
      time complexity : O(2 ^ n)
      space complexity : O(n)

Use a 26-bit integer to represent characters 'a' → 'z'.

Bit mapping:
a → bit 0
b → bit 1
c → bit 2
...
z → bit 25

For a character:
bit = 1 << (ord(ch) - ord('a'))

Operations used:

1. Check duplicate inside word
   if mask & bit:
       character already exists

2. Add character to mask
   mask |= bit

3. Check overlap between two strings
   if curr_mask & word_mask == 0:
       no common characters

4. Merge two strings
   new_mask = curr_mask | word_mask

5. Count unique characters
   length = bin(mask).count('1')

Benefits:
- overlap check → O(1)
- merge sets → O(1)
- replaces visit[26] array with one integer

'''
