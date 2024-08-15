def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = arr[len(arr) // 2]
    left = []
    right = []
    middle = []

    for x in arr:
        if x < mid:
            left.append(x)
        elif x > mid:
            right.append(x)
        elif x == mid:
            middle.append(x)

    return quick_sort(left) + middle + quick_sort(right)

def get_array_from_input():
    user_input = input('Enter numbers that seprate with space:')
    return list(map(int, user_input.split()))

if __name__ == '__main__':
    arr = get_array_from_input()
    sorted_arr = quick_sort(arr)
    print(' '.join(map(str, sorted_arr)))