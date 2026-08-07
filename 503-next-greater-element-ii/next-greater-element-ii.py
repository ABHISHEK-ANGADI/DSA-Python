from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n  # Initialize the entire result array with -1
        st = []         # Monotonic stack to store the elements
        
        # Traverse backwards from 2*n - 1 down to 0 to simulate doubling the array
        for i in range(2 * n - 1, -1, -1):
            curr_idx = i % n  # Get the actual index in the original array
            
            # Pop elements from stack that are smaller than or equal to the current element
            while len(st) > 0 and st[-1] <= nums[curr_idx]:
                st.pop()
                
            # Only populate the answer during the first pass (actual array indices)
            if i < n:
                if len(st) > 0:
                    ans[curr_idx] = st[-1]
            
            # Push the current element onto the stack
            st.append(nums[curr_idx])
            
        return ans
