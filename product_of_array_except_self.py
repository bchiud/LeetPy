from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]):
        """
        brute force:
        time: n^2
        space: n


        time: n
        space: n
        """
        n = len(nums)
        total_product_sans_zeroes = 1
        zero = [0] * n
        zeroes = 0

        for i, v in enumerate(nums):
            if v == 0:
                zero[i] = 1
                zeroes += 1
            else:
                total_product_sans_zeroes *= v

        if zeroes > 1:
            return [0] * n

        ans = []

        for i, v in enumerate(nums):
            if v == 0:
                ans.append(total_product_sans_zeroes)
            elif zeroes > 0:
                ans.append(0)
            else:
                ans.append(total_product_sans_zeroes // v)

        return ans

    def productExceptSelfCleaner(self, nums: List[int]):
        n = len(nums)
        output = []

        beforeProduct = 1
        for i in range(0, n):
            output.append(beforeProduct)
            beforeProduct = beforeProduct * nums[i]

        afterProduct = 1
        for i in range(n - 1, -1, -1):
            output[i] = output[i] * afterProduct
            afterProduct = afterProduct * nums[i]

        return output


if __name__ == '__main__':
    s = Solution()
    assert s.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert s.productExceptSelfCleaner([1, 2, 3, 4]) == [24, 12, 8, 6]
