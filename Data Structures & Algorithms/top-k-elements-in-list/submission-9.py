class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for num in nums:
            hash_map[num] = hash_map.get(num,0) + 1
    
        res = []
        frequency = [[] for i in range(len(nums))]
        for key ,val in hash_map.items():
            frequency[val-1].append(key)

        for i in range(len(nums)-1, -1, -1):
            for val in frequency[i]:
                res.append(val)
                if len(res) == k:
                    return res
        
 