from typing import List


def sortedSquares(nums: List[int]) -> List[int]:
    n = len(nums)
    left, right = 0, n - 1
    ans = [0] * n
    for i in range(n - 1, -1, -1):
        if abs(nums[left]) >= abs(nums[right]):
            ans[i] = nums[left] ** 2
            left += 1
        else:
            ans[i] = nums[right] ** 2
            right -= 1

    return ans


if __name__ == '__main__':
    a = [-4, -1, 0, 3, 10]
    print(sortedSquares(a) == [0, 1, 9, 16, 100])

    b = [-7, -3, 2, 3, 11]
    print(sortedSquares(b) == [4, 9, 9, 49, 121])
