class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack = []
        for i in intervals :
            if stack and stack[-1][1] >= i[0] :
                stack[-1][1] = max(i[1], stack[-1][1])
            else :
                stack.append(i)
        return stack


        
''' solution using a stack 
    time complexity : O(nlogn) 
    space complexity : O(n)  
''' 
