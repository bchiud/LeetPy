def fib(n: int) -> int:
    """
    time: n
    space: n
    """
    # if n <= 1:
    #     return n
    #
    # nums = [0] * n
    # nums[0] = 0
    # nums[1] = 1
    #
    # for i in range(2, n):
    #     nums[i] = nums[i - 2] + nums[i - 1]
    #
    # return nums[n - 2] + nums[n - 1]

    """
    time: n
    space: 1
    """
    # if n <= 1:
    #     return n
    #
    # first = 0
    # second = 1
    #
    # for i in range(2, n):
    #     first, second = second, first + second
    #
    # return first + second

    """
    time: 1
    space: 1
    """

    phi = (1 + 5 ** 0.5) / 2
    print(((phi ** n) + 1) // (5 ** 0.5))
    return ((phi ** n) + 1) // (5 ** 0.5)


if __name__ == '__main__':
    print(fib(2) == 1)
    print(fib(3) == 2)
    print(fib(4) == 3)
    print(fib(5) == 5)
    print(fib(6) == 8)
    print(fib(7) == 13)
    print(fib(8) == 21)
