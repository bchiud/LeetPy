def myPow(x: float, n: int) -> float:
    """
    time: log(n)
    space: log(n)
    """
    if n == 0:
        return 1
    if n < 0:
        return 1 / myPow(x, -n)
    if n % 2:
        return x * myPow(x, n - 1)
    return myPow(x * x, n / 2)

    """
    time: log(n)
    space: 1
    """
    if n < 0:
        x = 1 / x
        n = -n
    ans = 1
    while n:
        if n % 2:
            ans *= x
            n -= 1
        else:
            x *= x
            n /= 2
    return ans