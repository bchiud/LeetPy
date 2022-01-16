from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    """
    pointers
    time: n^2
    space: n
    """
    # size = len(nums)
    # nums.sort()
    # result = []
    # for i in range(size - 2):
    #     if nums[i] > 0:
    #         break
    #     if i > 0 and nums[i] == nums[i - 1]:
    #         continue
    #     l, r = i + 1, size - 1
    #     while l < r:
    #         # print(f'i: {i}: {nums[i]}   j: {j}: {nums[j]}   k: {k}: {nums[k]}')
    #         cur = nums[i] + nums[l] + nums[r]
    #         if cur == 0:
    #             result.append([nums[i], nums[l], nums[r]])
    #             while l < r and nums[l] == nums[l + 1]:
    #                 l += 1
    #             while l < r and nums[r - 1] == nums[r]:
    #                 r -= 1
    #         if cur < 0:
    #             l += 1
    #         else:
    #             r -= 1
    # return result

    """
    hashset
    time: n^2
    space: n
    """
    # nums.sort()
    # result = []
    # size = len(nums)
    # for i in  range(size - 2):
    #     if nums[i] > 0:
    #         break
    #     if i == 0 or nums[i - 1] != nums[i]:
    #         seen = set()
    #         j = i + 1
    #         while j < size:
    #             complement = -nums[i] - nums[j]
    #             if complement in seen:
    #                 result.append([nums[i], complement, nums[j]])
    #                 while j < size - 1 and nums[j] == nums[j + 1]:
    #                     j += 1
    #             seen.add(nums[j])
    #             j += 1
    # return result

    """
    hashset (no sort)
    time: n^2
    space: n
    """
    dup, res = set(), set()
    seen = {}
    for i, vali in enumerate(nums):
        if vali not in dup:
            dup.add(vali)
            for j, valj in enumerate(nums[i+1:]):
                complement = -vali - valj
                if complement in seen and seen[complement] == i:
                    res.add(tuple(sorted((vali, complement, valj))))
                seen[valj] = i
    return list(res)

if __name__ == '__main__':
    print(threeSum([-1, 0, 1, 2, -1, -4]).sort() == [[-1, -1, 2], [-1, 0, 1]].sort())
    print(threeSum([]).sort() == [].sort())
    print(threeSum([0]).sort() == [].sort())
    print(threeSum([0, 0, 0]).sort() == [[0,0,0]].sort())
