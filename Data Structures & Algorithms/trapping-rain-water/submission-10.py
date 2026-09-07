class Solution:
    def trap(self, height: List[int]) -> int:

        # print("--- Collect Left Water ---")
        water_level = 0
        # pass from the left
        left_collect = [0] * len(height)
        for i in range(0, len(height) - 1):
            # print(f"water_level = {water_level}")
            if water_level > height[i]:
                left_collect[i] = water_level
             # left
            if i == 0 and height[i] > height[i+1]:
                # print("left max", i)
                # update water_level
                water_level = max(height[i], water_level)
                continue

            # check if max
            if  height[i] > height [i+1] :
                water_level = max(height[i], water_level)
                # print("max", i)
                continue
            
            # if not a max, add water water_trapped
            left_collect[i] = water_level

        # print("--- Collect Right Water ---")
        water_level = 0
        right_collect = [0] * len(height)
        for i in range(len(height) - 1, 0, -1):
            # print(f"water_level = {water_level}")
            if water_level > height[i]:
                right_collect[i] = water_level

            # right max
            if height[i] > height[i-1] and i == len(height) - 1:
                # print("right max", i)
                water_level = max(height[i], water_level)
                continue
            
            # check if max
            if height[i - 1] < height[i] :
                water_level = max(height[i], water_level)
                # print("max", i)
                continue

        # calculate water
        water_trapped = 0
        for i in range(len(height) - 1):
            # print(f"water collected: {water_trapped}")
            water_trapped += max( min(left_collect[i], right_collect[i]) - height[i], 0)

        # print(height)
        # print(left_collect) 
        # print(right_collect)
        return water_trapped



            