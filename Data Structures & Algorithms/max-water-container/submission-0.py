class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_water = 0
        while left < right:
            current_water = (right - left)*min(heights[left], heights[right])
        
            max_water = max(current_water, max_water)
            if heights[left] > heights[right]:
                right -= 1
                continue
            left += 1

        return max_water