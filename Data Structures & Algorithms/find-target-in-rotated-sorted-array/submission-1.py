class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        pivot = 0

        while l<r:
            m = l + (r-l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
            pivot = l

        def binary_search(left: int, right: int) -> int:
            while left<=right:
                mid = left + (right-left) // 2
                if nums[mid] < target:
                    left = mid+1
                elif nums[mid] > target:
                    right = mid-1
                else:
                    return mid
            return -1

        
        if nums[pivot] <= target <= nums[-1]:
            return binary_search(pivot, len(nums) - 1)
        else: 
            return binary_search(0, pivot - 1)