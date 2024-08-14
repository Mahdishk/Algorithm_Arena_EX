def swap(a, b):
    return b, a

def gcd(a, b):
    if a < b:
        a, b = swap(a, b)

    if (a % b == 0):
        return b
    else:
        return gcd(b, a % b)


if __name__ == '__main__':
    a = int(input('Enter number'))
    b = int(input('Enter another number'))
    print(gcd(a, b))