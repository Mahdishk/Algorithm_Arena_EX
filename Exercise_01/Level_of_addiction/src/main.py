import math
from functools import reduce

def get_array_form_input():
    user_input = input()
    return list(map(int, user_input.split()))

def gcd_of_list(arr):
    return reduce(math.gcd, arr)

def amount_of_material(n, arr):
    best_gcd = gcd_of_list(arr)
    materials = sum(x // best_gcd for x in arr)
    return materials

if __name__ == '__main__':
    n = int(input())
    arr = get_array_form_input()
    print(amount_of_material(n, arr))