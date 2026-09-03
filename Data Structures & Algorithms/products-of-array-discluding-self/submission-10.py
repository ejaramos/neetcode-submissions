class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]* len(nums)
        left = [1]* ( len(nums) + 1 )
        right = [1]* ( len(nums) + 1 )
        for i in range(len(nums)):
            left_ptr = i+1
            right_ptr = len(nums) - (left_ptr)
            
            left[left_ptr] = left[left_ptr-1]*nums[i] 
            right[right_ptr] = right[right_ptr+1] *nums[right_ptr]
        
        for i in range(len(nums)):
            result[i] = left[i] * right[i+1]
        return result
        