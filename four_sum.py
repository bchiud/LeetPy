from typing import List


class Solution:
    """
    time: n ^ 3
    space: n => k space required for recursion; worst case k == n
    """
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.kSum(nums, target, 4)

    def kSum(self, nums: List[int], target: int, k: int) -> List[List[int]]:
        ans = []

        if len(nums) < k or target < nums[0] * k or nums[-1] * k < target:
            return ans

        if k == 2:
            return self.twoSum(nums, target)
        else:
            for i in range(len(nums)):
                if i > 0 and nums[i - 1] == nums[i]:
                    continue
                else:
                    for subset in self.kSum(nums[i + 1:], target - nums[i], k - 1):
                        ans.append([nums[i]] + subset)

        return ans

    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        i, j = 0, len(nums) - 1

        while i < j:
            total = nums[i] + nums[j]
            if total < target or (0 < i and nums[i - 1] == nums[i]):
                i += 1
            elif total > target or (j < len(nums) - 1 and nums[j] == nums[j + 1]):
                j -= 1
            else:
                ans.append([nums[i], nums[j]])
                i += 1
                j -= 1

        return ans


if __name__ == '__main__':
    s = Solution()
    assert s.fourSum([1,0,-1,0,-2,2], 0) == [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]