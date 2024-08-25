def find_k_perfect_numbers(num, k):
    # Step 1: Initialize an array to store the sum of proper divisors
    sum_div = [0] * (num + 1)

    # Step 2: Sieve-like approach to calculate the sum of proper divisors
    for i in range(1, num + 1):
        for j in range(2 * i, num + 1, i):
            sum_div[j] += i

    # Step 3: Find and collect all k-perfect numbers
    k_perfect_numbers = []
    for i in range(2, num + 1):
        if sum_div[i] + k == i:
            k_perfect_numbers.append(i)

    if k_perfect_numbers == []:
        return -1

    return ' '.join(map(str, k_perfect_numbers))

def get_array_from_input():
    user_input = input()
    return list(map(int, user_input.split()))

if __name__ == '__main__':
    num, k = get_array_from_input()
    print(find_k_perfect_numbers(num, k))