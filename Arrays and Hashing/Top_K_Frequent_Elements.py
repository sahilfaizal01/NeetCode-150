class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for n in nums:
            res[n] = 1 + res.get(n,0)
        sorted_keys = sorted(res,key=res.get,reverse=True)
        return sorted_keys[:k]
