class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_streak = 0
        overall_max = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                current_streak = 0
            else:
                current_streak += 1
            overall_max = max(current_streak, overall_max)
            
        return overall_max
