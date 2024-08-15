def swap(a: int, b: int) -> tuple[int, int]:
    """To swap to elments

    :param a: number 1
    :param b: number 2
    :return: tuple(number 2, number 1)
    """
    return b, a

def gcd(a: int, b: int) -> int:
    """Find GCD of two numbers

    :param a: number 1
    :param b: number 2
    :return: GCD of number 1 and number 2
    """
    if a < b:
        a, b = swap(a, b)

    if (b == 0):
        return a
    else:
        return gcd(b, a % b)


if __name__ == '__main__':
    a = int(input('Enter number:'))
    b = int(input('Enter another number:'))
    print(gcd(a, b))