from typing import List

"""
odd jumps: arr[i] <= arr[j] and arr[j] is the smallest possible value
even jumps: arr[i] >= arr[j] and arr[j] is the largest possible value
"""


def oddEvenJumps(arr: List[int]) -> int:
    """
    time: n^2
    space: n
    """
    # goods = 0
    # size = len(arr)
    # for i in range(0, size):
    #     j = i
    #     jump = 1
    #     while j < size:
    #         next_j = j
    #
    #         if jump % 2 == 1:
    #             odd_list = list(filter(lambda x: arr[j] <= x, arr[j + 1:size]))
    #             if odd_list:
    #                 next_j = j + 1 + arr[j + 1:size].index(min(odd_list))
    #             else:
    #                 break
    #         else:
    #             even_list = list(filter(lambda x: arr[j] >= x, arr[j + 1:size]))
    #             if even_list:
    #                 next_j = j + 1 + arr[j + 1:size].index(max(even_list))
    #             else:
    #                 break
    #
    #         if next_j == j:
    #             break
    #         else:
    #             j = next_j
    #         jump += 1
    #     if j == size - 1:
    #         goods += 1
    # return goods

    """
    """
    print(sorted([[5,0],[4,1],[3,2],[2,3],[1,4],[0,5]]))


    # for i, v in enumerate(arr)
    #
    #
    #
    #
    # print(arr)
    # n = len(arr)
    # next_higher, next_lower = [0] * n, [0] * n
    #
    # stack = []
    # print(list(sorted([a, i] for i, a in enumerate(arr))))
    # for a, i in sorted([a, i] for i, a in enumerate(arr)):
    #     while stack and stack[-1] < i:
    #         print(f'stack a: {stack}')
    #         next_higher[stack.pop()] = i
    #         print(f'next_higher: {next_higher}')
    #     stack.append(i)
    #     print(f'stack b: {stack}')
    # print(next_higher)
    #
    # stack = []
    # print(list(sorted([-a, i] for i, a in enumerate(arr))))
    # for a, i in sorted([-a, i] for i, a in enumerate(arr)):
    #     while stack and stack[-1] < i:
    #         next_lower[stack.pop()] = i
    #     stack.append(i)
    # print(next_lower)
    #
    # higher, lower = [0] * n, [0] * n
    # higher[-1] = lower[-1] = 1
    # for i in range(n - 1)[::-1]:
    #     higher[i] = lower[next_higher[i]]
    #     lower[i] = higher[next_lower[i]]
    # return sum(higher)


if __name__ == '__main__':
    print(oddEvenJumps([10, 13, 12, 14, 15]) == 2)
    #
    # print(oddEvenJumps([2, 3, 1, 1, 4]) == 3)
    #
    # print(oddEvenJumps([5, 1, 3, 4, 2]) == 3)
