def make_one(a):
    remainder = 1 % a
    k = 1
    result = "1"

    while remainder != 0:
        remainder = (remainder * 10 + 1) % a
        result += "1"
        k += 1

        if k > 1000000:  # Prevent excessive computation
            return -1

    return result


if __name__ == '__main__':
    num = int(input())
    result = int(make_one(num))
    print(result // num)