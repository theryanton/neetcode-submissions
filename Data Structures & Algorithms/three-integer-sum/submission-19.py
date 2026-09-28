class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortednums = sorted(nums)
        i = 0
        seen = set()
        result = []
        
        for i in range(len(sortednums) - 2):
            if sortednums[i] in seen: 
                continue
            else:
                left = i + 1
                right = len(sortednums) - 1
                while left < right:
                    sum = sortednums[left] + sortednums[right] + sortednums[i]
                    if sum > 0: # 1 2 3, target = 2
                        right -= 1
                    elif sum < 0:
                        left += 1
                    else:
                        result.append([sortednums[i], sortednums[left], sortednums[right]])
                        right -= 1
                        left += 1
                        while sortednums[left] == sortednums[left - 1] and left < right:
                            left += 1
                seen.add(sortednums[i])
        return result
            
