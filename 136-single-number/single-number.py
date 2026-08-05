class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = []

        for num in nums:
            if num in ans:
                ans.remove(num)
            else:
                ans.append(num)
        
        return ans[0]