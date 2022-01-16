class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup, missing = 0, 0
        for n in nums:
            cur = abs(n)
            if nums[cur - 1] < 0:
                dup = cur
            else:
                nums[cur - 1] *= -1

        for i, v in enumerate(nums):
            if v > 0:
                missing = i + 1
                break

        return [dup, missing]


if __name__ == '__main__':
    s = Solution()
    assert s.findErrorNums([1, 2, 2, 4]) == [2, 3]
    assert s.findErrorNums([1, 1]) == [1, 2]
