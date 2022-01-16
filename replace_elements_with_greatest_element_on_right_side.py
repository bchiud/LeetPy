from typing import List


def replaceElements(arr: List[int]) -> List[int]:
    n = len(arr)

    last_largest = arr[n - 1]
    arr[n - 1] = -1
    for i in range(n - 2, -1, -1):
        cur_val = arr[i]
        arr[i] = last_largest
        if cur_val > last_largest:
            last_largest = cur_val

    return arr

if __name__ == '__main__':
    a = [17, 18, 5, 4, 6, 1]
    replaceElements(a)
    print(a == [18, 6, 6, 6, 1, -1])

    b = [400]
    replaceElements(b)
    print(b == [-1])
