

def multiply(num1: str, num2: str) -> str:
    n1, n2 = len(num1), len(num2)

    if n1 == 0 or n2 == 0 or num1 == "0" or num2 == "0":
        return "0"

    arr = [0] * (n1 + n2)
    for i in range(n1 - 1, -1, -1):
        for j in range(n2 -1, -1, -1):
            current = arr[i + j + 1] + (int(num1[i]) * int(num2[j]))
            arr[i + j + 1] = current % 10
            arr[i + j] += current // 10

    # remove leading 0's
    for i, v in enumerate(arr):
        if v != 0:
            return "".join([str(i) for i in arr[i:]])

    return "0"


if __name__ == '__main__':
    print(multiply("2", "3") == "6")
    print(multiply("123", "456") == "56088")