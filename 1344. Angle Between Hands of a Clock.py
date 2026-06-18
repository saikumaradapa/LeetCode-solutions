class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        min_angle = minutes * 6           # 360/60 = 6 degrees per minute
        hr_angle = (hour % 12) * 30 + minutes * 0.5  # 360/12=30 per hour + 0.5 per minute
        diff = abs(hr_angle - min_angle)
        return min(diff, 360 - diff)

'''
    minute hand: 6 degrees per minute
    hour hand: 30 degrees per hour + 0.5 degrees per minute (it moves with minutes)
    take absolute difference, return the smaller of the two possible angles
    time complexity : O(1)
    space complexity : O(1)
'''
