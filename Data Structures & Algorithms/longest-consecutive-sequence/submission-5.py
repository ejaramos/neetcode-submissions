class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # empty array
        # if not nums:
        #     return 0

        overall_max = 0
        nums_set = set(nums)
        starts = set()

        for num in nums_set:
            if num - 1 not in nums_set:
                starts.add(num)

        for each in starts:
            current = each
            streak = 0
            while True:
                streak += 1
                current += 1
                if current not in nums_set:
                    break
            overall_max = max(overall_max, streak)

        return overall_max

        