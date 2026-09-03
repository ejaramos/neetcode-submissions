class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # base case, check len(set(nums))
        if len(set(nums)) < len(nums):
            return True
        return False

        