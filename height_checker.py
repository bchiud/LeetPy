import collections
from typing import List


def heightChecker(heights: List[int]) -> int:
    count = collections.Counter(heights)
    print(count)
    cur_val = 1
    diff = 0
    for h in heights:
        while count[cur_val] == 0:
            cur_val += 1
        print(f'h: {h}, cur_val: {cur_val}')
        if h != cur_val:
            diff += 1
        count[cur_val] -= 1

    return diff


if __name__ == '__main__':
    a = [1, 1, 4, 2, 1, 3]
    print(heightChecker(a) == 3)

    # b = [5, 1, 2, 3, 4]
    # print(heightChecker(b) == 5)
    #
    # c = [1, 2, 3, 4, 5]
    # print(heightChecker(c) == 0)
