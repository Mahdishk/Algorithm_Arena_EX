def swap(a, b):
    return b, a

def gcd(a, b):
    if a < b:
        a, b = swap(a, b)

    if (b == 0):
        return a
    else:
        return gcd(b, a % b)

def ggcd(arr):
    max_num = max(arr)
    count = [0] * (max_num + 1)


    for num in arr:
        count[num] += 1


    for gcd_candidate in range(max_num, 0, -1):
        multiples_count = 0
        for multiple in range(gcd_candidate, max_num + 1, gcd_candidate):
            multiples_count += count[multiple]
        if multiples_count > 1:
            return gcd_candidate

def get_array_from_input():
    user_input = input('Enter numbers that seprate with space:')
    return list(map(int, user_input.split()))

if __name__ == '__main__':
    amount_of_num = int(input('Enter amount of number:'))
    arr = get_array_from_input()
    print(ggcd(arr))
