class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = {} 
        for i, ele in enumerate(nums):
            if ele in hashMap:
                return True
            hashMap[ele] = i
        return False
