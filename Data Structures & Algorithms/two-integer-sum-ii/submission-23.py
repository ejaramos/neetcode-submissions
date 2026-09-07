class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Approach 1: use hash map to store seen values -> not O(1)
        # complements = {}
        # for i in range( len(numbers) ):
        #     target_complement = target - numbers[i]
            
        #     print(target_complement, complements)
        #     if target_complement in complements.keys():
        #         return [ complements[target_complement][1], i+1] 

        #     complements[numbers[i]] = (i, numbers[i])
        
        # Approach 2: check for membership of target
        # breaks on duplicates

        # for i in range(len(numbers)):
        #     complement = target - numbers[i]
        #     # print([*numbers[:i], *numbers[i:]])
        #     # is complement in the list
        #     if complement in [*numbers[:i], *numbers[i:]]:
        #         if complement == numbers[i]:
        #             return [i+1, [*numbers[:i], *numbers[i:]].index(complement) + i + 1 ]
        #         return [i+1, [*numbers[:i], *numbers[i:]].index(complement) + 1]

        # approach 3
        # can we use non-decreasing property?
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]
            # print(f"left: {left}, right: {right} | current = {numbers[left]+numbers[right]}")
            
            # print()
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            
            if current_sum > target:
                right -= 1

            if current_sum < target:
                left += 1
        
        return [left+1, right+1]







