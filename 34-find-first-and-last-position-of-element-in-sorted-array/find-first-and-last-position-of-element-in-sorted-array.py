class Solution:
    def lowerBound(self, nums, target):
        n = len(nums)
        l = 0
        r = n-1
        ans = n
        while l <= r:
            mid = (l+r)// 2
            if nums[mid] >= target:
                ans = mid
                r = mid - 1
            else:
                l = mid+1 
        return ans
    
    def uperBound(self, nums, target):
        n = len(nums)
        l = 0
        r = n-1
        ans = n
        while l <= r:
            mid = (l+r)// 2
            if nums[mid] > target:
                ans = mid
                r = mid - 1
            else:
                l = mid+1 

        
        return ans 
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lb = self.lowerBound(nums, target)
        up = self.uperBound(nums, target)

        if lb == up:
            #not present
            return [-1, -1]
        else: 
            return [lb, up-1]
        