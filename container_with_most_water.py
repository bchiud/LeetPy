from typing import List


def maxArea(height: List[int]) -> int:
    """
    time: n^2:
    space: 1
    """
    # volume = 0
    # for i, a in enumerate(height):
    #     for j, b in enumerate(height):
    #         if i == j:
    #             continue
    #         candidate = (j - i) * min(a, b)
    #         volume = max(volume, candidate)
    # return volume

    """
    time: n
    space: 1
    """
    i = 0
    j = len(height) - 1
    volume = 0
    while i < j:
        volume = max(volume, (j - i) * min(height[i], height[j]))
        if (height[i] < height[j]):
            i += 1
        else:
            j -= 1
    return volume


if __name__ == '__main__':
    print(maxArea([1,8,6,2,5,4,8,3,7]) == 49)
    print(maxArea([1,1]) == 1)
    print(maxArea([4,3,2,1,4]) == 16)


