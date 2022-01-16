class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        missing = 0
        for n in nums:
            missing ^= n
        return missing