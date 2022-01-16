from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)

        if n < 3:
            return

        nums.sort()
        closest = None
        for i in range(n - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            j, k = i + 1, n - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total == target:
                    return total
                elif abs(total - target) < (abs(closest - target) if closest is not None else float('inf')):
                    print(f'{abs(total - target)} {(abs(closest - target) if closest else float("inf"))}')
                    closest = total
                    print(f'{nums[i]} {nums[j]} {nums[k]} : {total} {closest}')

                if total < target:
                    j += 1
                elif total >= target:
                    k -= 1

        return closest


if __name__ == '__main__':
    s = Solution()
    s.threeSumClosest([0, 2, 1, -3], 1)
