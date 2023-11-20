class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n-1
        mid = 0
        ## finding the pivot
        while l<r:
            mid = (l+r)//2
            if nums[mid]>nums[r]:
                l = mid+1
            else:
                r = mid
        ## searching for the element
        pivot = l
        l, r = 0, n-1
        while(l<=r):
            mid = (l+r)//2
            mid2 = (mid+pivot)%n
            if(nums[mid2]==target):
                return mid2
            elif(nums[mid2]<target):
                l = mid+1
            else:
                r = mid-1

        return -1
