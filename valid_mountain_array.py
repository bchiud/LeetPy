from typing import List


def validMountainArray(arr: List[int]) -> bool:
    n = len(arr)
    i = 0
    j = n - 1
    while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1
    while 0 < j and arr[j - 1] > arr[j]:
            j -= 1
    return 0 < i == j < n - 1


    # size = len(arr)
    # increasing = False
    # decreasing = False
    #
    # if size < 3:
    #     return False
    #
    # if arr[0] >= arr[1]:
    #     return False
    #
    # if arr[size - 2] <= arr[size - 1]:
    #     return False
    #
    #
    # for i in range(size - 2):
    #     if not decreasing and not increasing and arr[i] < arr[i + 1]:
    #         increasing = True
    #     elif not decreasing and increasing and arr[i] < arr[i + 1]:
    #         pass
    #     elif not decreasing and increasing and arr[i] > arr[i + 1]:
    #         decreasing = True
    #     elif decreasing and arr[i] > arr[i + 1]:
    #         pass
    #     else:
    #         return False
    #
    # return True

if __name__ == '__main__':
    a = [2,1]
    print(validMountainArray(a) == False)

    b = [3,5,5]
    print(validMountainArray(b) == False)

    c = [0,3,2,1]
    print(validMountainArray(c) == True)

    d = [3,7,6,4,3,0,1,0]
    print(validMountainArray(d) == False)