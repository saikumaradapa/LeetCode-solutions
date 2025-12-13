class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        categories = ["electronics", "grocery", "pharmacy", "restaurant"]
        cat_index = {cat: i for i, cat in enumerate(categories)}
        valid = []
        for idx in range(len(code)):
            # Check code validity
            if (
                code[idx] and
                businessLine[idx] in cat_index and
                isActive[idx] and
                all(ch.isalnum() or ch == "_" for ch in code[idx])
            ):
                valid.append((cat_index[businessLine[idx]], code[idx]))
        
        # Sort first by category index, then lex by code
        valid.sort()
        return [c for _, c in valid]

''' 
    time complexity : O(n * m + n log n)
    space complexity : O(n)
'''
