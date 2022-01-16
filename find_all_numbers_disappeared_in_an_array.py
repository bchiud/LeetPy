from typing import List


def findDisappearedNumbers(nums: List[int]) -> List[int]:
    for n in nums:
        index = abs(n) - 1
        if nums[index] > 0:
            nums[index] *= -1

    return [i + 1 for i in range(len(nums)) if nums[i] > 0]
    
    # original = set(nums)
    # all = set([i for i in range(1, len(nums) + 1)])
    #
    # return list(all - original)


if __name__ == '__main__':
    a = [4, 3, 2, 7, 8, 2, 3, 1]
    print(findDisappearedNumbers(a) == [5, 6])
