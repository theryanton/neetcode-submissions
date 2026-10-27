class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = l + (r-l) // 2
            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m
        
        pivot = l
        left, right = 0, len(nums) - 1
        if nums[pivot] <= target <= nums[right]:
            left = pivot
        else:
            right = pivot - 1

        
        while left <= right:
            middle = left + (right-left) // 2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle
        return -1
        


        