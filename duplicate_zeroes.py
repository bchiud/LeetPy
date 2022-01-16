from typing import List


def duplicateZeros(arr: List[int]) -> None:
    """
    Do not return anything, modify arr in-place instead.
    """
    zeroes = arr.count(0)
    size = len(arr)

    for i in range(size - 1, -1, -1):
        # print(f'Before - i: {i}, zeroes: {zeroes}, arr: {arr}')
        if i + zeroes < size:
            arr[i + zeroes] = arr[i]
        if arr[i] == 0:
            zeroes -= 1
            if i + zeroes < size:
                arr[i + zeroes] = 0
        # print(f'After - i: {i}, zeroes: {zeroes}, arr: {arr}')


def compare_list(input: List, output: List) -> bool:
    return input == output


if __name__ == '__main__':
    a = [1, 1, 0, 1, 1]
    duplicateZeros(a)
    print(a == [1, 1, 0, 0, 1])

    b = [0, 1, 7, 6, 0, 2, 0, 7]
    duplicateZeros(b)
    print(b == [0, 0, 1, 7, 6, 0, 0, 2])

    c = [8, 4, 5, 0, 0, 0, 0, 7]
    duplicateZeros(c)
    print(c == [8, 4, 5, 0, 0, 0, 0, 0])
