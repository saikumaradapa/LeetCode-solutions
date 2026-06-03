class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        # earliest a land ride can finish
        min_land_finish = min(s + d for s, d in zip(landStartTime, landDuration))
        # earliest a water ride can finish
        min_water_finish = min(s + d for s, d in zip(waterStartTime, waterDuration))

        res = float('inf')

        # land first (finishing as early as possible), then each water ride
        for ws, wd in zip(waterStartTime, waterDuration):
            res = min(res, max(min_land_finish, ws) + wd)

        # water first, then each land ride
        for ls, ld in zip(landStartTime, landDuration):
            res = min(res, max(min_water_finish, ls) + ld)

        return res

'''
    do exactly one land + one water ride, either order
    for land→water: finish = max(land_finish, water_start) + water_duration
    this grows with land_finish, so always pick the earliest-finishing land ride
    symmetric for water→land
    precompute min finish per category, then try each ride of the other category
    time complexity : O(n + m)
    space complexity : O(1)
'''
