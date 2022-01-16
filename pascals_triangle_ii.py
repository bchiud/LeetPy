from typing import List


def getRow(rowIndex: int) -> List[int]:
    """
    time: n^2
    space: n^2
    """
    # if rowIndex == 0:
    #     return [1]
    # elif rowIndex == 1:
    #     return [1, 1]
    #
    # base = getRow(rowIndex - 1)
    # new = [1]
    # for i in range(1, len(base), 1):
    #     new.append(base[i - 1] + base[i])
    # new.append(1)
    #
    # return new

    """
    time: k^2
    space: k
    """
    # if rowIndex == 0:
    #     return [1]
    # base = [1, 1]
    # while len(base) != rowIndex + 1:
    #     new = [1]
    #     for i in range(1, len(base), 1):
    #         new.append(base[i - 1] + base[i])
    #     new.append(1)
    #     base = new
    #
    # return base

    """
    time: k^2
    space: k
    [1, 2, 1, 1, 1]
    [1, 3, 3, 1, 1]
    [1, 4, 6, 4, 1]
    """
    pascal = [1] * (rowIndex + 1)
    for end in range(2, rowIndex + 1):
        for start in range(1, end):
            pascal[end - start] += pascal[end - start - 1]
    return pascal

    """
    time: k
    space: k
    """
    # triangle = [1]
    #
    # for i in range(1, rowIndex + 1):
    #     triangle.append(triangle[i - 1] * (rowIndex - (i - 1)) // i)
    #     print(triangle)
    #
    # return triangle

    """
    time: k
    space: k
    """
    # triangle = [0] * (rowIndex + 1)
    # triangle[0] = triangle[rowIndex] = 1
    #
    # for i in range(0, rowIndex >> 1):
    #     print(triangle)
    #     val = triangle[i] * (rowIndex - i) / (i + 1)
    #     triangle[i + 1] = triangle[rowIndex - 1 - i] = val
    #
    # print(triangle)
    # return triangle


if __name__ == '__main__':
    a = 3
    print(getRow(a) == [1, 3, 3, 1])

    b = 0
    print(getRow(b) == [1])

    c = 1
    print(getRow(c) == [1, 1])

    d = 4
    print(getRow(d) == [1, 4, 6, 4, 1])

    e = 5
    print(getRow(e) == [1, 5, 10, 10, 5, 1])
