class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        output = 0

        while l < r:
            if height[l] < height[r]:
                area = (height[l] * (r - l))
                output = max(output, area)
                l += 1
            else:
                area = (height[r] * (r - l))
                output = max(output, area)
                r -= 1
        
        return output