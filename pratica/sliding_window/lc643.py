class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = sum(nums[:k])
        output = window

        for i in range (len(nums) - k):
            window = window - nums[i] + nums[i+k]
            output = max(output, window)

        return output / k