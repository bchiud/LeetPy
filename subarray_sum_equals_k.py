from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        time: n^3 => sum takes n time
        space: 1
        """
        count = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if sum(nums[i:j + 1]) == k:
                    count += 1
        return count

    def subarrayCumulativeSum(self, nums: List[int], k: int) -> int:
        """
        time: n^2 => sum takes n time
        space: 1
        """
        count = 0
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]
                if total == k:
                    count += 1
        return count

    def subarraySumHashMap(self, nums: List[int], k: int) -> int:
        """
        time: n
        space: n
        """
        count = total = 0
        sum_to_num_occurances_of_sum = defaultdict(int)
        sum_to_num_occurances_of_sum[0] += 1

        for i in range(len(nums)):
            total += nums[i]
            count += sum_to_num_occurances_of_sum.get(total - k, 0)
            sum_to_num_occurances_of_sum[total] += 1

        return count
