from typing import List


def findNumbers(nums: List[int]) -> int:
    even_digits = 0
    for x in nums:
        digits = 0
        while x != 0:
            print(f'{x}: {digits}')
            x //= 10
            digits += 1
        if digits % 2 == 0:
            even_digits += 1
    return even_digits


if __name__ == '__main__':
    a = [555,901,482,1771]
    print(findNumbers(a) == 1)