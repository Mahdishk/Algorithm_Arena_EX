def find_prime(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not primes
    p = 2
    while p * 2 <= n:
        if primes[p]:
            for i in range(p * 2, n + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, n + 1) if primes[p]]

def amount_of_so_prime(num):
    primes = find_prime(num)
    prime_set = set(primes)  # For O(1) lookup
    count = 0

    for prime in primes:
        if '0' in str(prime):
            continue
        sum_digits = 0
        sum_digits = sum(int(digit) for digit in str(prime))
        if sum_digits in prime_set:
            count += 1

    return count

if __name__ == '__main__':
    num = int(input())
    print(amount_of_so_prime(num))
