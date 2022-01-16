class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0

        while nums:
            left = right = nums.pop()
            while left - 1 in nums:
                left -= 1
                nums.remove(left)
            while right + 1 in nums:
                right += 1
                nums.remove(right)
            longest = max(longest, right - left + 1)

        return longest