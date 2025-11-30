class Solution:
    def majorityElement(self, v: List[int]) -> List[int]:
        cnt1, cnt2 = 0, 0 # counts
        el1, el2 = None, None
        n = len(v)
        for i in range(n):
            if cnt1 == 0 and el2 != v[i]:
                cnt1 = 1
                el1 = v[i]
            elif cnt2 == 0 and el1 != v[i]:
                cnt2 = 1
                el2 = v[i]
            elif v[i] == el1:
                cnt1 += 1
            elif v[i] == el2:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        cnt1, cnt2 = 0, 0
        for i in range(n) :
            if v[i] == el1 :
                cnt1 += 1
            elif v[i] == el2 :
                cnt2 += 1
        res =[]
        if cnt1 > n//3 and el1 != None :
            res.append(el1)
        if cnt2 > n//3 and el2 != None :
            res.append(el2)
        return res
            

''' Extended Boyer Moore’s Voting Algorithm
    time complexity O(n)
    space complexity O(1) 
'''

########################################################################################################################################################

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dit = dict()
        res = []
        for n in nums :
            if n in dit :
                dit[n] += 1
            else :
                dit[n] = 1
        for n, c in dit.items() :
            if c > len(nums)//3 :
                res.append(n)
        return res

''' time complexity O(n) 
    space complexity O(n)
'''
