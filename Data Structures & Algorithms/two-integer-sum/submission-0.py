class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        single pass

        iterate:
            - look at subarray
        '''
        for i in range( len(nums) ):
            sub_array = [ x for x in nums[i+1:] ]
            
            for j, v in enumerate (sub_array):
                if nums[i] + v == target:
                    return [i, i+j+1]