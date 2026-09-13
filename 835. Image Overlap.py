class Solution:
    def largestOverlap(self, img1, img2):
        n = len(img1)
        res = 0
        for dr in range(-(n-1), n):
            for dc in range(-(n-1), n):
                curr = 0
                for r in range(n):
                    for c in range(n):
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and img1[r][c] == 1 and img2[nr][nc] == 1:
                            curr += 1
                res = max(res, curr)
        return res
