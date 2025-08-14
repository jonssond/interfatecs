class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i+1, len(nums)-1
            while l < r:
                summ = (nums[l] + nums[r] + nums[i])
                if summ > 0:
                    r -= 1
                elif summ < 0:
                    l += 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1

        return result