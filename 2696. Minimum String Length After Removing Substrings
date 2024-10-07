class Solution:
    def minLength(self, s: str) -> int:
        # Continue processing while "AB" or "CD" substrings exist
        while "AB" in s or "CD" in s:
            if "AB" in s:
                # Remove all occurrences of "AB"
                s = s.replace("AB", "")
            elif "CD" in s:
                # Remove all occurrences of "CD"
                s = s.replace("CD", "")

        return len(s)
