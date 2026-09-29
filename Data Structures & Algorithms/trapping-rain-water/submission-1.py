class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        result = 0
        
        # calculate prefix array of max height
        pre = [0] * n
        pre[0] = height[0]
        for i in range(1, n):
            pre[i] = max(height[i], pre[i-1])
        
        # calculate suffix array
        suf = [0] * n
        suf[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            suf[i] = max(height[i], suf[i+1])

        for i in range(n):
            result += min(pre[i], suf[i]) - height[i]
        return result

        
