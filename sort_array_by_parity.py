from typing import List


def sortArrayByParity(A: List[int]) -> List[int]:
    left = 0
    right = len(A) - 1

    while left < right:
        while left < len(A) and A[left] % 2 == 0:
            left += 1
        while right > 0 and A[right] % 2 == 1:
            right -= 1
        if left < right:
            A[left], A[right] = A[right], A[left]

    return A


if __name__ == '__main__':
    a = [3, 1, 2, 4]
    print(sortArrayByParity(a))
