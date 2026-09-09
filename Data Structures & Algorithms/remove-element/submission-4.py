class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        temp_list = ["_"]* len(nums)
        for i in range(len(nums)):
            print(f"i = {i}, j = {k}, temp ={ temp_list}")      
            if nums[i] == val:
                continue
            else:
                temp_list[k] = nums[i]
                k += 1
        
        for i in range(len(nums)):
            nums[i] = temp_list[i]

        # print(f"k = {val}, nums = {nums}")
        return k

