class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        ps = 0
        ps_count = {0: 1}

        for num in nums:
            ps += num
            if (ps - k) in ps_count:
                count += ps_count[ps - k]
            if ps in ps_count:
                ps_count[ps] += 1
            else:
                ps_count[ps] = 1