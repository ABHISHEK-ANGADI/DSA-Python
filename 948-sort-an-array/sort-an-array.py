class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Base case: arrays with 0 or 1 element are already sorted
        if len(nums) <= 1:
            return nums
        
        # Split the array into two halves
        mid = len(nums) // 2
        left_half = self.sortArray(nums[:mid])
        right_half = self.sortArray(nums[mid:])
        
        # Merge the sorted halves together
        return self.merge(left_half, right_half)
    
    def merge(self, left: List[int], right: List[int]) -> List[int]:
        sorted_arr = []
        i = j = 0
        
        # Compare elements from both halves and merge them in order
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_arr.append(left[i])
                i += 1
            else:
                sorted_arr.append(right[j])
                j += 1
                
        # Append any remaining elements
        sorted_arr.extend(left[i:])
        sorted_arr.extend(right[j:])
        
        return sorted_arr
