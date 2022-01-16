from typing import List


def checkIfExist(arr: List[int]) -> bool:
    s = set()
    size = len(arr)
    for i in range(size):
        val = arr[i]
        if val * 2 in s or (val % 2 == 0 and val / 2 in s):
            return True
        s.add(val)
    return False


if __name__ == '__main__':
    a = [10, 2, 5, 3]
    print(checkIfExist(a) is True)

    b = [7, 1, 14, 11]
    print(checkIfExist(b) is True)

    c = [3, 1, 7, 11]
    print(checkIfExist(c) is False)
