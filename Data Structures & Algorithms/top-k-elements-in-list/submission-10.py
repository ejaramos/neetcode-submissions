class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        max_count = len(nums)
        groups = [[] for x in range(max_count + 1)]
        
        for val, count in counts.items():
            groups[count].append(val)
        
        result = []
        for i in range(max_count, 0, -1):
            for val in groups[i]:
                result.append(val)
                if len(result) == k:
                    return result
        return result